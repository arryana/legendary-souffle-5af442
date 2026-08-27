from PIL import Image, ImageFilter, ImageDraw
import numpy as np, os, sys

REPO='/home/user/legendary-souffle-5af442/'
six  = np.asarray(Image.open('shelfsrc/sagnemuseumshelfsprite.jpg').convert('RGB')).astype(np.float64)
three= np.asarray(Image.open('shelfsrc/sagnemuseumshelfwalls.jpg').convert('RGB')).astype(np.float64)
H,W,_ = six.shape

base = six.copy()
T,B,F = 300,372,14
w=np.ones((B-T,1,1))
for i in range(F): w[i]=w[-1-i]=i/F
base[T:B] = six[T:B]*(1-w) + three[T:B]*w

SOFFIT = (0,78)                                  # ceiling recess + its downlights: keep rigid
BOARDS = [(148,181),(229,260),(387,414),(474,502),(555,596)]
OH     = int(os.environ.get('OH',860))           # output height — the wall stretches to fit
B1,B5  = int(os.environ.get('B1',280)), int(os.environ.get('B5',720))
DST    = [round(B1+(B5-B1)*i/4) for i in range(5)]

src_pts=[SOFFIT[0], SOFFIT[1]]; dst_pts=[SOFFIT[0], SOFFIT[1]]
for (a,b),d in zip(BOARDS, DST):
    c=(a+b)//2; s=d-c
    src_pts+=[a,b]; dst_pts+=[a+s,b+s]
