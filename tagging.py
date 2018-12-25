#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : tagging.py
# @Author: wangzhy
# @Date  : 2018/11/7 15:52
# @Desc  : 输入 带有标点的文本 去标点 然后 使用二元模型 添加断句
# 			计算准确率和召回率 F1值
#

import time
import datetime
import string
import json
from langconv import *

# 标记 a i h x 的汉字的 频率 字典
dic_a_p = {}
dic_i_p = {}
dic_h_p = {}
dic_x_p = {}

# 所有的汉字mark  频率集合 字典
dic_hant_mark_p = {}

# 二元标记 频率 字典
dic_bigram_p = {}
# 三元标记 频率 字典
dic_trigram_p = {}
# 二元 三元标记 整合到一起的 频率 字典
dic_bi_tri_gram_p = {}

# 准确率的 list
p_percision_list = []
# 召回率的 list
p_recall_list = []
# F值
f1_measure_list = []

# 四种标记的list
four_mark_list = ['h', 'a', 'i', 'x']

data_biaodian_right = ''	# 标点正确的文本
data_two_mark_right = ''	# 将正确的标点转换为a,其余为x
data_duanju_right = ''	# 断句正确的文本

data_mark = ''	# 利用Ngram生成的 带有4种标记的文本
data_biaodian = ''	# 将data_mark 里的标记转换成标点 文本

dir = "D:\\FilesUsers\\古文本自动句读\\测试集_有标点\\"	# 测试集路径 101个文件
files = ['与山巨源绝交书,嵇康.txt', '与袁石浦,陶望龄.txt', '中华古今注,马缟.txt','中华民国史事日志,郭廷以.txt', '中国官场学,汪龙庄、万枫江.txt', '中山诗话,刘攽.txt', '中庸章句,子思.txt', '中庸章句集注,朱熹.txt', '中说,王通.txt', '云中事记,(明)苏祐.txt', '云中纪变,(明) 孙允中 .txt', '仪礼,佚名.txt', '仪礼注疏,郑玄.txt', '众家编年体晋史,汤球.txt', '优古堂诗话,吴开.txt', '佐治药言,汪辉祖.txt', '作字示儿孙,傅山.txt', '元人小令选,.txt', '元代野史,(民国)田腾蛟.txt', '元史,(明)宋濂.txt', '元朝秘史,佚名.txt', '元诗别裁集,张景星.txt', '先唐文,严可均辑.txt', '先秦汉魏晋南北朝诗,逯钦立.txt', '养兰说,陶望龄.txt', '友古词,蔡伸.txt', '叙陈正甫会心集,袁宏道.txt', '吴礼部诗话,吴师道.txt', '周书,(唐)令狐德棻.txt', '周子全书,周敦颐.txt', '周易,佚名.txt', '周易参同契,魏伯阳.txt', '周易正义,孔颖达.txt', '周易注,王弼.txt', '周易略例,王弼.txt', '周易郑康成注,王应麟.txt', '周易集解,李鼎祚.txt', '周礼,周公旦.txt', '周礼注疏,贾公彦.txt', '周髀算经,佚名.txt', '子夏易传,卜子夏.txt', '孝经,孔丘.txt', '孝经注疏,李隆基.txt', '小山词,晏几道.txt', '小石潭记,柳宗元.txt', '庄子,庄周.txt', '庄子集解,王先谦.txt', '庄子集释,郭庆藩.txt', '庄氏史案,佚名.txt', '张可九元曲集,张可九.txt', '张文襄公事略,(清)佚名.txt', '彦周诗话,许顗.txt', '徐霞客游记,徐弘祖.txt', '忠经,(汉)马融.txt', '愚公移山,列子.txt', '战国策,刘向.txt', '拙轩词话,张侃.txt', '新本郑氏周易,恵栋.txt', '无住词,陈与义.txt', '无名氏28首,无名氏.txt', '易传,.txt', '易童子问,欧阳修.txt', '昭明文选,萧统.txt', '智囊全集,冯梦龙.txt', '朱子治家格言,朱柏庐.txt', '朱子语类,朱熹.txt', '杂说,李贽.txt', '浙东纪略,徐芳烈.txt', '溪堂词,谢逸.txt', '煮泉小品,田艺蘅.txt', '玉台新咏,徐陵.txt', '珠玉词,晏殊.txt', '真山民集,真桂芳.txt', '知稼翁词,黄公度.txt', '知言,胡宏.txt', '竹书纪年,.txt', '竹屋痴语,高观国.txt', '竹斋诗余,黄机.txt', '竹斋集,王冕.txt', '粤游见闻,瞿共美.txt', '粤词雅,潘飞声.txt', '紫微诗话,吕本中.txt', '续诗品,袁枚.txt', '艺苑卮言,王世贞.txt', '薛涛、李冶诗集,薛涛 李冶.txt', '薛涛诗全集,薛涛.txt', '西厢记,王实甫.txt', '西湖梦寻,张岱.txt', '谢朓全集,谢朓.txt', '谢灵运诗全集,谢灵运.txt', '資治通鑑,(北宋)司馬光主編.txt', '贞观政要,吴兢.txt', '越绝书,袁康.txt', '輶轩使者绝代语释别国方言,杨雄.txt', '逸老堂诗话,俞弁.txt', '醉翁亭记,欧阳修.txt', '长生殿,洪昇.txt', '长门赋,司马相如.txt', '闲情赋并序,陶渊明.txt', '饮水词,纳兰性德.txt', '麈史,王得臣.txt']
files = ['与山巨源绝交书,嵇康.txt', '与袁石浦,陶望龄.txt', '中华古今注,马缟.txt']
files = ['与山巨源绝交书,嵇康.txt', '与袁石浦,陶望龄.txt']
files = ['醉翁亭记,欧阳修.txt']


