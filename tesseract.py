import cv2
import numpy as np
import pytesseract as pt
pt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


# get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# noise removal
def remove_noise(image):
    return cv2.medianBlur(image,5)
    
#Threading
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

def opening(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

def ProcessImage(img):
    image = cv2.imread(img)
    rn = remove_noise(image)
    gray = get_grayscale(rn)
    openin = opening(gray)
    thresh  = thresholding(openin)
    # cv2.imwrite('testout2.jpg',thresh)
    text = pt.image_to_string(thresh,lang='eng')
    text = text.split(' ')
    textoutput = ''
    for i in text:
        textoutput+=' '+i

    return textoutput


if __name__=='__main__':
    print(ProcessImage('test.jpg'))