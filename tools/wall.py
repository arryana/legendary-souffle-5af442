#!/usr/bin/env python3
"""Build the landing page's three wall pictures from her own photographs.

    python3 tools/wall.py  <sagnegalleryshelveswood.png>  <sagneplateblank.jpg>

Everything the page draws on is made here, so the steps are recorded rather than
living in a scratchpad.  Her originals are in her `daidle` Drive folder; nothing
in this script invents anything, it only moves her own pixels about.

The five boards in her photograph sit at rows 164, 320, 480, 634 and 789.
Every number below was measured off that picture, not chosen.
"""
import sys, numpy as np
from PIL import Image, ImageFilter

SRC_BOARDS = [(164,195),(320,345),(480,499),(634,659),(789,820)]
SKIRTING   = 895          # where the baseboard's top moulding begins
FLOOR      = 944          # where the floorboards begin

def load(p):  return np.asarray(Image.open(p).convert('RGB')).astype(np.float64)
def save(a,p):
    Image.fromarray(np.clip(a,0,255).astype(np.uint8)).save(p, quality=94)
    print(f'   wrote {p}  {a.shape[1]}x{a.shape[0]}')

def trade_floor_for_wall(a, shift=40):
    """Half the floor is dead space; the wall above the top shelf is not enough.
    Stretch the plain wall above the first board by `shift` and crop the same off
    the floor, so the picture is the same size with the room better spent."""
    H,W,_ = a.shape
    top = a[:141]
    ys  = np.linspace(0,140,141+shift)
    i0=np.clip(np.floor(ys).astype(int),0,140); i1=np.clip(i0+1,0,140); f=(ys-i0)[:,None,None]
    return np.vstack([top[i0]*(1-f)+top[i1]*f, a[141:]])[:H]

def clean_bays(a, boards, bottom):
    """Her idea: the wall above the top shelf has no shadow on it, so use that
    same wall in every bay.  Under each board the wall was almost black (about 3
    of 255) and took a hundred rows to recover; the clean band is 20 at its
    darkest.  Taken across the middle only, so the picture keeps its own corners."""
    H,W,_ = a.shape
    clean = a[0:180]
    x = np.arange(W).astype(float)
    wx = (np.clip((x-100)/110,0,1) * np.clip((W-100-x)/110,0,1))[None,:,None]
    out = a.copy()
    spans = [(boards[i][1], boards[i+1][0]) for i in range(len(boards)-1)] + [(boards[-1][1], bottom)]
    for y0,y1 in spans:
        h=y1-y0
        ys=np.linspace(0,clean.shape[0]-1,h)
        i0=np.floor(ys).astype(int); i1=np.clip(i0+1,0,clean.shape[0]-1); f=(ys-i0)[:,None,None]
        new = clean[i0]*(1-f)+clean[i1]*f
        wy=np.ones((h,1,1)); fe=8
        for i in range(fe): wy[i]=min(1,i/fe); wy[-1-i]=min(1,i/fe)
        m=wy*wx
        out[y0:y1]=np.clip(a[y0:y1]*(1-m)+new*m,0,255)
    return out