# 将简体中文 转换为 繁体中文
def chsIntoCht(data):
	# 将输入转为 繁体中文
	data = Converter('zh-hant').convert(data)
	data.encode('utf-8')
	return data


# 读取本地 频率字典 函数
def updateBiDict():

	# 声明字典是全局变量，而不是局部变量
	global dic_bigram_p
	global dic_trigram_p
	global dic_bi_tri_gram_p
	global dic_hant_mark_p
	global dic_a_p
	global dic_x_p
	global dic_h_p
	global dic_i_p

	# 读入本地字典
	f1 = open('D:\\FilesUsers\\古文本自动句读\\汉字标记集\\pro_bigram.txt', 'r', encoding='utf-8')
	dic_bigram_p = json.load(f1)	# 二元模型标记 概率
	f1.close()
	f1 = open('D:\\FilesUsers\\古文本自动句读\\汉字标记集\\pro_trigram.txt', 'r', encoding='utf-8')
	dic_trigram_p = json.load(f1)  # 三元模型标记 概率
	f1.close()
	f1 = open('D:\\FilesUsers\\古文本自动句读\\汉字标记集\\pro_hant_a.txt', 'r', encoding='utf-8')
	dic_a_p = json.load(f1)
	f1.close()
	f1 = open('D:\\FilesUsers\\古文本自动句读\\汉字标记集\\pro_hant_i.txt', 'r', encoding='utf-8')
	dic_i_p = json.load(f1)
	f1.close()
	f1 = open('D:\\FilesUsers\\古文本自动句读\\汉字标记集\\pro_hant_h.txt', 'r', encoding='utf-8')
	dic_h_p = json.load(f1)
	f1.close()
	f1 = open('D:\\FilesUsers\\古文本自动句读\\汉字标记集\\pro_hant_x.txt', 'r', encoding='utf-8')
	dic_x_p = json.load(f1)
	f1.close()


	# 将所有标记的汉字频率字典 集合到一起
	dic_hant_mark_p.update(dic_a_p)
	dic_hant_mark_p.update(dic_i_p)
	dic_hant_mark_p.update(dic_h_p)
	dic_hant_mark_p.update(dic_x_p)
	# print('“汉字mark”频率的 总个数：', len(dic_hant_mark_p))

	# 将 二元 三元模型标记 整合到一起
	dic_bi_tri_gram_p.update(dic_bigram_p)
	dic_bi_tri_gram_p.update(dic_trigram_p)
	# print('二元三元概率字典：', dic_bi_tri_gram_p)

	# 对频率字典进行平滑处理
	dic_bigram_p['other'] = 0.0003
	dic_hant_mark_p['other'] = 0.0003
	# 将'xa'加入频率字典
	# dic_bigram_p['xa'] = 0.3
	# dic_bigram_p['ah'] = 0.0
	# dic_bigram_p['ii'] = 0.0
	# dic_bigram_p['hh'] = 0.0
	# dic_bigram_p['ax'] = 0.0
	# dic_bigram_p['xi'] = 0.0
	# dic_bigram_p['hx'] = 0.0
	# dic_bigram_p['hi'] = 0.0

	# 所有的汉字mark  频率集合 字典  按照汉字 升序排序
	dic_hant_mark_p = dict(sorted(dic_hant_mark_p.items(), key=lambda x: x[0]))
	# 二元组 频率字典 升序排序
	dic_bigram_p = dict(sorted(dic_bigram_p.items(), key=lambda x: x[0]))


	# print(dic_bigram_p)

	# 输出频率字典
	'''
	print('dic_bigram_p', dic_bigram_p)
	print("dic_a_p:", sorted(dic_a_p.items(), key=lambda x: x[1], reverse=True)[:100])
	print("dic_i_p:", sorted(dic_i_p.items(), key=lambda x: x[1], reverse=True)[:100])
	print("dic_h_p:", sorted(dic_h_p.items(), key=lambda x: x[1], reverse=True)[:100])
	print("dic_x_p:", sorted(dic_x_p.items(), key=lambda x: x[1], reverse=True)[:100])
	print("dic_hant_mark_p:", sorted(dic_hant_mark_p.items(), key=lambda x: x[0])[1310:2500])
	# '''

	return 0


