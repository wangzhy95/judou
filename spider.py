#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : spider.py
# @Author: wangzhy
# @Date  : 2018/10/3116:57
# @Desc  : 
#
import requests
import re
from langconv import *

'''

# 下载一个网页
url = 'http://www.zggdwx.com/heguanzi.html'
# 模拟浏览器发送http请求
response = requests.get(url)
# 编码方式
response.encoding = 'utf-8'
# 网页源码
html = response.text
# print(html)
# 小说的名字
# title = re.findall(r'<meta name="Keywords" content="(.*?)">', html)[0]
title = '鹖冠子'
# 新建一个文件，保存小说内容
# with open('%s.txt' % title) as f:
fb = open('D:\\pythonProject\\清洗数据时\\鹖冠子,陆佃.txt', 'w', encoding='utf-8')

fb.write(title + '。' + '\n')
# 获取每一章信息（章节，url）
dl = re.findall(r'</legend><div>.*?<label>书评', html, re.S)[0]
chapter_info_list = re.findall(r'<a href="(.*?)" target="_blank">(.*?)</a>', dl)
# print(chapter_info_list)
# 循环每一个章节，分别去下载
for chapter_info in chapter_info_list:

	chapter_url, chapter_title = chapter_info
	# 下载章节内容
	chapter_response = requests.get(chapter_url)
	chapter_response.encoding = 'utf-8'
	chapter_html = chapter_response.text
	# 提取，章节内容
	chapter_content = re.findall(r'<div class="content"><p>(.*?)</p></div></div><!-- 中国古典文学顶部书籍内容页底部 -->', chapter_html, re.S)[0]
	# print(chapter_content)
	# 清洗数据
	chapter_content = chapter_content.replace('	', '')
	chapter_content = chapter_content.replace(' ', '')
	chapter_content = chapter_content.replace('<br/>', '')
	chapter_content = chapter_content.replace('</div>', '')
	chapter_content = chapter_content.replace('<div>', '')
	chapter_content = chapter_content.replace('<p>', '')
	chapter_content = chapter_content.replace('</p>', '')
	chapter_content = chapter_content.replace('</a>', '')
	chapter_content = chapter_content.replace('&nbsp;', '')

	# 简体转换为繁体
	chapter_content = Converter('zh-hant').convert(chapter_content)
	chapter_content.encode('utf-8')


	# 持久化
	fb.write(chapter_title)
	fb.write('。')
	fb.write('\n')
	fb.write(chapter_content)
	fb.write('\n')

	print(chapter_title)

'''

title = '尹文子,尹喜.txt'

f1 = open('D:\\pythonProject\\清洗数据时\\%s' % title, 'r', encoding='utf-8')
data = f1.read()

data = Converter('zh-hant').convert(data)
data.encode('utf-8')
f1.close()

f1 = open('D:\\pythonProject\\清洗数据时\\%s' % title, 'w', encoding='utf-8')
f1.write(data)
print(title + '**简转繁完成**')



string1 = '全吴嘉会古风流。渭南往岁忆来游。西子方来、越相功成去，千里沧江一叶舟。至今无限盈盈者，尽来拾翠芳洲。最是簇簇寒村，遥认南朝路、晚烟收。三两人家古渡头。'

string1 = Converter('zh-hant').convert(string1)
string1.encode('utf-8')
print(string1)

# '''