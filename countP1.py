#!/usr/bin/env python   # 在Linux环境中标注运行路径
# -*- coding: utf-8 -*-
# @File  : countP1.py
# @Author: wangzhy
# @Date  : 2018年10月25日
# @Desc  : 生成“汉字mark”频数字典
#           计算各个标记个数
#           生成 “汉字mark”频率 字典
#           𝑃(曰│a) = (𝑃(曰a))/(𝑃(a)) = (c(曰a))/(𝑐(a))


import math
import operator
import json

global NULL
NULL=''

# 标记集合
marks = ['a', 'i', 'h', 'x']

# 标记 a i h x 总数
count_a = count_i = count_h = count_x = 0

# 标记为a i h x 的"汉字mark" 的频数 字典
dic_a = {}
dic_i = {}
dic_h = {}
dic_x = {}

# 标记 a i h x 的汉字的 频率 字典
dic_a_p = {}
dic_i_p = {}
dic_h_p = {}
dic_x_p = {}



# 分词并统计词频，构建频数字典，统计各个标记个数
def dictionary(sentence, lists):

    global count_a, count_h, count_i, count_x # count_a 默认生成新的局部变量，如果想指代全局变量，需要在语句前加 global

    # 将sentence 字符每两个一组，输入到 list 里面
    for i in range(0, len(sentence), 2):    # 输出0到len()之间的偶数，不包括len()，即每两个输出一个

        # 将sentence 每两个一组 存入lists
        lists.append(sentence[i:i+2])    # sentence[i:i+2] 区间为左开右闭

    # 统计词频，如果词在字典word_dir{}中出现过则+1，未出现则=1
    for word in lists:  # word 形式为 '汉字mark', 比如 '字a'
        if word[-1] == 'a':  # 如果标记为 a

            count_a += 1
            dict = dic_a
            dict_p = dic_a_p
        else:
            if word[-1] == 'i':  # 如果标记为 i
                count_i += 1
                dict = dic_i
                dict_p = dic_i_p
            else:
                if word[-1] == 'h':  # 如果标记为 h
                    count_h += 1
                    dict = dic_h
                    dict_p = dic_h_p
                else:
                    if word[-1] == 'x':  # 如果标记为 x
                        count_x += 1
                        dict = dic_x
                        dict_p = dic_x_p
        if word not in dict:
            dict[word] = 1
        else:
            dict[word] += 1
    return lists

# 生成频率字典
def dictionaryProbability(lists):

    for word in lists:
        if word[-1] == 'a':  # 如果标记为 a
            count_each = count_a
            dict = dic_a
            dict_p = dic_a_p
        else:
            if word[-1] == 'i':  # 如果标记为 i
                count_each = count_i
                dict = dic_i
                dict_p = dic_i_p
            else:
                if word[-1] == 'h':  # 如果标记为 h
                    count_each = count_h
                    dict = dic_h
                    dict_p = dic_h_p
                else:
                    if word[-1] == 'x':  # 如果标记为 x
                        count_each = count_x
                        dict = dic_x
                        dict_p = dic_x_p
        if word not in dict:
            dict_p[word] = float(1)/float(count_each)   # 数据平滑处理：加1法
        else:
            dict_p[word] = (float(dict[word]) + 1)/float(count_each)