# 打开文件，并按行读文件，去掉换行和空格，变为一行字符串，并返回
def readlinesFile(file):  # file是文件名

	global dir  # 声明全局变量 文件路径 dir
	# 打开一个文件f     rU 要求文件必须存在 且 按行进行分割
	f = open(dir + file, 'r', encoding='utf-8')

	# data1 为去掉换行后的文章内容；
	data1 = ''
	# 按行读取文件 并进行操作，将标点转换为a
	try:
		for line in f:
			# do_somthing_with(line) // line带"\n"
			# data1 为去掉换行后的文章内容
			data1 += line.strip()
	finally:
		f.close()

	return data1


# 将标点转换为 标记a, 其余标记x ，并返回
def twoMark(line):

	# 新定义一个字符串 保存转换标点为a后的字符串
	str = ''
	# data2 为转换标点为a后的文章，多个str连接
	data2 = ''

	# 对每一行的每个字符c 进行判断 将标点转换为a
	for c in line:

		# 英文
		if c in string.ascii_letters:
			continue
		# 数字
		elif c.isdigit():
			str += c
		# 空格
		elif c.isspace():
			continue
		# 中文
		elif c.isalpha():
			str += c
		# 特殊字符
		else:
			str += 'a'
	# data2 为转换标点为a后的文章，多个str连接
	data2 += str

	# 对data2 进行操作，去掉连续重复 a，在其余字后面加上 x，步骤为：（写一个汉字和前面的标记，默认最后一个是标记a)
	data3 = ''  # 存储加入x和去掉连续重复a的字符串；
	# 遍历data2 里面的每个字符，去掉连续重复 a，并在其余字后面加上 x
	for c in data2:
		# 如果不是a，即 c 是 字
		if c != 'a':
			if len(data3) == 0:  # 如果是第一个字  直接输入到data3
				data3 += c
			elif data3[-1] == 'a':  # 不是第一个字符，即data3 里已有字符，且最后一个字符是 a
				data3 += c
			else:  # data3 里已有字符，且最后一个字符是不是 a
				data3 += 'x'
				data3 += c
		# 如果是a
		else:
			if len(data3) == 0:  # 如果文章开头是a  则去掉a
				continue
			else:
				# 去掉连续重复的a 只留一个
				if data3[-1] != 'a':  # 汉字后 第一个a
					data3 += c  # 写入a

	return data3


# 去掉标记函数，输入为带有标记的字符串，返回无标记字符串
def removeMark(data):
	data4 = ''
	for i in range(0, len(data),2):
		data4 += data[i]

	return data4


# 显示进度函数 ，当检测文本时，输出检测进度百分比以及当时的时间
def schedule(i,lenth):
	if i == 0:	# 显示开始时间
		print(' 检测进度： 0', '%  时间：', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))  # 获取当前时间
		return 0
	for num_temp in range(100,0,-1):	# 第三个参数表示的是100所有进行的操作，每次加上-1，直到0
		if i >= (lenth - 1) * num_temp / 100:
			if num_temp == 100:	# 最后 有换行符
				print('\r 检测进度：100', '% 时间：', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') )  # 获取当前时间
			else:	# end=''为不换行，'\r'表示回车（将光标移动到行首而不换行）
				print('\r 检测进度：%d' % num_temp, '%  时间：', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), end='')  # 获取当前时间
			num_temp += 1
			return 0

	return 0


