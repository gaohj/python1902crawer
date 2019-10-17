from bs4 import BeautifulSoup
import requests
import re
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
}

url = "https://search.51job.com/list/180200,000000,0000,00,9,99,python,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="


response = requests.get(url=url,headers=headers)
html = response.content.decode('gbk')


bs = BeautifulSoup(html,'lxml')

jobnum_str = bs.select(".rt")[0].text
print(jobnum_str)


num_re = r'.*?(\d+).*'
num = re.findall(num_re,jobnum_str,re.S)
print(num)

print(int(num[0]))