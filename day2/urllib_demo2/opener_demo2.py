import urllib.request

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
    "Cookie":"anonymid=juagdpiney0yg3; _r01_=1; jebe_key=af15eb55-de2a-49f2-8861-fe6e628d49ed%7C67510b08b897c5e3b50e55d3a235a53c%7C1554854833372%7C1%7C1554854833452; _de=28A69782AB906D4A677B8FA35C706602; depovince=HUB; jebecookies=c29d8dfa-8729-481b-a3cc-8741a46a2d84|||||; JSESSIONID=abc-gOwP1NftxeBYHms3w; ick_login=3d32f9c0-c46f-400f-81f2-1fae7ee3c3e6; p=b8c67d511787e5e21828a6d3812fb7a93; ap=541197383; first_login_flag=1; ln_uact=gaohj5@163.com; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=f3cd54d81fe356806ed7f2f9e59b86c33; societyguester=f3cd54d81fe356806ed7f2f9e59b86c33; id=541197383; xnsid=2dcdbbae; ver=7.0; loginfrom=null; wp_fold=0; jebe_key=af15eb55-de2a-49f2-8861-fe6e628d49ed%7C67510b08b897c5e3b50e55d3a235a53c%7C1571189581023%7C1%7C1571189584369"
}

#构建一个HttpHandler 处理器对象   用来处理http请求

handler = urllib.request.HTTPHandler() #http请求
#handler = urllib.request.HTTPSHandler() #https请求

#创建一个支持http请求的opener对象
opener = urllib.request.build_opener(handler)


#将打开器对象设置为全局打开器
urllib.request.install_opener(opener)
#后期如果你是用urlopen()
#构建request 请求

# req = urllib.request.Request("http://www.baidu.com",headers=headers)
#
# #原来是  urllib.request.urlopen(req)
#
# res = opener.open(req)
#
# print(res.read().decode('utf-8'))

res = urllib.request.urlopen("http://www.ifeng.com/")
print(res.read().decode('utf-8'))