# 利用二元模型(局部最优） 给文本加标记，返回data_mark ，输入没有标点的 繁体 文本data
def bigramTaggingLocalBest(data):
	# 用来存放与输入data对应的 最大概率的标记字符串
	mark = ''

	print(' 需要加标点的字符个数：',len(data))	# 输出文本的字符个数
	# 遍历输入字符串的 每一个字 根据Viterbi公式，算出后面概率最大的 标记，存入mark中
	for i in range(len(data)):

		if len(data) > 300:	# 当需要加标点的字符个数 大于 300 时，显示检测进度
			# 检测进度显示，显示开始时间，和最新的 1% ，直到100%
			schedule(i,len(data))

		# 对于每个汉字 data[i] 找到它后面概率最大的标记
		mark_temp1 = ''  # 存放 一个汉字后 概率最大的标记
		pr_temp1 = 0.0  # 存放 一个汉字后的标记 最大概率
		pr1 = 0.0  # 第一种 总概率1

		# 第一种 先根据汉字 计算其后概率最大的 标记，再 计算相应二元组的概率，二者相乘计算总概率1
		for value, key in dic_hant_mark_p.items():  # 遍历 “汉字mark”  频率字典dic_hant_mark_p，
			if value[0] <= data[i]:
				if value[0] == data[i] and pr_temp1 < key:  # 根据汉字 找到其后面 最大概率的 标记，以及最大的概率
					mark_temp1 = value[1]
					pr_temp1 = key
			else:
				break
		# 在计算相应二元组概率，进而计算总概率1
		if mark == '':  # 如果是首个汉字，不需要计算二元组，
			pr1 = pr_temp1  # 总概率1
		else:  # 根据二元模型 的相应概率，计算总概率1
			bigram_temp = mark[-1] + mark_temp1  # 对应的 二元组
			if bigram_temp not in dic_bigram_p:
				pr1 = pr_temp1 * dic_bigram_p['other']  # 总概率1
			else:
				pr1 = pr_temp1 * dic_bigram_p[bigram_temp]  # 总概率1

		# 初始化变量
		mark_temp2 = ''  # 存放 一个标记后 概率最大的标记
		pr_temp2 = 0.0  # 存放 一个标记后的标记的 最大概率
		pr2 = 0.0  # 第二种 总概率2
		# 第二种 先计算二元组 概率最大的标记，再计算汉字生成 该标记概率，二者相乘计算总概率2
		if mark != '':
			for value, key in dic_bigram_p.items():  # 遍历 二元组 概率字典
				if value[0] <= mark[-1]:
					if value[0] == mark[-1] and pr_temp2 <= key:  # 根据前一个标记和二元模型，找到该标记后最大概率的标记
						mark_temp2 = value[1]
						pr_temp2 = key
				else:
					break
			hant_mark_temp = data[i] + mark_temp2  # 再根据 汉字和该标记的概率，计算总概率2
			if hant_mark_temp not in dic_hant_mark_p:
				pr2 = pr_temp2 * dic_hant_mark_p['other']
			else:
				pr2 = pr_temp2 * dic_hant_mark_p[hant_mark_temp]  # 总概率2

		# 比较 两种 的总概率1和2，概率大的那个为 所求标记，将标记存入mark中
		if pr1 > pr2:
			mark += mark_temp1
		else:
			mark += mark_temp2

	# print(mark)
	# print(data)

	# 将汉字data 和 标记mark_data 两个string交叉合并起来
	data_mark = [''] * len(data) * 2
	data_mark[::2] = data
	data_mark[1::2] = mark
	data_mark = ''.join(data_mark)

	return data_mark


# 利用二元模型(采用 基础 for循环） 给文本加标记，返回data_mark ，输入没有标点的 繁体 文本data
def trigramTaggingBase(data):

	mark = ''	# 概率最大的标记字符串，mark 为 概率最大的mark_temp
	data_mark_temp = ''	# 中间过程的 每个标记字符串
	data_mark_temp_p = 0	# mark_temp 对应的概率

	# 遍历data 中每一个 字data[i]
	for i in range(0,len(data)):

		data_mark_temp += data[i]	# 将

		# 每一个字后 遍历4种标记
		for mark_one in four_mark_list:


			data_mark_temp += mark_one


	return 0


# 利用三元模型 给文本加标记，返回data_mark，输入没有标点的 繁体 文本data
def trigramTagging(data):


	return 0


# 将标记转化为断句
def markIntoDuanju(data_mark):
	data_biaodian = data_mark
	data_biaodian = data_biaodian.replace('x', '')
	data_biaodian = data_biaodian.replace('h', '')
	data_biaodian = data_biaodian.replace('i', '')
	data_biaodian = data_biaodian.replace('a', '/')
	return data_biaodian


