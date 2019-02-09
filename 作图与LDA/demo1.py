# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 20:32:01 2018

@author: 64283
"""
from scipy.misc import imread
import matplotlib.pyplot as plt
import jieba
from wordcloud import WordCloud, ImageColorGenerator

# 设置路径
#   1）背景图片路径
back_coloring_path = 'C:/Users/64283/Desktop/数据挖掘final/作图与LDA/book.png'
#   2）#为matplotlib设置中文字体路径
font_path = 'C:/Windows/Fonts/simhei.ttf' 
#   3）设置停词表路径
stopwords_path = 'C:/Users/64283/Desktop/数据挖掘final/作图与LDA/stopword/stopWord.txt' # 停用词词表

# 设置背景图片
back_coloring = imread(back_coloring_path)

# 设置词云属性
wc = WordCloud(font_path=font_path,  # 设置字体
               background_color="white",  # 背景颜色
               max_words=2000,  # 词云显示的最大词数
               mask=back_coloring,  # 设置背景图片
               max_font_size=100,  # 字体最大值
               random_state=42,
               width=1000, height=860, margin=2,# 设置图片默认的大小,但是如果使用背景图片的话,那么保存的图片大小将会按照其大小保存,margin为词语边缘距离
               )

# 设置停词表
file = open(stopwords_path,'r',encoding='utf8')
stoplist = file.read().split()

# 停词与切词函数
def jieci(text_path):
    file = open(text_path,'r')
    LIST = file.read().split()
    words=[]
    for STR in LIST:
        String=jieba.cut(STR)
        String=filter(lambda word: word not in stoplist,String)
        words.extend(String)
        content =' '.join(words)
    return content

# 词云1：都市
dushi_path = 'C:/Users/64283/Desktop/数据挖掘final/作图与LDA/分类/dushi.txt'
dushi = jieci(dushi_path) #停词与切词
wc.generate(dushi) # 生成词云
image_colors = ImageColorGenerator(back_coloring) # 从背景图片生成颜色值
plt.figure(figsize = (12, 8))
plt.imshow(wc.recolor(color_func=image_colors))
plt.axis("off") #去掉坐标轴
plt.savefig('词云1：都市.png', dpi=400, bbox_inches='tight')

# 词云2：科幻
kehuan_path = 'C:/Users/64283/Desktop/数据挖掘final/作图与LDA/分类/kehuan.txt'
kehuan = jieci(kehuan_path) #停词与切词
wc.generate(kehuan) # 生成词云
image_colors = ImageColorGenerator(back_coloring) # 从背景图片生成颜色值
plt.figure(figsize = (12, 8))
plt.imshow(wc.recolor(color_func=image_colors))
plt.axis("off") #去掉坐标轴
plt.savefig('词云2：科幻.png', dpi=400, bbox_inches='tight')

# 词云3：仙侠
xianxia_path = 'C:/Users/64283/Desktop/数据挖掘final/作图与LDA/分类/xianxia.txt'
xianxia = jieci(xianxia_path) #停词与切词
wc.generate(xianxia) # 生成词云
image_colors = ImageColorGenerator(back_coloring) # 从背景图片生成颜色值
plt.figure(figsize = (12, 8))
plt.imshow(wc.recolor(color_func=image_colors))
plt.axis("off") #去掉坐标轴
plt.savefig('词云3：仙侠.png', dpi=400, bbox_inches='tight')

# 词云4：奇幻
qihuan_path = 'C:/Users/64283/Desktop/数据挖掘final/作图与LDA/分类/qihuan.txt'
qihuan = jieci(qihuan_path) #停词与切词
wc.generate(qihuan) # 生成词云
image_colors = ImageColorGenerator(back_coloring) # 从背景图片生成颜色值
plt.figure(figsize = (12, 8))
plt.imshow(wc.recolor(color_func=image_colors))
plt.axis("off") #去掉坐标轴
plt.savefig('词云4：奇幻.png', dpi=400, bbox_inches='tight')

# 词云5：玄幻
xuanhuan_path = 'C:/Users/64283/Desktop/数据挖掘final/作图与LDA/分类/xuanhuan.txt'
xuanhuan = jieci(xuanhuan_path) #停词与切词
wc.generate(xuanhuan) # 生成词云
image_colors = ImageColorGenerator(back_coloring) # 从背景图片生成颜色值
plt.figure(figsize = (12, 8))
plt.imshow(wc.recolor(color_func=image_colors))
plt.axis("off") #去掉坐标轴
plt.savefig('词云5：玄幻.png', dpi=400, bbox_inches='tight')

# 词云6：历史
lishi_path = 'C:/Users/64283/Desktop/数据挖掘final/作图与LDA/分类/lishi.txt'
lishi = jieci(lishi_path) #停词与切词
wc.generate(lishi) # 生成词云
image_colors = ImageColorGenerator(back_coloring) # 从背景图片生成颜色值
plt.figure(figsize = (12, 8))
plt.imshow(wc.recolor(color_func=image_colors))
plt.axis("off") #去掉坐标轴
plt.savefig('词云6：历史.png', dpi=400, bbox_inches='tight')