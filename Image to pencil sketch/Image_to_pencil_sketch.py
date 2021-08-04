import numpy as np
import imageio
import scipy.ndimage
import cv2

img = "MS.jpg"

def rgb2gray(rgb):
    return np.dot(rgb[...,:3],[0.2989,0.5870,0.1140])
    # it is 2 dimensional array formula to covert image to gray scale


def dodge(front,back):
    final_sketch=front*255/(255-back)
    #if image is greater than 255 which i dont think is possible but still if it is thre will convert it to 255
    final_sketch[final_sketch>255]=255
    final_sketch[back==255]=255
    #to convert any suitable existing column to categorical type we will accept function
    #and uint8 is for 8-bit signed integer
    return final_sketch.astype('uint8')


ss = imageio.imread(img)  # to read the given image
gray=rgb2gray(ss)#first we will image to black andwhite tat means gray scale

i=255-gray #0,0,0 is for darkest colour and 255,255,255 is for brightest colour which is probably white colour

#to convert in to blur image
blur=scipy.ndimage.filters.gaussian_filter(i,sigma=15)
#sigma is the intensity of blurness of image
r=dodge(blur,gray)#this function wil convert our image to sketch by taking two parameters as blur and gray
cv2.imwrite('MS_sketch.png',r)