if __name__ == "__main__":

    # 797个文件
    files = ['七修类稿,郎锳.txt', '万历野获编,(明)沈德符.txt', '三十六计,佚名.txt', '三命通会,万民英.txt', '三国志 裴松之注,(晋)陈寿编(南朝宋)裴松之注.txt', '三国杂事,(宋)唐庚.txt', '三国遗事,僧一然.txt', '三朝北盟会编,徐梦莘.txt', '三略,黄石公.txt', '三辅黄图,佚名.txt', '不真空论,僧肇.txt', '与梁武帝论书启,陶弘景.txt', '世说新语,刘义庆.txt', '东京梦华录,孟元老.txt', '东南纪事,邵廷采.txt', '东坡志林,苏轼.txt', '东坡易传,苏东坡.txt', '东坡词,苏轼.txt', '东坡诗话,苏东坡.txt', '东堂词,毛滂.txt', '东浦词,韩玉.txt', '东观奏记,裴庭裕.txt', '东观汉记校注,刘珍等(东汉) 吴树平校注.txt', '两同书,罗隐.txt', '临川先生文集,王安石.txt', '临池管见,周星莲.txt', '临池诀,卢携.txt', '丹阳词,葛胜仲.txt', '乐府古题要解,吴兢.txt', '乐府指迷,沈义父.txt', '乐府杂录,段安节.txt', '乐府诗集,郭茂倩.txt', '乐章集,柳永.txt', '乙酉扬州城守纪略,.txt', '九势,蔡邕.txt', '九家旧晋书辑本,汤球辑(清) 杨朝明校补.txt', '九州春秋,西晋·司马彪.txt', '九歌,屈原.txt', '九章算术,张苍.txt', '书后品,李嗣真.txt', '书品[节录],庾肩吾.txt', '书学,钱泳.txt', '书学捷要[节录],朱履贞.txt', '书断,张怀瓘.txt', '书断列传,张怀瓘.txt', '书旨述,虞世南.txt', '书法散论,傅山.txt', '书法约言,宋曹.txt', '书法论,沈尹默.txt', '书法辑要,文伯子.txt', '书法雅言,项穆.txt', '书湖州庄氏史狱,翁广平.txt', '书目答问,张之洞.txt', '书筏,笪重光.txt', '书论,.txt', '书论,欧阳询.txt', '书诀,丰坊.txt', '书述,李煜.txt', '乾坤大略,王余佑.txt', '了凡四训,袁了凡.txt', '二十四孝,郭居敬.txt', '二十四诗品,司空图.txt', '二字诀,李华.txt', '二老堂诗话,周必大.txt', '云笈七签,张君房.txt', '五代史阙文,王禹偁.txt', '五代新说,徐炫.txt', '五代春秋,(宋)尹洙.txt', '五十六种书并序,韦续.txt', '五国故事,佚名.txt', '五杂俎,谢肇淛.txt', '五灯会元,释普济.txt', '亢仓子,庚桑楚.txt', '人物志,刘邵.txt', '人间词话,王国维.txt', '仇池笔记,苏轼.txt', '今本竹书纪年疏证,王国维.txt', '从政录,薛瑄.txt', '传习录,王守仁.txt', '伤寒论,张仲景.txt', '何博士备论,何去非.txt', '佛国记,法显.txt', '佛祖通载,释念常.txt', '佛说四十二章经,.txt', '侨吴集,郑元祐.txt', '借竹楼记,徐渭.txt', '倩女离魂,郑光祖.txt', '傅青主女科,傅山.txt', '僧宝传,释惠洪.txt', '全三国文,严可均辑.txt', '全上古三代文,严可均辑.txt', '全元曲,.txt', '全北齐文,严可均辑.txt', '全后周文,严可均辑.txt', '全后汉文,严可均辑.txt', '全后魏文,严可均辑.txt', '全唐五代词,.txt', '全唐文,董诰.txt', '全唐诗,.txt', '全宋文,严可均辑.txt', '全宋词,唐圭璋.txt', '全晋文,严可均辑.txt', '全梁文,严可均辑.txt', '全汉文,严可均辑.txt', '全汉诗,丁绍仪.txt', '全秦文,严可均辑.txt', '全陈文,严可均辑.txt', '全隋文,严可均辑.txt', '全齐文,严可均辑.txt', '八家后汉书辑注,周天游辑注.txt', '公孙龙子,公孙龙.txt', '六一词,欧阳修.txt', '六一诗话,欧阳修.txt', '六书缘起,孙光祖.txt', '六体书论,张怀瓘.txt', '六朝文絜,许梿.txt', '六祖大师法宝坛经,法海.txt', '六韬(注释本),姜子牙.txt', '六韬,姜尚.txt', '兰亭集序,王羲之.txt', '关尹子,尹喜.txt', '兵制,黄宗羲.txt', '典论,曹丕.txt', '兼明书,丘光庭.txt', '农学古籍概览,.txt', '冷斋夜话,释惠洪.txt', '分甘馀话,王士禛.txt', '列仙传,刘向.txt', '列女传,刘向.txt', '列子,列御寇.txt', '列子集释,杨伯峻.txt', '刘壮肃公奏议,刘铭传.txt', '刘子,刘昼.txt', '刘桢诗全集,刘桢.txt', '前出师表,诸葛亮.txt', '前汉纪,(东汉)荀悦.txt', '前赤壁赋,苏轼.txt', '劉氏菊譜,劉蒙.txt', '勤有堂随录,陈栎.txt', '包待制智勘后庭花,郑廷玉.txt', '包待制智赚生金阁,武汉臣.txt', '包龙图智赚合同文字,.txt', '化书,谭峭.txt', '北史,(唐)李延寿.txt', '北山酒经,朱翼中.txt', '北户录,段公路.txt', '北溪字义,陈淳.txt', '北碑南帖论[节录],阮元.txt', '北苑別錄,趙汝礪(北宋).txt', '北苑别录,赵汝砺.txt', '北齐书,(唐)李百药.txt', '医学源流论,徐大椿.txt', '医方集解,汪昂.txt', '十七史百将传,张预.txt', '十八家诗抄,曾国藩.txt', '十六国春秋别本,(北魏)崔鸿.txt', '十六湯品,蘇廙(唐).txt', '十叶野闻,(民国)许指严 .txt', '千家诗,谢枋得.txt', '千金翼方,孙思邈.txt', '升庵诗话,杨慎.txt', '华阳国志校补图注,常璩(晋) 任乃强校注.txt', '南北书派论[节录],阮元.txt', '南北朝杂记,(宋)刘敞.txt', '南史,(唐)李延寿.txt', '南岳小录,李冲昭.txt', '南征录汇,(金)李天民.txt', '南明野史,(清)南沙三餘氏.txt', '南濠诗话,都穆.txt', '南询录,邓豁渠.txt', '南越笔记,李调元.txt', '南迁录,(金)张师颜 .txt', '南齐书,(梁)萧子显.txt', '博物志,(晋)张华.txt', '历代兵制,陈傅良.txt', '历代崇道记,杜光庭.txt', '厚黑学,李宗吾.txt', '双江聂先生文集,聂豹.txt', '古今书评,袁昂.txt', '古今刀剑录,陶宏景.txt', '古尊宿语录,僧赜藏.txt', '古文观止,吴楚材.txt', '古方八阵,张景岳(明).txt', '古本竹书纪年辑证,.txt', '古画品录,谢赫.txt', '古籍版本知识,.txt', '古籍目录及其功用,.txt', '古诗十九首,.txt', '古诗源,沈德潜.txt', '古谣谚,杜文澜.txt', '台湾通史,连横.txt', '史記,(漢)司馬遷著.txt', '史通,刘知几.txt', '司马法,司马穰苴.txt', '吊古战场文,李华.txt', '名贤集,佚名.txt', '后出师表,诸葛亮.txt', '后山诗话,陈师道.txt', '后汉书 李贤注,(南朝宋)范烨编(唐)李贤等注.txt', '后汉书,范烨编.txt', '后汉纪校注,袁宏(晉) 周天游校注.txt', '吕氏春秋,吕不韦.txt', '听秋声馆词话,丁绍仪.txt', '吴地记,陆广微.txt', '吴子,吴起.txt', '吴船录,范成大.txt', '吴越春秋,赵晔.txt', '呻吟语摘,吕坤.txt', '和清真词,方千里.txt', '唐人咏茶诗,.txt', '唐会要,王溥.txt', '唐六典,李林甫.txt', '唐国史补,唐·李肇.txt', '唐子西文录,强幼安.txt', '唐宋名家词选,龙榆生.txt', '唐律疏议,长孙无忌.txt', '唐才子传,辛文房.txt', '唐文拾遗,陆心源.txt', '唐文续拾,陆心源.txt', '唐李问对,阮逸.txt', '唐诗三百首,蘅塘退士选编.txt', '商君书,商鞅.txt', '四书章句集注,朱熹.txt', '四体书势,卫恒.txt', '四库全书总目提要,永瑢.txt', '四溟诗话,谢榛.txt', '围炉夜话,王永彬.txt', '国语,左丘明.txt', '国闻备乘,胡思敬.txt', '国雅品,顾起纶.txt', '图画见闻志,郭若虚.txt', '圣求词,吕渭老.txt', '坦菴词,赵师使.txt', '墨子,墨翟.txt', '墨子城守各篇简注,岑仲勉.txt', '墨子白话今译,.txt', '墨子闲诂,孙诒让.txt', '声律启蒙,李渔.txt', '备急千金要方,孙思邈.txt', '复雅歌词,鲖阳居士.txt', '夏商野史,(明)钟惺 .txt', '外交小史,(清)佚名.txt', '夜航船,张岱.txt', '大业拾遗记,颜师古.txt', '大同纪事,明·韩邦奇.txt', '大唐创业起居注,温大雅.txt', '大唐新语,唐·刘肃.txt', '大唐西域记,释玄奘.txt', '大学章句,孔子.txt', '大学章句集注,朱熹.txt', '大宋宣和遗事,宋·佚名.txt', '大戴礼记,戴德.txt', '大观茶论,赵佶.txt', '大金吊伐录,(金)佚名.txt', '天工开物,宋应星.txt', '天朝田亩制度,洪秀全.txt', '天玉经,杨筠松.txt', '太上感应篇,(宋)李昌龄.txt', '太平天国战记,(清)罗惇曧.txt', '太平经合校,于吉.txt', '太玄经,杨雄.txt', '太白阴经,李筌.txt', '奇经八脉考,李时珍.txt', '奉天录,赵元一.txt', '奴书订,祝允明.txt', '奴才小史,(民国)老吏.txt', '姑溪词,李之仪.txt', '姜夔词选,姜夔.txt', '姜斋诗话,王夫之.txt', '娇红记,孟称舜.txt', '婉约词,惠淇源.txt', '孔丛子,孔鲋.txt', '孔子家语,王肃.txt', '孔雀东南飞,.txt', '孙子兵法,孙武.txt', '孙子略解,曹操.txt', '孙子算经,佚名.txt', '孙膑兵法,孙膑.txt', '孙过庭书谱及其释文,孙过庭.txt', '孟子,孟轲.txt', '孟子字义疏证,戴东原.txt', '孟子注疏,赵岐.txt', '孟子集注,朱熹.txt', '孟郊集,孟郊.txt', '学治臆说,汪辉祖.txt', '宅经,.txt', '守城录,陈规.txt', '安陆集,张先.txt', '宋书,(梁)沈约.txt', '宋史,脫脫等.txt', '宋朝事实,(宋)李攸.txt', '宋袁阳源集,袁阳源.txt', '宋论,王夫之.txt', '宋词三百首,朱祖谋.txt', '宋诗一百首,王水照 朱刚注译.txt', '宋高僧传,赞宁.txt', '官箴,吕本中.txt', '审斋词,王千秋.txt', '宣和北苑貢茶錄,熊蕃(宋).txt', '宣和北苑贡茶录,熊蕃.txt', '家范 (全译评点本),司马光.txt', '容斋续笔,洪迈.txt', '容斋随笔,洪迈.txt', '寒山子诗集,.txt', '寒花葬志,归有光.txt', '寓简,沈作喆.txt', '寺塔记,段成式.txt', '封氏闻见记,封演.txt', '将苑,诸葛亮.txt', '尉繚子,尉缭.txt', '小儿语,吕得胜.txt', '小学诗,谢泰阶.txt', '尔雅,佚名.txt', '尔雅注疏,郭璞.txt', '尚书,孔丘.txt', '尚书大传,伏胜.txt', '尚书正义,孔安国.txt', '尹文子,尹喜.txt', '居易录,王士禛.txt', '山房随笔,蒋正子.txt', '山谷词,黄庭坚.txt', '岁华纪丽谱,费著.txt', '岑参诗选,岑参.txt', '岑参集,岑参.txt', '岕茶汇抄,冒襄.txt', '岛夷志略,汪大渊.txt', '岭外代答,周去非.txt', '岭表录异,刘恂.txt', '崇文总目,王尧臣.txt', '崔护诗选,崔护.txt', '崔颢诗全集,崔颢.txt', '嵇康诗全集,嵇康.txt', '己亥杂诗,龚自珍.txt', '师说,韩愈.txt', '帛书《黃帝四经》,.txt', '帝范,李世民.txt', '幕学举要,万维鶾.txt', '平宋录,刘敏中.txt', '平斋词,洪咨夔.txt', '平水韵部,《诗韵合壁》.txt', '广弘明集,道宣.txt', '广艺舟双楫,康有为.txt', '庐山记,陈舜俞.txt', '庚溪诗话,陈岩肖.txt', '康雍乾间文字之狱,清·佚名 .txt', '廿二史札记,赵翼.txt', '开元释教录,智升.txt', '弘明集,释侩佑.txt', '张子正蒙,张载.txt', '归去来辞,陶渊明.txt', '归愚词,葛立方.txt', '归田诗话,瞿佑.txt', '归田赋,张衡.txt', '律条公案,陈玉秀.txt', '心经,真德秀.txt', '忍经,(元)吴亮.txt', '思旧赋并序,向秀.txt', '慎子,慎到.txt', '扬子法言,汉·扬雄  晋·李轨 注.txt', '扬州十日记,王秀楚.txt', '扬州画舫录,李斗.txt', '承晋斋积闻录,梁巘.txt', '投笔肤谈,西湖逸士.txt', '折狱龟鉴,郑克.txt', '抱朴子内篇,葛洪.txt', '抱朴子外篇,葛洪.txt', '拾遗记,(前秦)王嘉.txt', '授笔要说,韩方明.txt', '握奇经,公孙宏.txt', '撼龙经,杨筠松.txt', '散论,于右任.txt', '敦煌变文集新书,.txt', '敬斋古今黈,李冶.txt', '文(历代诸家),.txt', '文史通义,章学诚.txt', '文子,辛銒.txt', '文心雕龙,刘勰.txt', '文心雕龙考异,張立齋.txt', '文心雕龙译注,陆侃如\u3000牟世金.txt', '文忠集,范景文.txt', '文献通考,马端临.txt', '文笔要诀,杜正伦.txt', '文选,萧统.txt', '断肠词,朱淑真.txt', '新书,贾谊.txt', '新五代史,(北宋)欧阳修.txt', '新元史,柯劭忞.txt', '新唐书,(北宋)欧阳修.txt', '新序,刘向.txt', '新語(简繁对照),陆贾.txt', '新论,桓谭.txt', '新语,陆贾.txt', '无能子,无能子.txt', '无量寿经,(三国魏)康僧铠译.txt', '日知录,顾炎武.txt', '日闻录,李翀.txt', '旧五代史,(北宋)薛居正.txt', '旧唐书,(后晋)刘昫.txt', '时贤本事曲子集,杨绘.txt', '明儒学案,黄宗羲.txt', '明史,(清)张廷玉.txt', '明圣二湖,张岱.txt', '明太祖宝训,.txt', '明夷待访录,黄宗羲.txt', '明季三朝野史,顾炎武.txt', '明季北略,计六奇.txt', '明季南略,计六奇.txt', '明皇杂录,唐·郑处诲.txt', '春秋公羊传,公羊高.txt', '春秋公羊传注疏,何休.txt', '春秋左传,左丘明.txt', '春秋左传正义,杜预.txt', '春秋穀梁传注疏,范宁.txt', '春秋繁露,董仲舒.txt', '春秋谷梁传,榖梁俶.txt', '春秋谷梁传注疏,范甯、杨士勋.txt', '春雨杂述,解缙.txt', '晋书,(唐)房玄龄等.txt', '晋后略,荀绰.txt', '晋孙子荆集,孙楚.txt', '晋王右军集,王羲之.txt', '晋荀公曾集,荀勖.txt', '晏子春秋,.txt', '景岳全书,张介宾.txt', '曹丕诗全集,曹丕.txt', '曹操诗全集,曹操.txt', '曹操诗集,曹操.txt', '曹组词集,曹组.txt', '曾国藩家书,曾国藩.txt', '曾国藩文集,曾国藩著 王澧华编.txt', '月波洞中记,郑樵.txt', '朝野佥载,唐·张鷟.txt', '木天禁语,范德机.txt', '本草纲目,李时珍.txt', '李义山诗集,李商隐.txt', '李商隐诗选,李商隐.txt', '李斯谏逐客书,李斯.txt', '李煜词全集,李煜.txt', '李白诗全集,李白.txt', '李贺诗全集,李贺.txt', '杜审言诗全集,杜审言.txt', '杜工部草堂诗话,蔡梦弼.txt', '杜甫诗全集,杜甫.txt', '松漠纪闻,洪皓.txt', '板桥杂记,余怀.txt', '林和靖集,林逋.txt', '林泉高致集,郭思.txt', '林纾作品集,林纾.txt', '林间录,释惠洪.txt', '枢垣记略,梁章钜.txt', '柳永词全集,柳永.txt', '栾城集,苏辙.txt', '桂林风土记,莫休符.txt', '桃花扇,孔尚任.txt', '桃花源记,陶渊明.txt', '桔中秘叙,.txt', '梁书,(唐)姚思廉.txt', '梁山伯与祝英台,.txt', '梅溪词,史达祖.txt', '梅磵诗话,韦居安.txt', '梅花谱,.txt', '梦溪笔谈,沈括.txt', '梦粱录,吴自牧.txt', '棋经,张拟.txt', '棋经十三篇,张拟.txt', '棋经论,.txt', '棠阴比事,桂万荣.txt', '楚辞,刘向.txt', '楚辞章句疏证,王逸.txt', '楚辞补註,洪兴祖.txt', '樵隐词,毛幵.txt', '橘录,韩彦直.txt', '武侯八阵兵法辑略,汪宗沂.txt', '武林旧事,周密.txt', '武经总要,曾公亮.txt', '毛詩,.txt', '民国野史,(民国)荫余轩放.txt', '水经注,郦道元.txt', '永历实录,王夫之.txt', '氾胜之书,氾胜之.txt', '汉书,班固.txt', '汉官六种,孙星衍.txt', '汉宫秋,马致远.txt', '汉魏南北朝墓志汇编,.txt', '江南野史,龙衮 陈尚君补遗.txt', '江阴城守纪,(清)韩菼编.txt', '池北偶谈,王士禛.txt', '沧浪诗话,严羽.txt', '法书要录-六卷全,张彦远.txt', '法书论,萧衍.txt', '法书论,蔡希综.txt', '法苑珠林,道世.txt', '法言义疏,杨雄.txt', '泰泉乡礼,黄佐.txt', '洗冤集录,宋慈.txt', '洛神赋,曹植.txt', '洛阳伽蓝记,杨衒之.txt', '洛阳牡丹记,欧阳修.txt', '浩然斋词话,周密.txt', '海岳名言,米芾.txt', '海野词,曾觌.txt', '淮南子,刘安.txt', '淮海詞,秦觀.txt', '深衣考误,江永.txt', '淳熙三山志,梁克家.txt', '清人原著——书法秘诀,.txt', '清代名人轶事,葛虚存.txt', '清代野记,(清)梁溪坐观老人.txt', '清代野记,梁溪坐观老人.txt', '清史稿,赵尔巽.txt', '清宫禁二年记,(清)裕德菱.txt', '清忠谱,李玉.txt', '清暑笔谈,(明)陆树声 .txt', '清朝前纪,(民国)孟森.txt', '清稗琐缀,佚名.txt', '清诗别裁集,沈德潜.txt', '温公续诗话,司马光.txt', '温热论,叶桂.txt', '湘军志,(清)王闿运.txt', '湘山野录,(宋)文莹.txt', '满清入关暴政,韩菼.txt', '满清兴亡史,(民国)汉史氏 .txt', '满清外史,(清)天嘏 .txt', '漱玉词,李清照.txt', '潜夫论笺校正,王符.txt', '濒湖脉学,李时珍.txt', '灵城精义,何溥.txt', '灵枢,.txt', '熙朝新语,(清)徐锡龄、钱泳.txt', '爱日斋丛抄,叶釐.txt', '爱莲说,周敦颐.txt', '片玉词,周邦彦.txt', '牡丹亭,汤显祖.txt', '物不迁论,僧肇.txt', '献帝春秋,(东汉)佚名 .txt', '王心斋全集,王艮.txt', '王文成全书,王守仁.txt', '王粲诗全集,王粲.txt', '王维诗集,王维.txt', '用笔法,钟瑶.txt', '甲申朝事小纪,王朝.txt', '申子,申不害.txt', '申鉴,荀悦.txt', '画禅室随笔,董其昌.txt', '画继,邓椿.txt', '留东外史,不肖生.txt', '留东外史续集,不肖生.txt', '痧胀玉衡,郭士遂.txt', '登楼赋,王粲.txt', '白居易诗全集,白居易.txt', '白朴集,白朴.txt', '白石道人歌曲,姜夔.txt', '白石道人诗说,姜夔.txt', '白虎通义,班固.txt', '白香词谱,舒梦兰.txt', '百战奇略,刘基.txt', '皇明奇事述,明·王世贞.txt', '皇明异典述,明·王世贞.txt', '皇明本纪,(明)佚名 .txt', '皇明盛事述,明·王世贞.txt', '皇明纪略,(明)皇甫录.txt', '益州名画录,黄休复.txt', '盐铁论,桓宽.txt', '石林词,叶梦得.txt', '石林诗话,叶梦得.txt', '碧岩录,释圆悟.txt', '礼记,戴德.txt', '礼记正义,郑玄.txt', '神仙传,葛洪.txt', '神农本草经,佚名.txt', '神异经,东方朔.txt', '离骚,屈原.txt', '禽经,张华.txt', '禾谱,曾安止.txt', '秋兴赋并序,潘岳.txt', '秦朝野史,(民国)黄士衡.txt', '稼轩词,辛弃疾.txt', '穆天子传,.txt', '窦娥冤,关汉卿.txt', '童心说,李贽.txt', '笑林广记,游戏主人.txt', '笔意赞,王僧虔.txt', '笔阵图,卫铄.txt', '笔髓论,虞世南.txt', '答万季埜诗问,冯班.txt', '筠豀乐府,李弥逊.txt', '算学启蒙总括,朱世杰.txt', '管子,管仲.txt', '管子轻重篇新诠,马非百.txt', '箧中集,元结.txt', '类证治裁,林佩琴.txt', '精忠旗,冯梦龙.txt', '素书,黄石公.txt', '素问,.txt', '纳兰家族墓碑,.txt', '练兵实纪,戚继光.txt', '续书断,朱长文.txt', '续书谱,姜夔.txt', '续佐治药言,汪辉祖.txt', '续资治通鉴,(清)毕沅.txt', '续资治通鉴长编,(宋)李焘.txt', '续资治通鉴长编拾补,(清)黄以周等辑.txt', '缉古算经,王孝通.txt', '罗昭谏集,罗隐.txt', '罗湖野录,晓莹.txt', '翠微先生北征录,华岳.txt', '翠微北征录,华岳.txt', '翰墨志,赵构.txt', '翰林要诀,陈绎曾.txt', '老子想尔注,张陵.txt', '老子道德经校释,老子.txt', '老子集注,落花散人.txt', '老学庵笔记,陆游.txt', '脉经,王叔和.txt', '脉象口诀歌,佚名.txt', '艺概[节录],刘熙载.txt', '艺舟双辑（附《十七帖》疏证）,包世臣.txt', '芦川词,张元干.txt', '苏武李陵诗,苏武.txt', '苏洵集,苏洵.txt', '苏轼词选（４８首),苏轼.txt', '苕溪渔隐丛话前集,胡仔.txt', '苕溪渔隐丛话后集,胡仔.txt', '英雄记,王粲.txt', '范德机诗集,范梈.txt', '范成大词集,范成大.txt', '茶录,蔡襄.txt', '茶疏,许次纾.txt', '茶神傳,艸衣.txt', '茶经,陆羽.txt', '茶賦  幷書,寒齋.txt', '茶錄,蔡襄(北宋).txt', '荀子,荀况.txt', '荆楚岁时记,宗懔.txt', '草书势(含今译),崔瑗.txt', '草书势,索靖.txt', '药性赋,佚名.txt', '菜根谭,洪应明.txt', '营造法式,李诫.txt', '葬书,郭璞.txt', '蒲江词,卢祖皋.txt', '藏海诗话,吴可.txt', '藤王阁序,王勃.txt', '虎钤经,许洞.txt', '蛮书,樊绰.txt', '蜀乱述闻,祝介.txt', '蜀王本纪,(明)郑朴 辑.txt', '血證論,.txt', '衍极并注,郑杓.txt', '袁氏世范,袁采.txt', '褚氏遗书,褚澄.txt', '西使记,刘郁.txt', '西夏书事,(清)吴广成.txt', '西夏事略,(宋)王称.txt', '西巡回銮始末,(清)佚名.txt', '西征随笔,汪景祺.txt', '西汉野史,(民国)黄士衡.txt', '西铭,张载.txt', '观林诗话,吴聿.txt', '解人颐,钱德苍.txt', '言兵事疏,晁错.txt', '言行龟鉴,张光祖.txt', '训蒙骈句,司守谦.txt', '论书,王僧虔.txt', '论书,苏轼.txt', '论书,蔡襄.txt', '论书,释亚栖.txt', '论书,黄庭坚.txt', '论书表,江式.txt', '论书表,虞龢.txt', '论法书,董其昌.txt', '论用笔十法,张怀瓘.txt', '论衡,王充.txt', '论语,孔丘.txt', '论语注疏,何晏.txt', '论语集注,朱熹.txt', '评书,祝允明.txt', '评书药石论（含今译）,张怀瓘.txt', '词曲(历代诸家),.txt', '词格律,唐宋词格律.txt', '词论,李清照.txt', '词韵简编,龙榆生.txt', '试笔,欧阳修.txt', '诗 (历代诸家),.txt', '诗人主客图,张为.txt', '诗人玉屑,魏庆之.txt', '诗品,钟嵘.txt', '诗学源流考,鲁九皋.txt', '诗学禁脔,范德机.txt', '诗式,皎然.txt', '诗法家数,杨载.txt', '诗经,.txt', '诗谱,陈绎曾.txt', '诗镜总论,陆时雍.txt', '诚斋诗话,杨万里.txt', '诫子篇,诸葛亮.txt', '说文解字,许慎.txt', '说苑,刘向.txt', '读书分年日程,程端礼.txt', '读史方舆纪要,顾祖禹.txt', '读孟尝君传,王安石.txt', '读通鉴论,王夫之.txt', '谐铎,沈起凤.txt', '象棋十诀,.txt', '象棋指归,贾题韬.txt', '负暄野录,陈槱.txt', '赌棋山庄词话,谢章铤.txt', '辽史,(元)脫脫.txt', '辽志,(宋)叶隆礼.txt', '过江七事,陈贞慧.txt', '近思录,吕祖谦.txt', '述张长史笔法十二意,颜真卿.txt', '送董生邵南序,韩愈.txt', '送高闲上人序,韩愈.txt', '逃禅词,杨无咎.txt', '通典,杜佑.txt', '通玄真经,辛銒.txt', '逸周书,孔晁.txt', '道德经（老子）,老子.txt', '邓子,邓析.txt', '邓析子,.txt', '郡斋读书志,晁公武.txt', '郭店楚墓竹简,.txt', '郴江百咏,阮阅.txt', '都城纪胜,灌圃耐得翁.txt', '酒德颂,刘伶.txt', '酒经,(宋)朱肱.txt', '酒边词,向子諲.txt', '采古来能书人名,羊欣.txt', '释名,刘熙.txt', '释怀素与颜真卿论草书,陆羽.txt', '释氏稽古略,觉岸.txt', '野记,(明)祝允明 .txt', '金人铭,.txt', '金刚经集注,(明)朱棣主编.txt', '金匮要略,张机.txt', '金史,(元)脫脫.txt', '金楼子,萧绎.txt', '鉴略妥注,李廷机.txt', '针邪密要,佚名.txt', '钝吟书要[节录],冯班.txt', '钝吟杂录,冯班.txt', '铁崖乐府,杨维桢.txt', '铜人针灸经,佚名.txt', '长短经,(唐)赵蕤.txt', '长短经（反经）,赵蕤.txt', '阮籍诗全集,阮籍.txt', '阳羡茗壶系,周高起.txt', '陆氏易解,姚士粦.txt', '陆游诗全集,陆游.txt', '陆贾新语注释,江津 王利器.txt', '陈书,(唐)姚思廉.txt', '陈子昂诗集,陈子昂.txt', '陈情表,李密.txt', '陈琳诗全集,陈琳.txt', '陶庵梦忆,张岱.txt', '陶渊明诗全集,陶渊明.txt', '陶渊明集,陶潜.txt', '隋书,(唐)魏徵.txt', '隋唐嘉话,唐·刘餗.txt', '隋唐野史,(明)罗贯中.txt', '随园食单,袁枚.txt', '隶书体,成公绥.txt', '难经,杨玄操.txt', '雷峰塔,方成培.txt', '青囊奥语,杨筠松.txt', '靖康传信录,李纲.txt', '靖康纪闻,宋 丁特起.txt', '非草书,赵壹.txt', '韩诗外传,韩婴.txt', '韩非子,韩非.txt', '顺宗实录,韩愈.txt', '颅囟经,卫汛.txt', '题卫夫人笔阵图后,王羲之.txt', '题跋176则,苏轼.txt', '颜氏家训,颜之推.txt', '颜氏家训集解,王利器.txt', '风俗通义校注,应劭.txt', '风骚旨格,齐己.txt', '高洁说,李贽.txt', '鬼谷子,王诩.txt', '鬼谷子本经阴符七术,鬼谷子.txt', '鬼门十三针,佚名.txt', '魏书,(北齐)魏收.txt', '魏晋世语,.txt', '魏郑公谏录,王方庆.txt', '鲍明远集,鲍照.txt', '鸦片事略,(清)李圭.txt', '鹖冠子,陆佃.txt', '鹤林玉露,罗大经.txt', '麓堂诗话,李东阳.txt', '黄帝内经,.txt', '黄帝阴符经,黄帝.txt', '齐东野语,周密.txt', '齐民要术,贾思勰.txt', '龙川别志,苏辙.txt', '龙洲词,刘过.txt']
    # files = ['东坡词,苏轼.txt', '爱莲说,周敦颐.txt', '全唐文,董诰.txt']
    # files = ['爱莲说,周敦颐.txt', '东坡词,苏轼.txt']

    # num 为计数器
    num = 0

    # 循环files 里的 每个文件file
    for file in files:
        num += 1  # 每检索一个文件,计数器加一
        print(num, file)

        # 读取每个文件，存入 data_file
        f1 = open('D:\\pythonProject\\训练集_四种标记\\%s' % file, 'r', encoding='utf-8')
        data_file = f1.read()
        f1.close()
        # print(data_file) # 输出字符串


        # 将string 每两个一组 存为 list
        data_list = []
        # 调用 dictionary函数，生成频数字典，统计各个标记个数
        data_list = dictionary(data_file, data_list)
        # print(data_list)

        # 调用函数，生成频率字典
        dictionaryProbability(data_list)

        print(file + '**检索完成**')

    # 输出各个标记的个数
    print("标记a的总个数count_a:", count_a)
    print("标记i的总个数count_i:", count_i)
    print("标记h的总个数count_h:", count_h)
    print("标记x的总个数count_x:", count_x)


    # 将各个标记的个数写入txt文件
    ''' 将各个标记的个数写入txt文件
    f2 = open('D:\\pythonProject\\汉字标记集\\各个标记的总个数.txt', 'w', encoding='utf-8')
    f2.write("标记a的总个数count_a:" + str(count_a) + '\n')
    f2.write("标记i的总个数count_i:" + str(count_i) + '\n')
    f2.write("标记h的总个数count_h:" + str(count_h) + '\n')
    f2.write("标记x的总个数count_x:" + str(count_x) + '\n')
    f2.close()
    '''

    # 输出各个标记前不同汉字个数
    print("a标记不同汉字个数：", len(dic_a))
    print("i标记不同汉字个数：", len(dic_i))
    print("h标记不同汉字个数：", len(dic_h))
    print("x标记不同汉字个数：", len(dic_x))


    # 将各个标记前不同汉字个数写入txt文件
    '''
    f2 = open('D:\\pythonProject\\汉字标记集\\汉字标记的个数统计.txt', 'w', encoding='utf-8')
    f2.write("a标记不同汉字个数：" + str(len(dic_a)) + '\n')
    f2.write("i标记不同汉字个数：" + str(len(dic_i)) + '\n')
    f2.write("h标记不同汉字个数：" + str(len(dic_h)) + '\n')
    f2.write("x标记不同汉字个数：" + str(len(dic_x)) + '\n')
    f2.close()
    '''

    # 频数字典 降序 排序
    # dic_a = sorted(dic_a.items(), key = lambda x : x[1], reverse = True)
    dic_a = sorted(dic_a.items(), key = operator.itemgetter(1), reverse = True) # 按照item中的第二个字符进行排序，即按照value排序，排序后是list格式
    dic_i = sorted(dic_i.items(), key = operator.itemgetter(1), reverse = True)
    dic_h = sorted(dic_h.items(), key = operator.itemgetter(1), reverse = True)
    dic_x = sorted(dic_x.items(), key = operator.itemgetter(1), reverse = True)

    # 输出排序后的 “汉字mark” 频数字典
    # print(dic_a) # 字典排序后 变成了 list格式的
    print(dic_a[:100])  # dict(list) 将list 转为 字典
    print(dic_i[:100])
    print(dic_h[:100])
    print(dic_x[:100])

    # 将频数字典写入文件
    '''
    f3 = open('D:\\pythonProject\\汉字标记集\\num_hant_a.txt', 'w', encoding='utf-8')
    json.dump(dict(dic_a), f3, ensure_ascii=False)  # 加上“ensure_ascii=False”，则不按照Unicode编码，可以存放中文
    f3.close()
    f3 = open('D:\\pythonProject\\汉字标记集\\num_hant_i.txt', 'w', encoding='utf-8')
    json.dump(dict(dic_i), f3, ensure_ascii=False)  # 加上“ensure_ascii=False”，则不按照Unicode编码，可以存放中文
    f3.close()
    f3 = open('D:\\pythonProject\\汉字标记集\\num_hant_h.txt', 'w', encoding='utf-8')
    json.dump(dict(dic_h), f3, ensure_ascii=False)  # 加上“ensure_ascii=False”，则不按照Unicode编码，可以存放中文
    f3.close()
    f3 = open('D:\\pythonProject\\汉字标记集\\num_hant_x.txt', 'w', encoding='utf-8')
    json.dump(dict(dic_x), f3, ensure_ascii=False)  # 加上“ensure_ascii=False”，则不按照Unicode编码，可以存放中文
    f3.close()
    '''

    # 频率字典 降序排序
    dic_a_p = sorted(dic_a_p.items(), key=lambda x: x[1], reverse=True)
    dic_i_p = sorted(dic_i_p.items(), key=lambda x: x[1], reverse=True)
    dic_h_p = sorted(dic_h_p.items(), key=lambda x: x[1], reverse=True)
    dic_x_p = sorted(dic_x_p.items(), key=lambda x: x[1], reverse=True)

    # 输出 频率字典
    print(dic_a_p[:100])
    print(dic_i_p[:100])
    print(dic_h_p[:100])
    print(dic_x_p[:100])

    # 将频率字典写入文件
    '''
    f3 = open('D:\\pythonProject\\汉字标记集\\pro_hant_a.txt', 'w', encoding='utf-8')
    json.dump(dict(dic_a_p), f3, ensure_ascii=False)  # 加上“ensure_ascii=False”，则不按照Unicode编码，可以存放中文
    f3.close()
    f3 = open('D:\\pythonProject\\汉字标记集\\pro_hant_i.txt', 'w', encoding='utf-8')
    json.dump(dict(dic_i_p), f3, ensure_ascii=False)  # 加上“ensure_ascii=False”，则不按照Unicode编码，可以存放中文
    f3.close()
    f3 = open('D:\\pythonProject\\汉字标记集\\pro_hant_h.txt', 'w', encoding='utf-8')
    json.dump(dict(dic_h_p), f3, ensure_ascii=False)  # 加上“ensure_ascii=False”，则不按照Unicode编码，可以存放中文
    f3.close()
    f3 = open('D:\\pythonProject\\汉字标记集\\pro_hant_x.txt', 'w', encoding='utf-8')
    json.dump(dict(dic_x_p), f3, ensure_ascii=False)  # 加上“ensure_ascii=False”，则不按照Unicode编码，可以存放中文
    f3.close()
    '''