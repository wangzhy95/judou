from langconv import *
import sys

# print(sys.version)
# print(sys.version_info)

# 转换繁体到简体
def cht_to_chs(line):
    line = Converter('zh-hans').convert(line)
    line.encode('utf-8')
    return line

# 转换简体到繁体
def chs_to_cht(line):
    line = Converter('zh-hant').convert(line)
    line.encode('utf-8')
    return line


line_chs='<>123asdasd把中文字符串进行繁体和简体中文的转换'
line_cht='<>123asdasd把中文字符串進行繁體和簡體中文的轉換'

ret_chs = "%s\n" %cht_to_chs(line_cht)
ret_cht = "%s\n" %chs_to_cht(line_chs)

print("chs=", ret_chs)
print("cht=",ret_cht)

# file = open('ret.txt','w',encoding='utf-8')
# file.write(ret_chs)
# file.write(ret_cht)
# file.close()

# 读文件
# f = open('E:\\Study朝\\研一\\1013\\spider\\四库全书\\集部\\与山巨源绝交书,嵇康.txt','r',encoding='utf-8')
# te = f.read()
# te = chs_to_cht(te)

chs = '子曰：“学而时习之，不亦说乎。”'
ch = '皇后问题后来被改编成了一款游戏'
chs = chs_to_cht(ch)

print(chs)