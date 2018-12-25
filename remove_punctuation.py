#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : remove_punctuation.py
# @Author: wangzhy
# @Date  : 2018/11/1515:01
# @Desc  : 去掉文本标点
#

import string

# 去掉line里的标点
def removeBiaodian(line):

    # 存储去掉标点后的文本
    text = ''

    # 对line的每个字符c 进行判断 去掉标点
    for c in line:
        # 文章总字符数count_all
        count_all =1

        # 英文
        if c in string.ascii_letters:
            # count_en += 1
            count_all += 1

        # 数字
        elif c.isdigit():
            # count_dg += 1
            count_all += 1
            text += c
        # 空格
        elif c.isspace():
            # count_sp += 1
            count_all += 1
        # 中文
        elif c.isalpha():
            # count_zh += 1
            count_all += 1
            text += c
        # 特殊字符
        # else:
            # if count_all == 1:
            #     count_all -= 1
            #     continue
            # count_pu += 1
    return text

if __name__ == '__main__':

    count_all = count_en = count_dg = count_sp = count_zh = count_pu = 0

    file = '闲情赋并序,陶渊明.txt'
    # 打开一个文件f     rU 要求文件必须存在 且 按行进行分割
    f = open('D:\\FilesUsers\\古文本自动句读\\测试集_有标点\\%s' % file, 'r', encoding='utf-8')

    # 输入文本 有标点
    text_input = input('请输入代标点的文本：')

    string_output = removeBiaodian(text_input)

    print('去掉标点后文本：' + string_output)