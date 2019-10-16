import json
import urllib.request
import urllib.parse

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
}

url = "https://job.alibaba.com/zhaopin/socialPositionList/doList.json"

for i in range(1,10):
    params = {
        'pageSize':'100',
        't':'0.24960111584863864',
        'keyWord':'python'
    }

data = urllib.parse.urlencode(params).encode()
req = urllib.request.Request(url,headers=headers,data=data)
resp = urllib.request.urlopen(req)
content = resp.read().decode()
print(content)


data_dict = json.loads(content)
job_list = data_dict['returnValue']['datas']

for job in job_list:
    degree = job.get('degree')
    departmentName = job.get('departmentName')
    description = job.get('description')
    firstCategory = job.get('firstCategory')
    workExperience = job.get('workExperience')

    with open('ali.txt','a+',encoding='utf-8') as fp:
        fp.write(str((degree,departmentName,description,firstCategory,workExperience))+"\n")
        fp.flush() #不按回车键也往里写数据