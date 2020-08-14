'''Initial script to analyse the wavelengths of light present in an image.'''
import cv2
import numpy as np
from skimage import io
import argparse

# img = io.imread('https://i.stack.imgur.com/DNM65.png')[:, :, :-1]



# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image")
args = vars(ap.parse_args())
img = cv2.imread(args["image"])
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)



average = img.mean(axis=0).mean(axis=0)

pixels = np.float32(img.reshape(-1, 3))

n_colors = 5
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 200, .1)
flags = cv2.KMEANS_RANDOM_CENTERS

_, labels, palette = cv2.kmeans(pixels, n_colors, None, criteria, 10, flags)
_, counts = np.unique(labels, return_counts=True)
print(counts)
dominant = palette[np.argmax(counts)]
print(dominant)
img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

#RGB - Blue in Grey
# cv2.imshow('B-RGB.jpg',img[:, :, 0])

# # RGB - Green in Grey
# cv2.imshow('G-RGB.jpg',img[:, :, 1])

# # RGB Red in Grey
# cv2.imshow('R-RGB.jpg',img[:, :, 2])

b = img.copy()
# set green and red channels to 0
b[:, :, 1] = 0
b[:, :, 2] = 0


g = img.copy()
# set blue and red channels to 0
g[:, :, 0] = 0
g[:, :, 2] = 0

r = img.copy()
# set blue and green channels to 0
r[:, :, 0] = 0
r[:, :, 1] = 0

# cv2.imshow('RGB', img)

# # RGB - Blue
# cv2.imshow('B-RGB', b)

# # RGB - Green
# cv2.imshow('G-RGB', g)

# # RGB - Red
# cv2.imshow('R-RGB', r)
cv2.imshow('RGB', img)
print(img[24,45])

imghsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow('HSV', imghsv)
print(imghsv[24,45])

#change only saturation
hsvsat = imghsv.copy()
hsvsat[:, :, 1] = 255
print(hsvsat[24,45])
hsvsattorgb = cv2.cvtColor(hsvsat, cv2.COLOR_HSV2BGR)
cv2.imshow('HSV Converted Saturation', hsvsattorgb)

#change both sat and value
imghsv[:, :, 1] = 255
imghsv[:, :, 2] = 255
print(imghsv[24,45])
imghsvbacktorgb = cv2.cvtColor(imghsv, cv2.COLOR_HSV2BGR)
cv2.imshow('HSV Converted', imghsvbacktorgb)
cv2.imwrite("HSVConv.png", imghsvbacktorgb)
print(imghsvbacktorgb[24,45])

height, width, channel = imghsvbacktorgb.shape
imgwavelengths = np.zeros((height, width, 1))
imgwavelengths = imgwavelengths.astype(np.int16)
wavelengthsintensityarray = np.zeros(1000)
wavelengthscountarray = np.zeros(1000)
for i in np.arange(height):
    for j in np.arange(width):
        if imghsvbacktorgb[i,j,0] == 255 and imghsvbacktorgb[i,j,1] == 0:
            imgwavelengths[i,j,0] = int(-((imghsvbacktorgb[i,j,2]*(440-380)/255.0)-440))
        elif imghsvbacktorgb[i,j,0] == 255 and imghsvbacktorgb[i,j,2] == 0:
            imgwavelengths[i,j,0] = int(((imghsvbacktorgb[i,j,1]*(490-440)/255.0)+440))
        elif imghsvbacktorgb[i,j,1] == 255 and imghsvbacktorgb[i,j,2] == 0:
            imgwavelengths[i,j,0] = int(-((imghsvbacktorgb[i,j,0]*(510-490)/255.0)-510))
        elif imghsvbacktorgb[i,j,1] == 255 and imghsvbacktorgb[i,j,0] == 0: 
            imgwavelengths[i,j,0] = int(((imghsvbacktorgb[i,j,2]*(580-510)/255.0)+510))
        elif imghsvbacktorgb[i,j,2] == 255 and imghsvbacktorgb[i,j,0] == 0:
            imgwavelengths[i,j,0] = int(-((imghsvbacktorgb[i,j,1]*(645-580)/255.0)-645))
        elif imghsvbacktorgb[i,j,2] == 255 and imghsvbacktorgb[i,j,1] == 0: 
            imgwavelengths[i,j,0] = int(((imghsvbacktorgb[i,j,0]*(781-645)/255.0)+645))
        else:
            imgwavelengths[i,j,0] = 0
        intensity = hsvsat[i,j,2]/255
        wavelengthsintensityarray[imgwavelengths[i,j,0]] = wavelengthsintensityarray[imgwavelengths[i,j,0]]+intensity
        wavelengthscountarray[imgwavelengths[i,j,0]] = wavelengthscountarray[imgwavelengths[i,j,0]]+1 

for k in range(340,781):
    # for i in np.arange(height):
    #     for j in np.arange(width):
    #         if imgwavelengths[i,j,0] == k:
    #             intensity = hsvsat[i,j,2]/255
    #             wavelengthsintensityarray[k] = wavelengthsintensityarray[k]+intensity
    #             wavelengthscountarray[k] = wavelengthscountarray[k]+1
    if wavelengthscountarray[k]==0:
        wavelengthscountarray[k] = 1
    wavelengthsintensityarray[k] = wavelengthsintensityarray[k]/wavelengthscountarray[k]       
    # print(wavelengthsintensityarray[k])

print(wavelengthsintensityarray[510])

wavelengthsintensityarray = wavelengthsintensityarray[340:781]
wavelengthscountarray = wavelengthscountarray[340:781]
wavelengthsintensityarray = [float('nan') if x==0 else x for x in wavelengthsintensityarray]

def interpolate_gaps(values, limit=None):
    """
    Fill gaps using linear interpolation, optionally only fill gaps up to a
    size of `limit`.
    """
    values = np.asarray(values)
    i = np.arange(values.size)
    valid = np.isfinite(values)
    filled = np.interp(i, i[valid], values[valid])

    if limit is not None:
        invalid = ~valid
        for n in range(1, limit+1):
            invalid[:-n] &= invalid[n:]
        filled[invalid] = np.nan

    return filled

filled = interpolate_gaps(wavelengthsintensityarray, limit=2)



import matplotlib.pyplot as plt
plt.xlim(379, 781)
plt.bar(np.arange(340, 781),filled)
plt.show()

avg_patch = np.ones(shape=img.shape, dtype=np.uint8)*np.uint8(average)

indices = np.argsort(counts)[::-1]  
 
freqs = np.cumsum(np.hstack([[0], counts[indices]/counts.sum()]))

rows = np.int_(img.shape[0]*freqs)

dom_patch = np.zeros(shape=img.shape, dtype=np.uint8)

print("Pixels")
for i in range(5):
    print(np.uint8(palette[indices[i]]))

for i in range(len(rows) - 1):
    dom_patch[rows[i]:rows[i + 1], :, :] += np.uint8(palette[indices[i]])

fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(12,6))
ax0.imshow(avg_patch)
ax0.set_title('Average color')
ax0.axis('off')
ax1.imshow(dom_patch)
ax1.set_title('Dominant colors')
ax1.axis('off')
plt.show(fig)