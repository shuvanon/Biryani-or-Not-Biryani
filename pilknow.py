from __future__ import print_function
from PIL import Image
import glob
import os
import imghdr


fileNames = glob.glob("Test Image/*.*")
for name in fileNames:
    im = Image.open(name)
    if(im.format!='JPEG'):
        print(name)
        print(im.format, im.size, im.mode)
