import requests
import re
import base64
import io
#分析字体工具 pip install fontTools
from fontTools.ttLib import TTFont
def get_maoyan():
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
    }
    url = "http://piaofang.maoyan.com/?ver=normal&isid_key=360E0FA91FBBA0DFF3E1AE8BA32954157F7FE4359FA31FCE3348D5A8176721C3"

    res = requests.get(url,headers=headers)
    html = res.text
    # print(html)
    result = re.search(r'charset=utf-8;base64,(.+?)\)',html)

    return html,result.group(1)

def analys_font():
    html,font_face = get_maoyan()
    font_data = base64.b64decode(font_face)
    # with open('maoyan.ttf','wb') as fp:
    #     fp.write(font_data)
    # font = TTFont("maoyan.ttf")
    baseFont = TTFont("maoyan.ttf")
    # font.saveXML("maoyan.xml")
    baseGlyf = baseFont['glyf']  #拿到 字体 和形状的关系
    baseFontMap = {
        0:baseGlyf['uniF1C6'],
        1:baseGlyf['uniE2FD'],
        2:baseGlyf['uniEEE1'],
        3:baseGlyf['uniEA6D'],
        4:baseGlyf['uniE4A1'],
        5:baseGlyf['uniE20B'],
        6:baseGlyf['uniF8F2'],
        7:baseGlyf['uniF22E'],
        8:baseGlyf['uniEAD8'],
        9:baseGlyf['uniEBDA'],
    }
    font = TTFont(io.BytesIO(font_data))
    glyf = font['glyf']

    #获取code和 name的关系
    codeNameMap = font.getBestCmap()
    #print(type(codeNameMap)) #dict 字典
    #print(codeNameMap)
    #{120: 'x', 57379: 'uniE023', 57504: 'uniE0A0', 57841: 'uniE1F1', 59146: 'uniE70A', 60219: 'uniEB3B', 60635: 'uniECDB', 60801: 'uniED81', 61047: 'uniEE77', 62505: 'uniF429', 63419: 'uniF7BB'}
    for code,name in codeNameMap.items():
        #print(hex(code))#页面上显示的代码就是  57379 的16进制
        #并且将0替换成空  前面拼接&# 最后面拼接;
        #组成页面上真正显示的代号
        codeStr = "&#"+str(hex(code)).replace("0","",1)+";"
        #根据name取出字体的形状
        currentShape = glyf[name]
        #再循环之前找好的文字和形状的关系  形状是一样的话 取出对应的文字
        for number,shape in baseFontMap.items():
            #如果形状是一样的 那么就找到这个文字了
            if shape == currentShape:
                html = re.sub(codeStr,str(number),html)
    with open('maoyan.html','w',encoding='utf-8') as fp:
        fp.write(html)
def main():
    # get_maoyan()
    analys_font()


if __name__ == "__main__":
    main()