import requests,json,time,re
from requests.exceptions import RequestException
from pyquery import PyQuery as pq
from fontTools.ttLib import TTFont
from io import BytesIO
import time 

def get_font(url):
    response = requests.get(url)
    font = TTFont(BytesIO(response.content))
    cmap = font.getBestCmap()
    font.close()
    return cmap

def get_encode(cmap,values):
    WORD_MAP = {'zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9','period':'.'}
    word_count=''
    for value in values.split(';'):
        value = value[2:]
        key = cmap[int(value)]
        word_count += WORD_MAP[key]
    return word_count

def rereturn(list):
    if len(list)>0:
        return list[0]
    else:
        return 0

def get_index(start_url):
    #获取当前页面的html
    response = requests.get(start_url).text   
    doc = pq(response)
    #获取当前字体文件名称
    classattr = doc('p.update > span > span').attr('class')
    pattern = '</style><span.*?%s.*?>(.*?)</span>'%classattr
    #获取当前页面所有被字数字符
    numberlist = re.findall(pattern,response)
    #获取当前包含字体文件链接的文本
    fonturl = doc('p.update > span > style').text() 
    #通过正则获取当前页面字体文件链接
    url = re.search('woff.*?url.*?\'(.+?)\'.*?truetype',fonturl) .group(1)
    cmap = get_font(url)
    for num in numberlist:
        response=response.replace(num,get_encode(cmap,num[:-1]))
    doc = pq(response)
    books = doc('.all-img-list li').items()
    listx=[]
    for book in books:
        item = {}
        item['link']=book('.book-mid-info h4 a').attr('href')
        item['bookname'] = book('.book-mid-info h4 a').text()
        item['author'] = book('.name').text()
        item['classes1'] = book('p.author > a:nth-child(4)').text()
        item['classes2'] = book('p.author > a:nth-child(6)').text()
        item['status'] = book('p.author span').text()
        item['content'] = book('.intro').text()
        item['number'] = book('p.update span span').text()+re.findall("(万字|字)", book('p.update span ').text())[0]
        item['collection']=book('p.update b span').text()+re.findall("(万总收藏|总收藏|千总收藏|百总收藏)", book('p.update b').text())[0]
        listx.append(item)   
    return listx
    
    
import pandas
booklist_new_df=pandas.read_csv('data1.csv')
len(booklist_new_df) 
    
def get_detail(start_url):
    #获取当前页面的html
    response = requests.get(start_url).text   
    doc = pq(response)
    #获取当前字体文件名称
    classattr = doc('p>em>span').attr('class')
    pattern = '</style><span.*?%s.*?>(.*?)</span>'%classattr
    #获取当前页面所有被字数字符
    numberlist = re.findall(pattern,response)
    #获取当前包含字体文件链接的文本
    fonturl = doc('p>em>style').text() 
    #通过正则获取当前页面字体文件链接
    url = re.search('woff.*?url.*?\'(.+?)\'.*?truetype',fonturl) .group(1)
    cmap = get_font(url)
    for num in numberlist:
        response=response.replace(num,get_encode(cmap,num[:-1]))
    doc = pq(response)
    item={}
    item['link']=start_url
    item['intro_1']=doc('.book-info p.intro').text()
    item['clicks']=doc('.book-info p em:nth-child(4) span ').text()+re.findall("(万总会员点击|总会员点击|千总会员点击|百总会员点击)", doc('.book-info p cite:nth-child(5)').text())[0]
    item['recomand']=doc('.book-info p em:nth-child(7) span ').text()+re.findall("(万总推荐|总推荐|千总推荐|百总推荐)", doc('.book-info p cite:nth-child(8)').text())[0]
    item['intro_2']=doc('.book-intro').text()
    item['tags']=doc('.tag-wrap a.tags').text()
    return item
    
detail=[]
errorlist=[]


for i in range(22500,25000):
    try:
        items=get_detail('https:'+booklist_new_df.loc[i]['link'])
    except:
        try:
            items=get_detail('https:'+booklist_new_df.loc[i]['link'])
        except:
            try:
                items=get_detail('https:'+booklist_new_df.loc[i]['link'])
            except:     
                items='error!'
                print('error!')
                errorlist.append(i)
    detail.append(items) 
    print(i)
    
    
    
#errorlist
errorlist
detail_1=detail

for i in errorlist:
    try:
        items=get_detail('https:'+booklist_new_df.loc[i]['link'])
    except:
        try:
            items=get_detail('https:'+booklist_new_df.loc[i]['link'])
        except:
            try:
                items=get_detail('https:'+booklist_new_df.loc[i]['link'])
            except:     
                items='error!'
                print('error!')
    detail[i-22500]=items 
    print(i)
    
    
    
item={}
item['link']=booklist_new_df.loc[i]['link']
item['intro_1']='页面已失效'
item['clicks']='页面已失效'
item['recomand']='页面已失效'
item['intro_2']='页面已失效'
item['tags']='页面已失效'
    
    
    
    









detail_df=pandas.DataFrame(detail)
detail_df.to_csv('data2_10.csv',encoding='utf8')


#
data2_1=pandas.read_csv('data2_1.csv')
data2_2=pandas.read_csv('data2_2.csv')
data2_3=pandas.read_csv('data2_3.csv')
data2_4=pandas.read_csv('data2_4.csv')
data2_5=pandas.read_csv('data2_5.csv')
data2_6=pandas.read_csv('data2_6.csv')
data2_7=pandas.read_csv('data2_7.csv')
data2_8=pandas.read_csv('data2_8.csv')
data2_9=pandas.read_csv('data2_9.csv')
data2_10=pandas.read_csv('data2_10.csv')


DATA2=data2_1
DATA2=DATA2.append(data2_2).append(data2_3).append(data2_4).append(data2_5).append(data2_6).append(data2_7).append(data2_8).append(data2_9).append(data2_10)
DATA2.to_csv('DATA2.csv',encoding='utf8')


from pandasql import sqldf
pysqldf = lambda q: sqldf(q, globals())
booklist_new_df=pysqldf("SELECT *,REPLACE(link,'//book.qidian.com/info/','') as bookid  FROM  booklist_new_df ")
DATA2=pysqldf("SELECT *,REPLACE(link,'https://book.qidian.com/info/','') as bookid  FROM  DATA2 ")

DATA=pysqldf("SELECT * FROM booklist_new_df a join DATA2 b on a.bookid=b.bookid")
DATA.to_csv('DATA_final.csv',encoding='utf8')