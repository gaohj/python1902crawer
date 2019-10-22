import requests
import re
import base64
from fontTools.ttLib import TTFont
import io

# pip install fontTools

def get_maoyan():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36"
    }
    url = "http://piaofang.maoyan.com/?ver=normal&isid_key=282B478391270B849F442DE49F06496059F92BE1C0D9BE9883201E6717CF879A"
    resp = requests.get(url,headers=headers)
    html = resp.text
    result = re.search(r'charset=utf-8;base64,(.+?)\)',html)
    return html,result.group(1)

def analysis_font():
    html,font_face = get_maoyan()
    font_data = base64.b64decode(font_face)
    # with open('maoyan.ttf','wb') as fp:
    #     fp.write(font_data)
    baseFont = TTFont("maoyan.ttf")
    # font = TTFont("maoyan.ttf")
    # font.saveXML("maoyan.xml")
    baseGlyf = baseFont['glyf']
    baseFontMap = {
        0: baseGlyf['uniEE14'],
        1: baseGlyf['uniEF04'],
        2: baseGlyf['uniF2E0'],
        3: baseGlyf['uniEFE0'],
        4: baseGlyf['uniF6EF'],
        5: baseGlyf['uniE7B9'],
        6: baseGlyf['uniEE8A'],
        7: baseGlyf['uniF5B1'],
        8: baseGlyf['uniECC2'],
        9: baseGlyf['uniF410']
    }
    font = TTFont(io.BytesIO(font_data))
    glyf = font['glyf']
    # getBestCmap：获取code和name的关系
    codeNameMap = font.getBestCmap()
    for code,name in codeNameMap.items():
        codeStr = "&#" + str(hex(code)).replace("0","",1) + ";"
        # 根据name取出当前这个字体的形状
        currentShape = glyf[name]
        # 再循环之前找好的文字和形状的关系，找到当前字体对应的真正的文字
        for number,shape in baseFontMap.items():
            # 如果形状相等，说明找到了，就可以找到这个number了
            if shape == currentShape:
                html = re.sub(codeStr,str(number),html)
    with open("maoyan1.html",'w',encoding='utf-8') as fp:
        fp.write(html)


def main():
    # get_maoyan()
    analysis_font()

if __name__ == '__main__':
    main()