# _*_ coding:utf-8 _*_
import requests
import re
# 下载一个网页
url = 'http://www.guoxuedashi.com/a/1443c/'
# 模拟浏览器发送http请求
response = requests.get(url)
# 编码方式
response.encoding = 'utf-8'
# 网页源码
html = response.text
# 小说的名字
title = re.findall(r'<meta name="Keywords" content="(.*?)">', html)[0]
# 新建一个文件，保存小说内容
# with open('%s.txt' % title) as f:
fb = open('%s.txt' % title, 'w', encoding='utf-8')
# 获取每一章信息（章节，url）
dl = re.findall(r'<dl>.*?</dl>', html, re.S)[0]
chapter_info_list = re.findall(r'<a href="(.*?)" target="_blank">(.*?)</a>', dl)
# 循环每一个章节，分别去下载
for chapter_info in chapter_info_list:
    # chapter_title = chapter_info[1]
    # chapter_url = chapter_info[0]
    chapter_url, chapter_title = chapter_info
    chapter_url = "http://www.guoxuedashi.com%s" % chapter_url
    # 下载章节内容
    chapter_response = requests.get(chapter_url)
    chapter_response.encoding = 'utf-8'
    chapter_html = chapter_response.text

    # 提取，章节内容
    chapter_content = re.findall(r'<!-- 219.143.205.28 -->(.*?)<div class="info_cate clearfix">', chapter_html, re.S)[0]
    # 清洗数据
    chapter_content = chapter_content.replace('	', '')
    chapter_content = chapter_content.replace(' ', '')
    chapter_content = chapter_content.replace('<br/>', '')
    chapter_content = chapter_content.replace('</div>', '')
    chapter_content = chapter_content.replace('<div>', '')
    chapter_content = chapter_content.replace('&nbsp;', '')

    # 持久化
    fb.write(chapter_title)
    fb.write('\n\n')
    fb.write(chapter_content)

    print(chapter_title)
