#encoding:utf-8


import urllib.request
import urllib.parse
from http.cookiejar import CookieJar,FileCookieJar,MozillaCookieJar,LWPCookieJar

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
}


#urllib.request.urlopen()
#用来保存cookie
def get_opener():
    #创建cookiejar对象
    cookiejar = CookieJar()
    #创建一个httpCookieProfessor对象 用来处理cookiejar对象
    handler = urllib.request.HTTPCookieProcessor(cookiejar)
    #创建一个打开器
    opener = urllib.request.build_opener(handler)
    return opener


def login_renren(opener):
    login_url = 'http://www.renren.com/PLogin.do'
    data = {
        'email':'gaohj5@163.com',
        'password':'12qwaszx'
    }

    req = urllib.request.Request(login_url,data=urllib.parse.urlencode(data).encode('utf-8'),headers=headers)
    res = opener.open(req)

    print(res.read().decode('utf-8'))
def visit_profile(opener):
    my_url = 'http://www.renren.com/541197383/profile'
    req = urllib.request.Request(my_url,headers=headers)
    res = opener.open(req)

    with open('renren2.html','w',encoding='utf-8') as fp:
        fp.write(res.read().decode('utf-8'))


if __name__ == "__main__":
    #创建一个打开器 对象
    opener = get_opener()
    #登录人人
    login_renren(opener)
    #访问个人中心
    visit_profile(opener)