from PIL import Image
import numpy as np, json, os

six  = np.asarray(Image.open('shelfsrc/sagnemuseumshelfsprite.jpg').convert('RGB')).astype(np.float64)
three= np.asarray(Image.open('shelfsrc/sagnemuseumshelfwalls.jpg').convert('RGB')).astype(np.float64)
H,W,_ = six.shape
base = six.copy()
T,B,F = 300,372,14
w=np.ones((B-T,1,1))
for i in range(F): w[i]=w[-1-i]=i/F
base[T:B] = six[T:B]*(1-w) + three[T:B]*w

SOFFIT=(0,78); BOARDS=[(148,181),(229,260),(387,414),(474,502),(555,596)]
X0,X1 = 270,1140
OUTW  = 760
GAPS  = [120,145,170,195,220]
meta  = []

def render(gap, ratio):
    B1 = 300; B5 = B1 + 4*gap; OH = B5 + 165
    DST=[round(B1+(B5-B1)*i/4) for i in range(5)]
    sp=[SOFFIT[0],SOFFIT[1]]; dp=[SOFFIT[0],SOFFIT[1]]
    for (a,b),d in zip(BOARDS,DST):
        s=d-(a+b)//2; sp+=[a,b]; dp+=[a+s,b+s]
    sp+=[H-1]; dp+=[OH-1]
    ys=np.arange(OH,dtype=float); src=np.interp(ys,dp,sp)
    i0=np.clip(np.floor(src).astype(int),0,H-1); i1=np.clip(i0+1,0,H-1); f=(src-i0)[:,None,None]
    wall=base[i0]*(1-f)+base[i1]*f
    if ratio < 1.0:
        L=wall.mean(axis=2,keepdims=True)
        wall=np.clip(wall*(np.where(L>60,60+(L-60)*ratio,L)/np.maximum(L,1e-6)),0,255)
    wall=wall[:, X0:X1]
    bands=[(a+(d-(a+b)//2), b+(d-(a+b)//2)) for (a,b),d in zip(BOARDS,DST)]
    im=Image.fromarray(np.clip(wall,0,255).astype(np.uint8))
    sc=OUTW/im.width
    im=im.resize((OUTW, round(im.height*sc)), Image.LANCZOS)
    return im, [(round(t*sc), round(b*sc)) for t,b in bands], round(SOFFIT[1]*sc)

for gi,gap in enumerate(GAPS):
    for li,ratio in enumerate([1.0, 0.30]):
        im,bands,sof = render(gap, ratio)
        im.save(f'tool/wall-{gi}-{li}.jpg', quality=80, optimize=True)
    meta.append({'gap':gap,'h':im.height,'bands':bands,'soffit':sof})
json.dump(meta, open('tool/walls.json','w'))
print(json.dumps(meta[0]), '...', len(GAPS),'spacings')
os.system('du -sh tool')
