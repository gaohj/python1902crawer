#encoding:utf-8
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\www\Tesseract-OCR\tesseract.exe'
img = Image.open('a.png')

text = pytesseract.image_to_string(img,lang='eng')

print(text)