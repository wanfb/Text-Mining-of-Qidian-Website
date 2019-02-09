# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 23:30:40 2018

@author: 64283
"""
import pandas as pd
from gensim import corpora, models
import jieba.posseg as jp, jieba
file = 'C:/Users/64283/Desktop/数据挖掘final/作图与LDA/cluster.xlsx'
data=pd.read_excel(file,sheet_name='Sheet1',keep_default_na=True)


# 提取各分类的前百本小说，语句中的1可以改为2，3，4，为4大分类，可以得到各自的结果
fenlei = data[data['label']==1]['abstract'].copy().dropna().tolist()
fenlei = fenlei[0:100]

# 文本集
texts = fenlei
# 分词过滤条件
jieba.add_word('人')
flags = ('n', 'ns', 'nt','v')  # 词性
stopwords_path = 'C:/Users/64283/Desktop/数据挖掘final/作图与LDA/stopword/stopWord.txt' # 停用词词表
file = open(stopwords_path,'r',encoding='utf8')
stopwords = file.read().split() # 停词表的创建 
stopwords.append('群号码')
stopwords.append('YY')
stopwords.append('加群')
stopwords.append('方想')
stopwords.append('收藏')
# stopwords.append('重生') # 对于分类4，需要加上“重生”作为停词

# 分词
words_ls = []
for text in texts:
    words = [word.word for word in jp.cut(text) if word.flag in flags and word.word not in stopwords and len(word.word)>1]
    words_ls.append(words)

# 构造词典
dictionary = corpora.Dictionary(words_ls)
# 基于词典，形成稀疏向量集
corpus = [dictionary.doc2bow(words) for words in words_ls]
# lda模型，num_topics设置主题的个数
tfidf = models.TfidfModel(corpus)
corpus_tfidf = tfidf[corpus]
lda = models.ldamodel.LdaModel(corpus=corpus_tfidf, id2word=dictionary, num_topics=3)
# 打印所有主题，每个主题显示8个词
for topic in lda.print_topics(num_words=8):
    print(topic)