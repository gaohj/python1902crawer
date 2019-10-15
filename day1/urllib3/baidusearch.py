import urllib.request
import urllib.parse
def baiduAPI(params):
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134"
    }

    url = "https://www.baidu.com/s?" +params
    # 创建请求对象
    req = urllib.request.Request(url=url, headers=headers)

    # 发送请求 获取返回值  urlopen函数
    response = urllib.request.urlopen(req)
    return response.read().decode('utf-8')

if __name__ == "__main__":
    kw = input("请输入要查找的关键词:")
    wd = {"wd":kw}
    params = urllib.parse.urlencode(wd)

    print(baiduAPI(params))
