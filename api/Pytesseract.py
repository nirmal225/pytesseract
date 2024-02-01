import pybase64

import cv2
import pytesseract


class Pytesseract:
    def save_mage(self, encoded_text):
        decoded_data = pybase64.b64decode(encoded_text)
        img_file = open('images/irctc_captcha2.jpeg', 'wb')
        img_file.write(decoded_data)
        img_file.close()

    def get_captcha(self):
        pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'
        image = cv2.imread('images/irctc_captcha2.jpeg')
        return pytesseract.image_to_string(image)
