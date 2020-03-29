from PIL import Image
import argparse
import math
import numpy as np
import random
import sys



# 70 levels of gray
gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
# 10 levels of gray
gscale2 = '@%#*+=-:. '
def getAverageL(image):
    im = np.array(image)
    w,h = im.shape
    return np.average(im.reshape(w*h))

def covertImageToAscii(fileName, cols, scale, moreLevels):
    global gscale1, gscale2
    image = Image.open(fileName).convert('L')
    W, H = image.size[0], image.size[1]
    print("input image dims: %d x %d" % (W, H))
    w = W/cols
    h = w/scale
    rows = int(H/h)
    print("cols: %d, rows: %d" % (cols, rows))
    print("tile dims: %d x %d" % (w, h))
    if cols > W or rows > H:
        print("Image too small for specified cols!")
        exit(0)
    aimg = []
    for j in range(rows):
        y1 = int(j*h)
        y2 = int((j+1)*h)
        if j == rows-1:y2 = H
        aimg.append("")
        for i in range(cols):
            x1 = int(i*w)
            x2 = int((i+1)*w)
            if i == cols-1:x2 = W
            img = image.crop((x1, y1, x2, y2))
            avg = int(getAverageL(img))
            if moreLevels:gsval = gscale1[int((avg*69)/255)]
            else:gsval = gscale2[int((avg*9)/255)]
            aimg[j] += gsval
    return aimg

def main():
    # imgFile=input('>FILE>')
    imgFile="img.jpg"
    outFile = 'out.txt'
    scale = 0.43
    cols = 100
    print('generating ASCII art...')
    aimg = covertImageToAscii(imgFile, cols, scale, False)
    f = open(outFile, 'w')
    for row in aimg:f.write(row + '\n')
    f.close()
    print("ASCII art written to %s" % outFile)

if __name__ == '__main__':
    main()
