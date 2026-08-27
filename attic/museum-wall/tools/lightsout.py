from PIL import Image, ImageFilter, ImageDraw
import numpy as np, os, sys
REPO='/home/user/legendary-souffle-5af442/'

W = np.asarray(Image.open('shelf5-a.jpg').convert('RGB').crop((214,0,1194,742))).astype(np.float64)
H,CW,_ = W.shape
BANDS  = [(148,181),(252,283),(357,384),(458,486),(555,596)]
SOFFIT = 88                     # rows above this are the ceiling recess: leave it alone
LAMPX  = [250, 490, 730]        # the recessed lamps sit under the ceiling ones

# 1. take the lamps out of the shelves. a board is uniform along its length,
#    so each fixture is replaced with clean board from further along the same shelf.
for top,bot in BANDS:
    y0,y1 = top-2, bot+8
    for x in LAMPX:
        x0,x1 = x-30, x+30
        dx = 115 if x1+115 < 850 else -115
        patch = W[y0:y1, x0+dx:x1+dx].copy()
        m = np.ones((y1-y0, x1-x0, 1))
        f = 10
        for i in range(f):
            m[:, i] = np.minimum(m[:, i], i/f); m[:, -1-i] = np.minimum(m[:, -1-i], i/f)
            m[i, :] = np.minimum(m[i, :], i/f); m[-1-i, :] = np.minimum(m[-1-i, :], i/f)
        W[y0:y1, x0:x1] = W[y0:y1, x0:x1]*(1-m) + patch*m

# 2. put the pools out. divide by the light that's falling, but only ever DARKEN —
#    so hot spots come down to the ambient and the shadows under the shelf ends stay put.
L  = W.mean(axis=2)
Li = Image.fromarray(np.clip(L,0,255).astype(np.uint8))
lit   = np.asarray(Li.filter(ImageFilter.GaussianBlur(34))).astype(np.float64)
broad = np.asarray(Li.filter(ImageFilter.GaussianBlur(230))).astype(np.float64)
gain  = np.clip(broad/np.maximum(lit,4.0), 0.35, 1.0)
gain[:SOFFIT] = 1.0                                  # the ceiling lamps stay lit
ramp = np.clip((np.arange(H)-SOFFIT)/26.0, 0, 1)[:,None]
gain = 1.0 + (gain-1.0)*ramp
W = np.clip(W*gain[:,:,None], 0, 255)

canvas = Image.fromarray(W.astype(np.uint8)).convert('RGBA')

# ---- the pieces, exactly as before -------------------------------------------
def cut_bright(img, box, lo, hi, feather=1.2):
    c=img.crop(box).convert('RGB')
    lum=np.asarray(c).astype(float).mean(axis=2)
    m=Image.fromarray((np.clip((lum-lo)/(hi-lo),0,1)*255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(feather))
    o=c.convert('RGBA'); o.putalpha(m); return o
ss=Image.open('shelfsrc/sagnecardstand1.jpg')
STAND=cut_bright(ss,(905,163,1175,556),80,120); WIN=(30,27,240,362)
ts=Image.open('shelfsrc/sagnemainpagetags.jpg')
TAG_S=cut_bright(ts,(205,258,695,520),45,90); TAG_Q=cut_bright(ts,(715,258,1205,520),45,90)

def shadow(sz,blur,alpha,ell=True):
    s=Image.new('RGBA',(sz[0]+blur*4,sz[1]+blur*4),(0,0,0,0)); d=ImageDraw.Draw(s)
    box=[blur*2,blur*2,blur*2+sz[0],blur*2+sz[1]]
    (d.ellipse if ell else d.rectangle)(box,fill=(0,0,0,alpha))
    return s.filter(ImageFilter.GaussianBlur(blur))

def card(cp,cx,baseline,h):
    sc=h/STAND.height
    st=STAND.resize((max(1,round(STAND.width*sc)),h),Image.LANCZOS)
    wx0,wy0,wx1,wy1=[round(v*sc) for v in WIN]
    im=Image.open(REPO+cp).convert('RGB').resize((wx1-wx0,wy1-wy0),Image.LANCZOS)
    p=Image.new('RGBA',st.size,(0,0,0,0)); p.paste(im,(wx0,wy0)); p=Image.alpha_composite(p,st)
    x=round(cx-p.width/2)
    sh=shadow((p.width,max(4,round(p.height*0.05))),5,110)
    canvas.alpha_composite(sh,(x-10,baseline-sh.height//2-2))
    canvas.alpha_composite(p,(x,baseline-p.height))

def tag(t,cx,cy,h):
    sc=h/t.height; im=t.resize((round(t.width*sc),h),Image.LANCZOS)
    x=round(cx-im.width/2); y=round(cy-im.height/2)
    canvas.alpha_composite(shadow((im.width,im.height),7,110,False),(x-14,y-10))
    canvas.alpha_composite(im,(x,y))

def plate(name,band,cx):
    p=Image.open(REPO+f'shelfplate-{name}.png').convert('RGBA')
    top,bot=band; h=max(9,round((bot-top)*0.50)); sc=h/p.height
    p=p.resize((round(p.width*sc),h),Image.LANCZOS)
    canvas.alpha_composite(p,(round(cx-p.width/2),round(top+(bot-top)*0.30)))

G=[('instrumenta',['candler/candle-card.png','conometer/conometer-card.png','galileo/galileo-card.png','windower/windower-card.png','storm/storm-card.png']),
   ('tactilia',['warmler/warmler-card.png','roller/roller-card.png','kaleidoscope/kaleidoscope-card.png']),
   ('systema',['gyre/gyre-card.png','musebox/musebox-card.png','chimes/chimes-card.png']),
   ('natura',['birds/birds-card.png','fireflies/fireflies-card.png','moths/moths-card.png','ant/ant-card.png']),
   ('phenomena',['bowl/bowl-card.png','chladni/chladni-card.png','rain/rain-card.png','lamp/lamp-card.png','pendulum/pendulum-card.png'])]
SX0,SX1=131,856; CH=int(os.environ.get('CH',92))
strips=[(b,canvas.crop((0,b[0],CW,b[1]+1)).copy()) for b in BANDS]
for (name,cards),band in zip(G,BANDS):
    n=len(cards); span=SX1-SX0; pitch=span/5.0; mid=(SX0+SX1)/2
    for cp,k in zip(cards,range(n)):
        card(cp, mid+pitch*(k-(n-1)/2), band[0]+2, CH)
for b,st in strips[:2]: canvas.paste(st,(0,b[0]))
for (name,_),band in zip(G,BANDS): plate(name,band,(SX0+SX1)/2)
tag(TAG_S, CW/2, (SOFFIT + (BANDS[0][0]-CH))/2 + 4, 46)
tag(TAG_Q, CW/2, (BANDS[4][1] + H)/2 + 20, 34)
canvas.convert('RGB').save(sys.argv[1], quality=94)
print('->',sys.argv[1], canvas.size)
