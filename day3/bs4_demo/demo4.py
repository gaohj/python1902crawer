

# from bs4.element import Tag
# from bs4.element import NavigableString
# from bs4.element import Comment
from bs4 import BeautifulSoup
import re
html = """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>bs4 demo</title>
</head>
<body>
    <p class="title">
        Test
        <b>我走过最多的路就是你的套路</b>
    </p>
    <p class="contents">
        <div>asdf</div><a href="#" class="box1" id="link1">1111111</a>
        <a href="#" class="box2"  id="link2">222222</a>
        <a href="#" class="box3"  id="link3">333333</a>
        
    </p>
    <p class="test">test</p>
    <p>
        <div id='sib'></div>
    </p>
</body>
</html>
<p><!--我是注释--></p>
"""

bs = BeautifulSoup(html,'lxml')
#tag
# print(bs.head)
# print(bs.head.title)
# print(bs.head.name)

# 属性
# print(bs.p.attrs)
# print(bs.a.attrs['href'])
# print(bs.a.attrs.get('class'))

#文本
# print(bs.p.b.string)
# print(bs.p.text) #Test
#         我走过最多的路就是你的套路
# print(bs.p.get_text())
#Test
#我走过最多的路就是你的套路

#兄弟节点
#同级的上一个 和下一个
# print(bs.a.next_sibling)#空格换行也是一个节点
# print(bs.a.next_sibling.next_sibling) #下一个的下一个
# print(bs.a.previous_sibling)#


#
# print(bs.find('p')) #返回第一个
# print(bs.find_all('p')) #列表

# print(bs.find_all(re.compile('^p$')))
comment = bs.p.contents
print(comment)