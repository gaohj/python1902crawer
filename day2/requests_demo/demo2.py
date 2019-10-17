
import requests
import json
import time
def youdaoAPI(kw):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
    }
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"

    response = requests.post(url,data=kw,headers=headers)
    res = response.content.decode('utf-8')
    dicts = json.loads(res)
    print(dicts['translateResult'][0][0]['tgt'])

if __name__ == "__main__":
    kw = input("请输入你要翻译的内容:")
    times = int(time.time() *1000)
    data = {
        "ts":1571219669873,
        "salt":times,
        "version":"2.1",
        "to":"AUTO",
        "from":"AUTO",
        "smartresult":"dict",
        "bv":"e218a051a7336600dfed880d272c7d6f",
        "sign":"e6d7646f447c8bcdf8b80b5b193112c6",
        "keyfrom":"fanyi.web",
        "client":"fanyideskweb",
        "action":"FY_BY_CLICKBUTTION",
        "doctype":"json",
        "i":kw
    }
    youdaoAPI(data)
