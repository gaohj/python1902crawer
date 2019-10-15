import urllib.request
import re

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134"
}


url = "https://search.51job.com/list/180200,000000,0000,00,9,99,python,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="

request = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(request)

html = response.read().decode('gbk')
# print(html)


#写正则 提取数据
jobnum_re = r'<div class="rt">(.*?)</div>'

jobnum_compile = re.compile(jobnum_re,re.S)#生成一个规则模式
#re.S 将.的遍及全局   包括\n

# jobnum = jobnum_compile.findall(html) #列表
jobnum = jobnum_compile.findall(html)[0] #列表
print(jobnum)  #共1503条职位

#提取数字

num_re = r'.*?(\d+).*?'
num = re.findall(num_re,jobnum)
print(num)
print(num[0])

res_str = r'<div class="el">(.*?)</div>'
joblist = re.findall(res_str,html,re.S)
# print(joblist[0])

for job in joblist:
    res_str2 = r'onmousedown="">(.*?)</a>'
    try:
        joblist2 = re.findall(res_str2, job, re.S)
        print(joblist2[0].strip())
    except:
        pass

