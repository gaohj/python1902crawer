#encoding:utf-8
import pytesseract
from PIL import Image
import urllib.request
import time

def main():
    pytesseract.pytesseract.tesseract_cmd = r'C:\www\Tesseract-OCR\tesseract.exe'
    # url = 'https://passport.lagou.com/vcode/create?from=register&refresh=1513082291955'
    url = 'http://icode.renren.com/getcode.do?t=web_login&amp;rnd=0.9851688715185922'
    while True:
        urllib.request.urlretrieve(url,'captcha.png')
        img = Image.open('captcha.png')
        text = pytesseract.image_to_string(img,lang='eng')
        print(text)
        time.sleep(2)

if __name__ == "__main__":
    main()
