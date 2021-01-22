import cv2

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


def ProcessImage(img):
    image = cv2.imread(img)
    rn = remove_noise(image)
    gray = get_grayscale(rn)
    thresholding = thresholding(gray)

    return pt.image_to_string(thresholding,lang='eng')


if __name__=='__main__':
    pass