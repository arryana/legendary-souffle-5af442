from PIL import Image, ImageFilter
import numpy as np, sys

src = Image.open('shelf5-a.jpg').convert('RGB')
CROP = (214, 0, 1194, 742)          # the navy panel only — no room either side
im   = src.crop(CROP)
a    = np.asarray(im).astype(np.float64)

L  = a.mean(axis=2)
Li = Image.fromarray(np.clip(L,0,255).astype(np.uint8))

# glare is uneven illumination: a few hot pools over an otherwise even wall.
# estimate the light falling on the scene, and the broad gradient it *should* be,
# then divide one by the other. surface texture and material stay; hot spots go.
lit   = np.asarray(Li.filter(ImageFilter.GaussianBlur(38))).astype(np.float64)
broad = np.asarray(Li.filter(ImageFilter.GaussianBlur(210))).astype(np.float64)
gain  = np.clip(broad/np.maximum(lit,4.0), 0.45, 1.7)[:,:,None]
out   = a * gain

# hold the overall level where it was, so this reads as even light and not as dimming
out *= L.mean()/np.clip(out.mean(axis=2),0,255).mean()
out  = np.clip(out,0,255)

Image.fromarray(out.astype(np.uint8)).save('five-shelves-noglare.jpg', quality=94)

def spread(x):
    l=x.mean(axis=2) if x.ndim==3 else x
    return np.percentile(l,99.5)-np.percentile(l,50)
print(f'brightest-to-midtone spread   before {spread(a):6.1f}   after {spread(out):6.1f}')
print(f'overall level                 before {a.mean():6.1f}   after {out.mean():6.1f}')
print(f'pixels above 200/255          before {(a.mean(axis=2)>200).sum():6d}   after {(out.mean(axis=2)>200).sum():6d}')