def match_cabinet(a, cabinet):
    """Her call: use the colours that are in the cabinet.  Its interior is a slate
    (49,62,74); this wall was a saturated navy (20,28,43).  Painted wall only --
    the walnut keeps its own colour."""
    C = np.vstack([cabinet[y0:y1,150:880].reshape(-1,3) for y0,y1 in
                   [(150,260),(360,460),(560,660),(760,860),(960,1080)]])
    cm, cs = C.mean(axis=0), C.std(axis=0)
    warm = a[:,:,0]-a[:,:,2]
    m = np.clip((2.0-warm)/12.0, 0, 1)
    m = np.asarray(Image.fromarray((m*255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(2))).astype(float)/255
    wp = a[m>0.85]; wm, ws = wp.mean(axis=0), wp.std(axis=0)
    matched = np.clip((a-wm)/np.maximum(ws,1e-6)*cs + cm, 0, 255)
    return np.clip(a + (matched-a)*m[:,:,None], 0, 255)

def widen(a, pad=180):
    """The desktop picture is cropped to the WINDOW's shape by its sides, never its
    foot -- the ends of the wall are bare and the floor is not. So give it more of
    its own plain wall at each end for the window to take."""
    H,W,_ = a.shape
    def stretch(block, out_w, flip):
        src = block[:, ::-1] if flip else block
        xs = np.linspace(0, src.shape[1]-1, out_w)
        i0=np.floor(xs).astype(int); i1=np.clip(i0+1,0,src.shape[1]-1); f=(xs-i0)[None,:,None]
        g = src[:,i0]*(1-f) + src[:,i1]*f
        return g[:, ::-1] if flip else g
    left  = stretch(a[:, :110], 110+pad, True)
    right = stretch(a[:, -110:], 110+pad, False)
    return np.concatenate([left, a[:, 110:-110], right], axis=1)

def narrow(a, board_l, board_r, margin, keep, feather=26):
    """Her idea for phones: shorten the shelves.  The slice comes out of the
    MIDDLE, so every board keeps both of its real ends and the wall its corners."""
    half=keep//2
    L0=board_l-margin; L1=L0+margin+half
    R1=board_r+margin; R0=R1-margin-(keep-half)
    left, right = a[:,L0:L1], a[:,R0:R1]
    out=np.concatenate([left,right],axis=1); j=left.shape[1]
    for i in range(feather):
        t=i/feather
        out[:, j-feather+i] = left[:, -feather+i]*(1-t) + right[:, i]*t
    return out

def shorten(a, boards, bottom_row, top, bay, out_h):
    """Bring the shelves closer together so five of them fit a phone screen, with
    the boards themselves carried across rigid so no wood is stretched."""
    a = a[:bottom_row+1]; H,W,_ = a.shape
    dst=[top+bay*i for i in range(len(boards))]
    sp=[0.0]; dp=[0.0]
    for (t,b),d in zip(boards,dst):
        s=d-(t+b)//2; sp+=[t,b]; dp+=[t+s,b+s]
    sp+=[H-1]; dp+=[out_h-1]
    ys=np.arange(out_h,dtype=float); src=np.interp(ys,dp,sp)
    i0=np.clip(np.floor(src).astype(int),0,H-1); i1=np.clip(i0+1,0,H-1); f=(src-i0)[:,None,None]
    return a[i0]*(1-f)+a[i1]*f, [[t+(d-(t+b)//2), b+(d-(t+b)//2)] for (t,b),d in zip(boards,dst)]

if __name__ == '__main__':
    shelf_src, plate_src = sys.argv[1], sys.argv[2]
    cabinet = load('shelves-navy.jpg')

    # ---- desktop: 1536x1024, her picture with the room better spent ------------
    a = trade_floor_for_wall(load(shelf_src), 40)
    B = [[t+40, b+40] for t, b in SRC_BOARDS]
    a = clean_bays(a, B, SKIRTING+40)
    a = match_cabinet(a, cabinet)
    PAD = 563   # enough plain wall that the widest window crops sides, never the foot
    save(widen(a, PAD), 'wall-desktop.jpg')
    print('   desktop boards:', B, ' everything shifted right by', PAD)

    # ---- phone: shelves shortened from the middle, bays closed up --------------
    p, pb = shorten(narrow(a, 169, 1362, 25, 380), B, 936, 191, 121, 728)
    save(p, 'wall-phone.jpg');    print('   phone boards:', pb)

    # ---- three-inch phone: shorter again --------------------------------------
    j, jb = shorten(narrow(a, 169, 1362, 14, 296), B, 936, 158, 100, 600)
    save(j, 'wall-small.jpg');    print('   small boards:', jb)

    # ---- the brass plate, cut off its ground and turned down -------------------
    pl = Image.open(plate_src).convert('RGB')
    q  = np.asarray(pl).astype(float)
    m  = (q[:,:,0]-q[:,:,2]) > 22;  m[:180] = False   # the brushed plate, on grey
    on = np.where(m.sum(axis=0) > 120)[0]
    runs=[]; s0=on[0]; prev=on[0]
    for x in on[1:]:
        if x-prev > 10: runs.append((s0,prev)); s0=x
        prev=x
    runs.append((s0,prev))
    x0,x1 = max(runs, key=lambda r: r[1]-r[0])
    rows = np.where(m[:, x0:x1+1].sum(axis=1) > (x1-x0)*0.5)[0]
    c = pl.crop((x0-2, rows[0]-2, x1+3, rows[-1]+3))
    w = np.asarray(c).astype(float)
    al = np.clip(((w[:,:,0]-w[:,:,2])-14)/12.0, 0, 1)
    msk = Image.fromarray((al*255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.8))
    dim = 255.0*np.power(np.clip(w/255.0,0,1), 1.30)*0.92     # her call: it was glary
    out = Image.fromarray(np.dstack([np.clip(dim,0,255), np.asarray(msk)]).astype(np.uint8), 'RGBA')
    out.save('sagne-plate.png');  print(f'   wrote sagne-plate.png  {out.size[0]}x{out.size[1]}')
