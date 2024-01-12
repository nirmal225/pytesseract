#!/bin/bash

#install tesserract
sudo apt install tesseract-ocr
sudo apt install libtesseract-dev

#install pillow,opencv-python and tesseract wrapper for python
pip install pytesseract
pip install pillow
pip install opencv-python