from PIL import Image, ImageFilter, ImageDraw
import numpy as np, os, sys
REPO='/home/user/legendary-souffle-5af442/'

six  = np.asarray(Image.open('shelfsrc/sagnemuseumshelfsprite.jpg').convert('RGB')).astype(np.float64)
three= np.asarray(Image.open('shelfsrc/sagnemuseumshelfwalls.jpg').convert('RGB')).astype(np.float64)
SH,SW,_ = six.shape
base=six.copy(); T,B,F=300,372,14
w=np.ones((B-T,1,1))
for i in range(F): w[i]=w[-1-i]=i/F
base[T:B]=six[T:B]*(1-w)+three[T:B]*w

SOF=(0,78); SRCB=[(148,181),(229,260),(387,414),(474,502),(555,596)]
OH=int(os.environ.get('OH',1170)); B1=int(os.environ.get('B1',300)); B5=int(os.environ.get('B5',1000))
DST=[round(B1+(B5-B1)*i/4) for i in range(5)]
sp=[SOF[0],SOF[1]]; dp=[SOF[0],SOF[1]]
for (a,b),d in zip(SRCB,DST):
    s=d-(a+b)//2; sp+=[a,b]; dp+=[a+s,b+s]
sp+=[SH-1]; dp+=[OH-1]
ys=np.arange(OH,dtype=float); src=np.interp(ys,dp,sp)
i0=np.clip(np.floor(src).astype(int),0,SH-1); i1=np.clip(i0+1,0,SH-1); f=(src-i0)[:,None,None]
Wall=base[i0]*(1-f)+base[i1]*f
BANDS=[(a+(d-(a+b)//2), b+(d-(a+b)//2)) for (a,b),d in zip(SRCB,DST)]
X0,X1=270,1140
Wall=Wall[:, X0:X1]; H,CW,_=Wall.shape
SOFFIT=SOF[1]+10
LAMPX=[464-X0, 704-X0, 944-X0]

# lamps out of the shelves
for top,bot in BANDS:
    y0,y1=max(0,top-2), min(H,bot+8)
    for x in LAMPX:
        x0,x1=x-30,x+30
        dx = 115 if x1+115 < CW-40 else -115
        patch=Wall[y0:y1, x0+dx:x1+dx].copy()
        # the board darkens along its length, so lift the borrowed piece onto the
        # tone of the spot it's filling — otherwise the join shows as a step
        eps=1e-6
        dL=Wall[y0:y1, x0-12:x0].mean(axis=1);      dR=Wall[y0:y1, x1:x1+12].mean(axis=1)
        sL=Wall[y0:y1, x0+dx-12:x0+dx].mean(axis=1); sR=Wall[y0:y1, x1+dx:x1+dx+12].mean(axis=1)
        gL=np.clip(dL/np.maximum(sL,eps),0.6,1.7);   gR=np.clip(dR/np.maximum(sR,eps),0.6,1.7)
        t=np.linspace(0,1,x1-x0)[None,:,None]
        patch=np.clip(patch*(gL[:,None,:]*(1-t)+gR[:,None,:]*t),0,255)
        m=np.ones((y1-y0,x1-x0,1)); fe=10
        for i in range(fe):
            m[:,i]=np.minimum(m[:,i],i/fe); m[:,-1-i]=np.minimum(m[:,-1-i],i/fe)
            m[i,:]=np.minimum(m[i,:],i/fe); m[-1-i,:]=np.minimum(m[-1-i,:],i/fe)
        Wall[y0:y1,x0:x1]=Wall[y0:y1,x0:x1]*(1-m)+patch*m

# pools out — darken only, so the shelf-end shadows survive; soffit untouched
L=Wall.mean(axis=2); Li=Image.fromarray(np.clip(L,0,255).astype(np.uint8))
lit=np.asarray(Li.filter(ImageFilter.GaussianBlur(34))).astype(np.float64)
broad=np.asarray(Li.filter(ImageFilter.GaussianBlur(240))).astype(np.float64)
g=np.clip(broad/np.maximum(lit,4.0),0.35,1.0); g[:SOFFIT]=1.0
g=1.0+(g-1.0)*np.clip((np.arange(H)-SOFFIT)/26.0,0,1)[:,None]
Wall=np.clip(Wall*g[:,:,None],0,255)
canvas=Image.fromarray(Wall.astype(np.uint8)).convert('RGBA')

def cut(img,box,lo,hi,fe=1.2):
    c=img.crop(box).convert('RGB'); lum=np.asarray(c).astype(float).mean(axis=2)
    m=Image.fromarray((np.clip((lum-lo)/(hi-lo),0,1)*255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(fe))
    o=c.convert('RGBA'); o.putalpha(m); return o
ss=Image.open('shelfsrc/sagnecardstand1.jpg'); STAND=cut(ss,(905,163,1175,556),80,120); WIN=(30,27,240,362)
ts=Image.open('shelfsrc/sagnemainpagetags.jpg')
TAG_S=cut(ts,(205,258,695,520),45,90); TAG_Q=cut(ts,(715,258,1205,520),45,90)
def sh(sz,bl,al,ell=True):
    s=Image.new('RGBA',(sz[0]+bl*4,sz[1]+bl*4),(0,0,0,0)); d=ImageDraw.Draw(s)
    bx=[bl*2,bl*2,bl*2+sz[0],bl*2+sz[1]]; (d.ellipse if ell else d.rectangle)(bx,fill=(0,0,0,al))
    return s.filter(ImageFilter.GaussianBlur(bl))
NOFRAME = os.environ.get('NOFRAME','')
def card(cp,cx,bl,h):
    if NOFRAME:
        # no brass round the picture. the card stands on the shelf, held by two small
        # dark clips, the way the cabinet on the live site does it.
        cw=round(h*0.72); im=Image.open(REPO+cp).convert('RGB').resize((cw,h),Image.LANCZOS)
        p=Image.new('RGBA',(cw,h),(0,0,0,0)); p.paste(im,(0,0))
        d=ImageDraw.Draw(p); d.rectangle([0,0,cw-1,h-1], outline=(18,22,30,190))
        x=round(cx-cw/2)
        canvas.alpha_composite(sh((cw,max(4,round(h*0.05))),5,120),(x-10,bl-4))
        canvas.alpha_composite(p,(x,bl-h))
        clip=Image.new('RGBA',(round(cw*0.30),max(3,round(h*0.035))),(26,31,40,235))
        canvas.alpha_composite(clip,(round(cx-clip.width/2), bl-clip.height))
        return
    sc=h/STAND.height; st=STAND.resize((max(1,round(STAND.width*sc)),h),Image.LANCZOS)
    a0,b0,a1,b1=[round(v*sc) for v in WIN]
    im=Image.open(REPO+cp).convert('RGB').resize((a1-a0,b1-b0),Image.LANCZOS)
    p=Image.new('RGBA',st.size,(0,0,0,0)); p.paste(im,(a0,b0)); p=Image.alpha_composite(p,st)
    x=round(cx-p.width/2)
    canvas.alpha_composite(sh((p.width,max(4,round(p.height*0.05))),5,110),(x-10,bl-4))
    canvas.alpha_composite(p,(x,bl-p.height))
def tag(t,cx,cy,h):
    sc=h/t.height; im=t.resize((round(t.width*sc),h),Image.LANCZOS)
    x=round(cx-im.width/2); y=round(cy-im.height/2)
    canvas.alpha_composite(sh((im.width,im.height),7,110,False),(x-14,y-10)); canvas.alpha_composite(im,(x,y))
def plate(n,band,cx):
    p=Image.open(REPO+f'shelfplate-{n}.png').convert('RGBA')
    t,b=band; h=max(9,round((b-t)*0.50)); sc=h/p.height
    p=p.resize((round(p.width*sc),h),Image.LANCZOS)
    canvas.alpha_composite(p,(round(cx-p.width/2),round(t+(b-t)*0.30)))
G=[('instrumenta',['candler/candle-card.png','conometer/conometer-card.png','galileo/galileo-card.png','windower/windower-card.png','storm/storm-card.png']),
   ('tactilia',['warmler/warmler-card.png','roller/roller-card.png','kaleidoscope/kaleidoscope-card.png']),
   ('systema',['gyre/gyre-card.png','musebox/musebox-card.png','chimes/chimes-card.png']),
   ('natura',['birds/birds-card.png','fireflies/fireflies-card.png','moths/moths-card.png','ant/ant-card.png']),
   ('phenomena',['bowl/bowl-card.png','chladni/chladni-card.png','rain/rain-card.png','lamp/lamp-card.png','pendulum/pendulum-card.png'])]
SX0,SX1=345-X0,1070-X0; CH=int(os.environ.get('CH',96))
strips=[(b,canvas.crop((0,b[0],CW,b[1]+1)).copy()) for b in BANDS]
for (n,cs),band in zip(G,BANDS):
    k0=len(cs); pitch=(SX1-SX0)/5.0; mid=(SX0+SX1)/2
    for k,cp in enumerate(cs): card(cp, mid+pitch*(k-(k0-1)/2), band[0]+2, CH)
for b,st in strips[:2]: canvas.paste(st,(0,b[0]))
for (n,_),band in zip(G,BANDS): plate(n,band,(SX0+SX1)/2)
tag(TAG_S, CW/2, (SOFFIT+(BANDS[0][0]-CH))/2, int(os.environ.get('TS',56)))
tag(TAG_Q, CW/2, (BANDS[4][1]+OH)/2-6, int(os.environ.get('TQ',42)))
canvas.crop((0,0,CW,int(os.environ.get('CROPH',OH)))).convert('RGB').save(sys.argv[1],quality=94)
print('->',sys.argv[1])
