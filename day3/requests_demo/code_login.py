import requests
from chaojiying import Chaojiying_Client
import random
ua_list = [
    "User-Agent,Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1",
    "User-Agent,Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0",
    "User-Agent,Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
]
ua_list = random.choice(ua_list)

headers = {
    'User-Agent':ua_list
}

#登录方法
def do_login(code):
    url = "http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=20199410460"
    data = {
        'icode':code,
        "f": "http%3A%2F%2Fwww.renren.com%2F541197383%2Fprofile",
        "rkey": "00de0309607d2424dc154f5b5f5a9f6d",
        "key_id": "1",
        "password": "833df4914709457db7c002d1351b6ac18d3a22485c4247ff8d11ff3985af615b",
        "email": "gaohj5@163.com",
        "origURL": "http://www.renren.com/home",
        "domain": "renren.com",
        "captcha_type": "web_login"
    }

    #发送post请求
    response = session.post(url,headers=headers,data=data)
    #获取结果
    result = response.content.decode()
    print(result)

#获取验证码
def get_code():
    #图形验证码接口
    url = "http://icode.renren.com/getcode.do?t=web_login&amp;rnd=%s" % (random.random())
    #发送请求
    res = session.get(url,headers=headers)
    #保存图片
    with open('code.jpg','wb') as fp:
        fp.write(res.content)
        fp.flush()
    chaojiying = Chaojiying_Client('gaohj5', '12qwaszx', '900304')
    im = open('code.jpg', 'rb').read()
    result = chaojiying.PostPic(im, 1902)['pic_str']
    print(result)
    return result


#访问个人中心
def get_profile():
    url = 'http://www.renren.com/541197383/profile'
    #打印结果
    response = session.get(url, headers=headers)
    # 获取结果
    result = response.content.decode()
    print(result)


if __name__ == "__main__":
    session = requests.session() #用来保存cookie
    code = get_code()
    do_login(code)
    get_profile()