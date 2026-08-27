from PIL import Image
import numpy as np, sys

six  = np.asarray(Image.open('shelfsrc/sagnemuseumshelfsprite.jpg').convert('RGB')).astype(np.float64)
three= np.asarray(Image.open('shelfsrc/sagnemuseumshelfwalls.jpg').convert('RGB')).astype(np.float64)
H,W,_ = six.shape

# --- 1. remove the third board (rows 316-339) using the clean wall from the 3-shelf photo,
#        which was shot on the same wall with the same camera and has nothing there.
PATCH_TOP, PATCH_BOT = 300, 372          # generous: board + its shadow
FEATHER = 14
base = six.copy()
w = np.ones((PATCH_BOT-PATCH_TOP,1,1))
for i in range(FEATHER):
    w[i] = w[-1-i] = i/FEATHER
base[PATCH_TOP:PATCH_BOT] = six[PATCH_TOP:PATCH_BOT]*(1-w) + three[PATCH_TOP:PATCH_BOT]*w

# --- 2. piecewise vertical remap: boards stay rigid, wall between them stretches.
BOARDS = [(148,181),(229,260),(387,414),(474,502),(555,596)]   # the five that remain
CENTRES = [ (a+b)//2 for a,b in BOARDS ]

def remap(dst_centres, out):
    # build a source-row lookup for every destination row
    src_pts, dst_pts = [0.0], [0.0]
    for (a,b),c,d in zip(BOARDS, CENTRES, dst_centres):
        shift = d - c
        src_pts += [a, b];  dst_pts += [a+shift, b+shift]      # board translated, not scaled
    src_pts += [H-1]; dst_pts += [H-1]
    ys = np.arange(H, dtype=np.float64)
    src = np.interp(ys, dst_pts, src_pts)
    i0 = np.clip(np.floor(src).astype(int), 0, H-1)
    i1 = np.clip(i0+1, 0, H-1)
    f  = (src - i0)[:,None,None]
    img = base[i0]*(1-f) + base[i1]*f
    Image.fromarray(np.clip(img,0,255).astype(np.uint8)).save(out, quality=94)
    return dst_centres

top, bot = 164, 575
even = [round(top + (bot-top)*i/4) for i in range(5)]
print('A even, same span :', even, 'gap', even[1]-even[0])
remap(even, 'shelf5-a.jpg')

top, bot = 150, 600
airy = [round(top + (bot-top)*i/4) for i in range(5)]
print('B even, more air  :', airy, 'gap', airy[1]-airy[0])
remap(airy, 'shelf5-b.jpg')
