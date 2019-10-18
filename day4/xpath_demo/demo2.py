from lxml import etree

#1.获取所有的tr标签
#2.获取第二个tr标签
#3 获取所有class为even的标签
#4.获取所有a标签的  href属性
#5.获取所有的职位信息 纯文本
parser = etree.HTMLParser(encoding='utf-8')  #解析为html文档  编码为utf-8
html = etree.parse("tencent.html",parser=parser)

#1
# trs = html.xpath("//tr")
# # print(type(trs)) #xpath返回的是一个列表
# for tr in trs:
#     print(etree.tostring(tr,encoding='utf-8').decode('utf-8'))

#2
# tr = html.xpath("//tr[2]")[0]
# print(etree.tostring(tr,encoding='utf-8').decode('utf-8'))

#3.获取所有class 为even 的标签

# trs = html.xpath("//tr[@class='even']")
# for tr in trs:
#     print(etree.tostring(tr,encoding='utf-8').decode('utf-8'))

# 4获取所有a标签的 href属性
# aList = html.xpath("//a/@href")
# for a in aList:
#     print("http://hr.tencent.com/"+a)

#5 获取所有的职位信息  纯文本

trs = html.xpath("//tr[position()>1]")
positions = []
for tr in trs:
   href = tr.xpath(".//a/@href")[0]
   fullurl = "http://hr.tencent.com/"+href
   title = tr.xpath("./td[1]//text()")[0]
   category = tr.xpath("./td[2]//text()")[0]
   nums = tr.xpath("./td[3]//text()")[0]
   address = tr.xpath("./td[4]//text()")[0]
   pubtime = tr.xpath("./td[5]//text()")[0]

   position = {
       'fullurl':fullurl,
       'title':title,
       'category':category,
       'nums':nums,
       'address':address,
       'pubtime':pubtime
   }
   positions.append(position)
print(positions)