# 统计字符串中 标记a 的下标
def aMarkLocation(data):
	list_a_location = []
	for i in range(len(data)):
		if data[i] == 'a':
			list_a_location.append(i)

	return list_a_location


# 计算准确率 ，
def calculatePrecision(list_a_location_ngram):
	num_temp = 0.0
	for i in list_a_location_ngram:
		if data_two_mark_right[i] == 'a':
			num_temp += 1

	p_percision = num_temp / len(list_a_location_ngram)
	return p_percision


# 计算召回率
def calculateRecall(list_a_location_right):
	num_temp = 0.0
	for i in list_a_location_right:
		if data_mark[i] == 'a':
			num_temp += 1

	p_recall = num_temp / len(list_a_location_right)
	return p_recall


# 计算F值
def calculateF1(p, r):

	return 2 * p * r / (p + r)


# 求list 值的 平均值
def avgList(list):
	sum =0
	for item in list:
		sum += item
	return sum/len(list)


# 测试过程，计算 准确率、召回率、F1值
def testP_R_F():
	global data_biaodian_right  # 标点正确的文本
	global data_two_mark_right   # 将正确的标点转换为a,其余为x
	global data_duanju_right   # 断句正确的文本
	global data_mark   # 利用Ngram生成的 带有4种标记的文本
	global data_biaodian   # 将data_mark 里的标记转换成标点 文本

	file_num = 0  # 计数器，计算文件个数
	# 遍历 测试集 文件，调用函数，读取文件，并加标记 a x
	for file in files:
		file_num += 1  # 计数器，计算文件个数
		print(file_num, file)
		data_biaodian_right = readlinesFile(file)	# 调用函数，读取文件，去掉文件里的换行和空格，
		# print('正确的标点文本：', data_biaodian_right)

		data_two_mark_right = twoMark(data_biaodian_right)  # 调用函数，将标点转换为标记 a x
		# print("转换为两种标记：", data_two_mark_right)

		# 正确的 断句文本
		data_duanju_right = markIntoDuanju(data_two_mark_right)
		# print('正确的断句文本：', data_duanju_right)

		# 没有标点的文本data
		data = removeMark(data_two_mark_right)
		# print('没有标点的文本：', data)

		# 使用二元模型(局部最优) 生成标记
		data_mark = bigramTaggingLocalBest(data)
		# print('二元生成的标记：', data_mark)

		# 将标记转变为 断句
		data_duanju = markIntoDuanju(data_mark)
		# print('二元的断句文本：', data_duanju)	# 输出断句后的文本

		# 正确的标记a 的下标
		list_a_location_right = aMarkLocation(data_two_mark_right)
		# print(list_a_location_right)

		# 二元生成的标记 a 的下标
		list_a_location_bigram = aMarkLocation(data_mark)
		# print(list_a_location_bigram)

		# 调用函数 计算准确率
		p_percision_list.append(calculatePrecision(list_a_location_bigram))
		print('准确率：', p_percision_list[-1])

		# 调用函数 计算召回率
		p_recall_list.append(calculateRecall(list_a_location_right))
		print('召回率：', p_recall_list[-1])

		# 调用函数 计算F值
		f1_measure_list.append(calculateF1(p_percision_list[-1], p_recall_list[-1]))
		print('F值：', f1_measure_list[-1])

		# 计算准确率 召回率 F值 的平均值
		p_percision_avg = avgList(p_percision_list)  # 准确率 平均值
		p_recall_avg = avgList(p_recall_list)  # 召回率 平均值
		f1_measure_avg = avgList(f1_measure_list)  # F值 平均值
		print('准确率 平均值:', p_percision_avg)
		print('召回率 平均值:', p_recall_avg)
		print('F值 平均值:', f1_measure_avg)

	return 0



if __name__ == '__main__':
	# 调用函数，读入本地字典
	updateBiDict()
	# 调用测试函数，计算准确率、召回率、F1值
	# testP_R_F()

	# 输入需要加标点的文本
	data = '子曰学而时习之不亦说乎有朋自远方来不亦乐乎人不知而不愠不亦君子乎曾子曰吾日三省吾身为人谋而不忠乎与朋友交而不信乎传不习乎'
	data = '子曰学而时习之不亦说乎有朋自远方来不亦乐乎'
	data = chsIntoCht(data)	# 转为繁体

	data_mark = bigramTagging(data)	# 使用二元模型 生成标记
	# print('二元生成的标记：', data_mark)
	data_duanju = markIntoDuanju(data_mark)	# 将标记转变为 断句
	print('二元的断句文本：', data_duanju)	# 输出断句后的文本
