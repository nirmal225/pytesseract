import cv2
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'
image = cv2.imread('images/irctc_captcha2.png')
print(pytesseract.image_to_string(image))
# inverted_image = cv2.bitwise_not(image)
# cv2.imwrite("inverted.png",inverted_image)