src_pts+=[H-1]; dst_pts+=[OH-1]
ys=np.arange(OH,dtype=float); src=np.interp(ys,dst_pts,src_pts)
i0=np.clip(np.floor(src).astype(int),0,H-1); i1=np.clip(i0+1,0,H-1); f=(src-i0)[:,None,None]
wall = base[i0]*(1-f)+base[i1]*f
BANDS=[(a+(d-(a+b)//2), b+(d-(a+b)//2)) for (a,b),d in zip(BOARDS,DST)]

# hold the hot wood back so the pieces are the brightest thing on the wall.
# a soft knee: shadows and the navy untouched, highlights compressed.
KNEE  = float(os.environ.get('KNEE',60))
RATIO = float(os.environ.get('RATIO',0.40))
if RATIO < 1.0:
    L = wall.mean(axis=2, keepdims=True)
    Lc = np.where(L>KNEE, KNEE+(L-KNEE)*RATIO, L)
    wall = np.clip(wall * (Lc/np.maximum(L,1e-6)), 0, 255)

X0,X1 = int(os.environ.get('CX0',270)), int(os.environ.get('CX1',1140))
wall = wall[:, X0:X1]
canvas = Image.fromarray(np.clip(wall,0,255).astype(np.uint8)).convert('RGBA')
CW = X1-X0

def cut_bright(img, box, lo, hi, feather=1.2):
    c = img.crop(box).convert('RGB')
    lum = np.asarray(c).astype(float).mean(axis=2)
    m = Image.fromarray((np.clip((lum-lo)/(hi-lo),0,1)*255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(feather))
    out = c.convert('RGBA'); out.putalpha(m); return out

stand_src = Image.open('shelfsrc/sagnecardstand1.jpg')
STAND = cut_bright(stand_src,(905,163,1175,556),80,120); WIN=(30,27,240,362)
tag_src = Image.open('shelfsrc/sagnemainpagetags.jpg')
TAG_S = cut_bright(tag_src,(205,258,695,520),45,90)
TAG_Q = cut_bright(tag_src,(715,258,1205,520),45,90)

def shadow(sz, blur, alpha, ellipse=True):
    s=Image.new('RGBA',(sz[0]+blur*4, sz[1]+blur*4),(0,0,0,0)); d=ImageDraw.Draw(s)
    box=[blur*2,blur*2,blur*2+sz[0],blur*2+sz[1]]
    (d.ellipse if ellipse else d.rectangle)(box, fill=(0,0,0,alpha))
    return s.filter(ImageFilter.GaussianBlur(blur))

def place_card(cp, cx, baseline, h):
    sc=h/STAND.height
    st=STAND.resize((max(1,round(STAND.width*sc)),h), Image.LANCZOS)
    wx0,wy0,wx1,wy1=[round(v*sc) for v in WIN]
    card=Image.open(REPO+cp).convert('RGB').resize((wx1-wx0,wy1-wy0), Image.LANCZOS)
    p=Image.new('RGBA',st.size,(0,0,0,0)); p.paste(card,(wx0,wy0)); p=Image.alpha_composite(p,st)
    x=round(cx-p.width/2)
    sh=shadow((p.width, max(4,round(p.height*0.05))),5,130)
    canvas.alpha_composite(sh,(x-10, baseline-sh.height//2-2))
    canvas.alpha_composite(p,(x, baseline-p.height))

def mount_tag(tag, cx, cy, h):
    sc=h/tag.height; t=tag.resize((round(tag.width*sc),h), Image.LANCZOS)
    x=round(cx-t.width/2); y=round(cy-t.height/2)
    sh=shadow((t.width,t.height),7,120,ellipse=False)
    canvas.alpha_composite(sh,(x-14,y-14+4))
    canvas.alpha_composite(t,(x,y))

def place_plate(name, band, cx):
    p=Image.open(REPO+f'shelfplate-{name}.png').convert('RGBA')
    top,bot=band; h=max(9,round((bot-top)*0.50)); sc=h/p.height
    p=p.resize((round(p.width*sc),h), Image.LANCZOS)
    canvas.alpha_composite(p,(round(cx-p.width/2), round(top+(bot-top)*0.30)))

BOARDSTRIP=[(b,canvas.crop((0,b[0],CW,b[1]+1)).copy()) for b in BANDS]

GROUPS=[('instrumenta',['candler/candle-card.png','conometer/conometer-card.png','galileo/galileo-card.png','windower/windower-card.png','storm/storm-card.png']),
        ('tactilia',   ['warmler/warmler-card.png','roller/roller-card.png','kaleidoscope/kaleidoscope-card.png']),
        ('systema',    ['gyre/gyre-card.png','musebox/musebox-card.png','chimes/chimes-card.png']),
        ('natura',     ['birds/birds-card.png','fireflies/fireflies-card.png','moths/moths-card.png','ant/ant-card.png']),
        ('phenomena',  ['bowl/bowl-card.png','chladni/chladni-card.png','rain/rain-card.png','lamp/lamp-card.png','pendulum/pendulum-card.png'])]
SX0, SX1 = 345-X0, 1070-X0
CH = int(os.environ.get('CH',108))

for (name,cards),band in zip(GROUPS,BANDS):
    n=len(cards); span=SX1-SX0
    pitch=span/5.0; mid=(SX0+SX1)/2
    xs=[mid + pitch*(k-(n-1)/2) for k in range(n)]
    for cp,x in zip(cards,xs): place_card(cp,x,band[0]+2,CH)
    place_plate(name,band,(SX0+SX1)/2)

for b,strip in BOARDSTRIP[:2]: canvas.paste(strip,(0,b[0]))
for (name,_),band in zip(GROUPS[:2],BANDS[:2]): place_plate(name,band,(SX0+SX1)/2)

# sagne on the wall above the top shelf; ? on the wall below the bottom one
mount_tag(TAG_S, CW/2, (SOFFIT[1] + (BANDS[0][0]-CH))/2, int(os.environ.get('TS',54)))
mount_tag(TAG_Q, CW/2, (BANDS[4][1] + OH)/2 - 6,        int(os.environ.get('TQ',40)))

canvas.crop((0,0,CW,int(os.environ.get('CROPH',OH)))).convert('RGB').save(sys.argv[1], quality=94)
print('gaps',[BANDS[i+1][0]-BANDS[i][0] for i in range(4)],'card',CH,'->',sys.argv[1],canvas.size)
