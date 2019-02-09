# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 19:50:07 2018

@author: 64283
"""
import pandas as pd
# 请更改为文件所在路径！！！
file = 'C:/Users/64283/Desktop/数据挖掘final/作图与LDA/lightbook.xlsx'
data=pd.read_excel(file,sheet_name='Sheet1',keep_default_na=True)


import seaborn as sns
import matplotlib.pyplot as plt  
from matplotlib.font_manager import FontProperties
#设置中文显示
myfont=FontProperties(fname=r'C:\Windows\Fonts\simhei.ttf',size=14)
sns.set(font=myfont.get_name())
#设置背景
sns.set_style("whitegrid",{"font.sans-serif":['simhei','Droid Sans Fallback']})

# 按照图片编号逐段运行程序！！！
# 图1：分类-条形图
from collections import Counter
a = Counter(data['classes1'])
a = pd.DataFrame.from_dict(a,orient='index').reset_index()
a = a.rename(columns={'index':'类型',0:'频数'})
plt.figure(figsize = (12, 8))
ax = sns.barplot(x="类型", y="频数", data=a, palette="Blues_d")
ax.tick_params(axis='x',labelsize=13) 
ax.tick_params(axis='y',labelsize=16)
plt.xlabel('分类', fontsize=20)
plt.ylabel('频数', fontsize=20)
plt.tight_layout()
ax.figure.savefig('图1：分类-条形图.png', dpi=400, bbox_inches='tight')


# 图2：收藏数-分类箱线图
import math
data['collection2']=data['collection1'].apply(lambda x: math.log10(x))
plt.figure(figsize = (12, 8))
ax = sns.boxplot(x="classes1", y="collection2", data=data, palette="Blues_d")
ax.tick_params(axis='x',labelsize=16) 
ax.tick_params(axis='y',labelsize=16)
plt.xlabel('分类', fontsize=20)
plt.ylabel('收藏数（对数变换）', fontsize=20)
plt.yticks([3,4,5,6],['1千','1万','10万','100万'])
plt.tight_layout()
ax.figure.savefig('图2：收藏数-分类-箱线图.png', dpi=400, bbox_inches='tight')

# 图3：点击数-分类箱线图
data['clicks2']=data['clicks1'].apply(lambda x: math.log10(x))
plt.figure(figsize = (12, 8))
ax = sns.boxplot(x="classes1", y="clicks2", data=data, palette="Blues_d")
ax.tick_params(axis='x',labelsize=16) 
ax.tick_params(axis='y',labelsize=16)
plt.xlabel('分类', fontsize=20)
plt.ylabel('点击数（对数变换）', fontsize=20)
plt.yticks([2,3,4,5,6,7,8],['1百','1千','1万','10万','100万','1000万','1亿'])
plt.tight_layout()
ax.figure.savefig('图3：点击数-分类-箱线图.png', dpi=400, bbox_inches='tight')

# 图4：推荐数-分类箱线图
data['recomand2']=data['recomand1'].apply(lambda x: math.log10(x))
plt.figure(figsize = (12, 8))
ax = sns.boxplot(x="classes1", y="recomand2", data=data, palette="Blues_d")
ax.tick_params(axis='x',labelsize=16) 
ax.tick_params(axis='y',labelsize=16)
plt.xlabel('分类', fontsize=20)
plt.ylabel('推荐数（对数变换）', fontsize=20)
plt.yticks([1,2,3,4,5,6,7],['10','1百','1千','1万','10万','100万','1000万'])
plt.tight_layout()
ax.figure.savefig('图4：推荐数-分类-箱线图.png', dpi=400, bbox_inches='tight')

# 图5：收藏数-点击数散点图
plt.figure(figsize = (12, 8))
ax = sns.regplot(x='collection2', y='clicks2', data=data)
ax.tick_params(axis='x',labelsize=16) 
ax.tick_params(axis='y',labelsize=16)
plt.xlabel('收藏数（对数变换）', fontsize=20)
plt.ylabel('点击数（对数变换）', fontsize=20)
plt.xticks([3,4,5,6],['1千','1万','10万','100万'])
plt.yticks([2,3,4,5,6,7,8],['1百','1千','1万','10万','100万','1000万','1亿'])
plt.tight_layout()
ax.figure.savefig('图5：收藏数-点击数散点图.png', dpi=400, bbox_inches='tight')


# 图6：收藏数-推荐数散点图
plt.figure(figsize = (12, 8))
ax = sns.regplot(x='collection2', y='recomand2', data=data)
ax.tick_params(axis='x',labelsize=16) 
ax.tick_params(axis='y',labelsize=16)
plt.xlabel('收藏数（对数变换）', fontsize=20)
plt.ylabel('推荐数（对数变换）', fontsize=20)
plt.xticks([3,4,5,6],['1千','1万','10万','100万'])
plt.yticks([1,2,3,4,5,6,7],['10','1百','1千','1万','10万','100万','1000万'])
plt.tight_layout()
ax.figure.savefig('图6：收藏数-推荐数散点图.png', dpi=400, bbox_inches='tight')

# 图7：推荐数-点击数散点图
plt.figure(figsize = (12, 8))
ax = sns.regplot(x='recomand2', y='clicks2', data=data, ci=95)
ax.tick_params(axis='x',labelsize=16) 
ax.tick_params(axis='y',labelsize=16)
plt.xlabel('推荐数（对数变换）', fontsize=20)
plt.ylabel('点击数（对数变换）', fontsize=20)
plt.xticks([1,2,3,4,5,6,7],['10','1百','1千','1万','10万','100万','1000万'])
plt.yticks([2,3,4,5,6,7,8],['1百','1千','1万','10万','100万','1000万','1亿'])
plt.tight_layout()
ax.figure.savefig('图7：推荐数-点击数散点图.png', dpi=400, bbox_inches='tight')

# 取前300收藏数
data1=data[0:300]

# 图8：分类-条形图（前300）
a = Counter(data1['classes1'])
a = pd.DataFrame.from_dict(a,orient='index').reset_index()
a = a.rename(columns={'index':'类型',0:'频数'})
plt.figure(figsize = (12, 8))
ax1 = sns.barplot(x="类型", y="频数", data=a, palette="Blues_d")
ax1.tick_params(axis='x',labelsize=13) 
ax1.tick_params(axis='y',labelsize=16)
plt.xlabel('分类', fontsize=20)
plt.ylabel('频数', fontsize=20)
plt.tight_layout()
ax1.figure.savefig('图8：分类-条形图（前300）.png', dpi=400, bbox_inches='tight')

# 图9：收藏数-分类箱线图（前300）
plt.figure(figsize = (12, 8))
ax = sns.boxplot(x="classes1", y="collection2", data=data1, palette="Blues_d")
ax.tick_params(axis='x',labelsize=16) 
ax.tick_params(axis='y',labelsize=16)
plt.xlabel('分类', fontsize=20)
plt.ylabel('收藏数（对数变换）', fontsize=20)
plt.yticks([5,6],['10万','100万'])
plt.tight_layout()
ax.figure.savefig('图9：收藏数-分类-箱线图（前300）.png', dpi=400, bbox_inches='tight')

# 图10：点击数-分类箱线图（前300）
plt.figure(figsize = (12, 8))
ax = sns.boxplot(x="classes1", y="clicks2", data=data1, palette="Blues_d")
ax.tick_params(axis='x',labelsize=16) 
ax.tick_params(axis='y',labelsize=16)
plt.xlabel('分类', fontsize=20)
plt.ylabel('点击数（对数变换）', fontsize=20)
plt.yticks([5,6,7,8],['10万','100万','1000万','1亿'])
plt.tight_layout()
ax.figure.savefig('图10：点击数-分类-箱线图（前300）.png', dpi=400, bbox_inches='tight')

# 图11：推荐数-分类箱线图（前300）
plt.figure(figsize = (12, 8))
ax = sns.boxplot(x="classes1", y="recomand2", data=data1, palette="Blues_d")
ax.tick_params(axis='x',labelsize=16) 
ax.tick_params(axis='y',labelsize=16)
plt.xlabel('分类', fontsize=20)
plt.ylabel('推荐数（对数变换）', fontsize=20)
plt.yticks([4,5,6,7],['1万','10万','100万','1000万'])
plt.tight_layout()
ax.figure.savefig('图11：推荐数-分类-箱线图（前300）.png', dpi=400, bbox_inches='tight')
