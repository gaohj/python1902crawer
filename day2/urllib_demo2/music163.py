
import urllib.request
import urllib.parse
import json
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
}

#post接口
url = "https://music.163.com/weapi/v1/resource/comments/A_PL_0_2783240?csrf_token="

data = {
    "params":"JKDq4LtELoh0m6USC17tdjp/BdF7vswdDOMZs7F+LHW3GOVspWTYYszzBIKCdEcWn2Q2eG1UHmhbYVwrSNwrGg4ljF2MvPTnpXDHRdvHw2nu1bt/uYCa1gEhMGQENYuBUwfYG/lLSYROzcPgyoIeGgfz0ioUviVXJPehwweNGsk8Awo5KLnpXvYfsAbjtrZB0yRWtFluWojJpHIoDquyClYfaSRLEb1WL4vNAPuA8BI=",
    "encSecKey":"bb8a4561f8d79aca80d57b8f9d21576dfb866548feadf33a8f4c4bb884f18cc2e8b0d7fe81d18bdd565024b56e2e546ea75246c90bf6305c06fc1617fce4bfba10b7ef39e2fd50aacdad303ea615aff20af49c11a6a382d33516536b790a74dc4a02ff76178ea548a435cbe8c81b39e88cea9afb4b18aa57293d4cfc56c503f5",
}

data = urllib.parse.urlencode(data).encode()
#str -> bytes  encode
#bytes -> str  decode

req = urllib.request.Request(url=url,headers=headers,data=data)
response = urllib.request.urlopen(req)

content = response.read().decode()

data_dict = json.loads(content)

hotComments = data_dict['hotComments']

for hotComment in  hotComments:
    nickname = hotComment['user']['nickname']
    content = hotComment['content']

    print(nickname,":",content)

