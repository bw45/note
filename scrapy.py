# import requests
# import re
# import json
# from bs4 import BeautifulSoup
# import csv
# import time
# import string
####day_one_two
#requests的7种方法
###___________________________________________httpbin.org/get
# data={'keyword':'nokia'} #设置数据集
# header={'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'} #设置头部信息,避免被屏蔽爬虫程序
# tmp=r.get('https://search.jd.com/Search',params=data,headers=header)
# tmp.encoding=tmp.apparent_encoding ##设置编码信息
# print(tmp.text)
# tmp=r.head('http://item.jd.com/100000287133.html',headers=header)
# print(tmp.headers)
# print(dir(tmp))
# print(tmp.text)



####day_three
#异常处理
#try: raise_for_status();except:
# def fist_scrapy(url):
# 	try:
# 		sample=r.get(url)
# 		sample.raise_for_status()
# 		sample.encoding=sample.apparent_encoding
# 		return sample.text
# 	except:
# 		return 'your spider is down'
# url='https://item.jd.com/100000287133.html'
# print(fist_scrapy(url))



####day_four
#text,content,status_code,headers,cookies,encoding,apparent_encoding
#网站对爬虫的来源或者IP进行审查
#网络图片下载和网站登陆
##下载图片
# url='https://img.zcool.cn/community/01dd5155499c1a0000019ae997cf7a.jpg@2o.jpg'
# tmp=r.get(url)
# with open('test.jpg','wb') as f:
# 	f.write(tmp.content)
##用cookies登陆
# headers={
# 	'Cookie':'_zap=a84acdba-7754-49b4-a11a-b16ae99ba925; d_c0="AADhjSIgyw6PThNrGxkMZeGMURahSRzoI-U=|1546929691"; q_c1=db0b2596595f44a489dae8f8fbda5dab|1546929693000|1546929693000; l_cap_id="OGIyMjVkYTZjZTQxNDZjNTg2ZWM5NWQ4ODZhY2Q2NDA=|1546933740|ea6d9b901a870e559d9664628f4884355ab83299"; r_cap_id="NDQ1Njc4ZTUwZDFiNDQxMmIzMzY2YzRjZDk5NmZiMGU=|1546933740|73dcac7593f2ad49be1c301645611ac3e00ed636"; cap_id="NjdlMmI4NTg4YTUwNDA0ZGFlYTAwNjk3YmJkODk4Njk=|1546933740|08ccadbf5fe9f2d4a7b8e6f8ed57125be6b7f25a"; _xsrf=YnGqQCHWUqFgzAa5DweP1hdfbOEXIgNX; capsion_ticket="2|1:0|10:1547168362|14:capsion_ticket|44:NmYxODc0ZDYxMjgzNDg5NmJjM2JiNmRhODc2NzVmYzI=|96693a7cebc94d41e81b9efe9e2060c902495d50ee627c38748893b46b0cf0d9"; z_c0="2|1:0|10:1547168387|4:z_c0|92:Mi4xWU01VkJ3QUFBQUFBQU9HTklpRExEaVlBQUFCZ0FsVk5nemdsWFFCWHNYS3lEMFlPOHhxRlBFTW5sRVVrTlgwSDNn|469f62774ce290e446349fba34a4b4d37f7f7524dfad7b1895ac04a690cd2617"; tst=r; __gads=ID=871b1dfa7040dda6:T=1547168880:S=ALNI_MY4jO6VBtANVUUaF_qN4XJL-e84Tw; tgw_l7_route=f2979fdd289e2265b2f12e4f4a478330',
# 	'Host':'www.zhihu.com',
# 	'User-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
# }
# tmp=r.get('https://www.zhihu.com',headers=headers)
# print(tmp.text)
##爬取多个页面
# def tmp(url):
# 	headers={'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
# 	response=r.get(url,headers=headers)
# 	if response.status_code==200:
# 		return(response.text)
# 	else:
# 		return '地址函数出错'
# def zz(html):
# 	pattern=re.compile('title=\"(.*?)\".*?star\">.*?：(.*?)</p>.*?releasetime\">.*?：(.*?)</p>',re.S)
# 	items=re.findall(pattern,html)
# 	result=[]
# 	for item in items:
# 		result.append({'电影名称':item[0],'主演':item[1].strip(),'上映时间':item[2]})
# 		# 'img':item[1],'名称':item[2],'主演':item[3].strip()[3:],'上映时间':item[4].strip()[5:]}
# 	return result
# def wrote_into_text(url):
# 	tmp1=tmp(url)
# 	zz1=zz(tmp1)
# 	with open('films.txt','a') as f:
# 		for i in zz1:
# 			f.write(str(i)+'\n')

# for i in range(0,10):
#     url='https://maoyan.com/board/4?offset='+str(i*10)
#     wrote_into_text(url)



####day_five_six

#beautifulsoup
#解析器 python标准库，lxml html解析器；lxml xml解析器；Html5lib

#Tag,NavigableString,BeautifulSoup,Comment

#children 包含子孙节点?
#descendants 包含孙节点?

#find_all(name,attrs,text)
# from bs4 import BeautifulSoup
# import re
# html_doc = """
# <html>
#     <head><title>The Dormouse's story</title></head>
#     <body>
#         <p class="story">
#             Once upon a time there were three little sisters; and their names were
#             <a href="http://example.com/elsie" class="sister" id="link1" name='wb'>
#             <span>Elsie</span>
#             </a>,
#             <a href="http://example.com/lacie" class="sister" id="link1">Lacie</a>
#               and
#             <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
#             and they lived at the bottom of a well.
#         </p>
#         <p class="story">...</p>
# """

# soup=BeautifulSoup(html_doc,'lxml')
# print(soup.p.children)
# for i,j in enumerate(soup.p.children):
# 	print(i,j)
# print(soup.p.descendants)
# for i,j in enumerate(soup.p.descendants):
# 	print(i,j)
# print(soup.p.parents)
# b=soup.find_all(attrs={'class':'sister'})
# for i in b:
# 	print(i)
# b=soup.find_all(id='link1')
# print(b)
# b=soup.find_all(text=re.compile('La'))
# print(b)

# def tmp(url):
# 	#设置头部信息，避免爬虫被屏蔽
# 	headers={'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
# 	#请求函数
# 	response=r.get(url,headers=headers)
# 	#判断是否请求成功
# 	if response.status_code==200:
# 		return(response.text)
# 	else:
# 		return '地址函数出错'
# def zz(html):
# 	#用beautifulsoup库&lxml解析html文件
# 	soup=BeautifulSoup(html,'lxml')
# 	#设置最后返回的列表
# 	result=[]
# 	#设置临时列表：每一部电影的容器
# 	tmp=[]
# 	#在解析后的函数里查找
# 	for a in soup.find_all(class_='movie-item-info'):
# 	#在查找到的内容中继续查找
# 		for i,j in enumerate(a.find_all(name='p')):
# 			if len(tmp) ==3:
# 				result.append(tmp)
# 				tmp=[]
# 				tmp.append(j.string.strip())
# 			else:
# 				tmp.append(j.string.strip())
# 	result.append(tmp)
# 	return result
# def wrote_into_text(url):
# 	tmp1=tmp(url)
# 	zz1=zz(tmp1)
# 	with open('films_soup_Be.txt','a') as f:
# 		for i in zz1:
# 			f.write(str(i)+'\n')
# 		# f.write('\n')
# 	return None
# for i in range(0,10):
#     url='https://maoyan.com/board/4?offset='+str(i*10)
#     wrote_into_text(url)



####day_seven

#选择器：节点选择器（<p>\<a>）、方法选择器(find_all()&find())、css选择器(select())、Xpath(与css类似，用于XML文档中搜索元素的路径语言)

# from bs4 import BeautifulSoup
# url='https://maoyan.com/board/4?offset=0'
# headers={'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
# #请求函数
# response=r.get(url,headers=headers)
# #判断是否请求成功
# soup=BeautifulSoup(response.text,'lxml')
# title=soup.select('#app > div > div > div.main > dl > dd > div > div > div.movie-item-info > p.name > a')
# actor=soup.select('#app > div > div > div.main > dl > dd > div > div > div.movie-item-info > p.star')
# time=soup.select('#app > div > div > div.main > dl > dd > div > div > div.movie-item-info > p.releasetime')
# for i,j,k in zip(title,actor,time):
# 	print(i.string,j.string.strip(),k.string)

# def tmp(url):
# 	#设置头部信息，避免爬虫被屏蔽
# 	headers={'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
# 	#请求函数
# 	response=r.get(url,headers=headers)
# 	#判断是否请求成功
# 	if response.status_code==200:
# 		return(response.text)
# 	else:
# 		return '地址函数出错'
# def zz(html):
# 	#用beautifulsoup库&lxml解析html文件
# 	soup=BeautifulSoup(html,'lxml')
# 	#设置最后返回的列表
# 	result=[]
# 	#css_selector方法
# 	title=soup.select('#app > div > div > div.main > dl > dd > div > div > div.movie-item-info > p.name > a')
# 	actor=soup.select('#app > div > div > div.main > dl > dd > div > div > div.movie-item-info > p.star')
# 	time=soup.select('#app > div > div > div.main > dl > dd > div > div > div.movie-item-info > p.releasetime')
# 	for i,j,k in zip(title,actor,time):
# 		tmp=[]
# 		tmp.append(i.string)
# 		tmp.append(j.string.strip())
# 		tmp.append(k.string)
# 		result.append(tmp)
# 	return result
# def wrote_into_text(url):
# 	tmp1=tmp(url)
# 	zz1=zz(tmp1)
# 	with open('films_soup_Beau.txt','a') as f:
# 		for i in zz1:
# 			f.write(str(i)+'\n')
# 		# f.write('\n')
# 	return None
# for i in range(0,10):
#     url='https://maoyan.com/board/4?offset='+str(i*10)
#     wrote_into_text(url)



####day_eight

#信息标记的三种形式
#组织方式
#html --- 显示数据
#标记方式
#xml json yaml
#xml --- 传输信息，存储信息
#json --- 键值对（字典）

#信息提取的一般方法

#信息存储
#txt
#json:loads() dumps() json只支持双引号描述

# def tmp(url):
# 	#设置头部信息，避免爬虫被屏蔽
# 	headers={'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
# 	#请求函数
# 	response=r.get(url,headers=headers)
# 	#判断是否请求成功
# 	if response.status_code==200:
# 		return(response.text)
# 	else:
# 		return '地址函数出错'
# def zz(html):
# 	#用beautifulsoup库&lxml解析html文件
# 	soup=BeautifulSoup(html,'lxml')
# 	#设置最后返回的列表
# 	result=[]
# 	#css_selector方法
# 	title=soup.select('#app > div > div > div.main > dl > dd > div > div > div.movie-item-info > p.name > a')
# 	actor=soup.select('#app > div > div > div.main > dl > dd > div > div > div.movie-item-info > p.star')
# 	time=soup.select('#app > div > div > div.main > dl > dd > div > div > div.movie-item-info > p.releasetime')
# 	for i,j,k in zip(title,actor,time):
# 		tmp=[]
# 		tmp.append(i.string)
# 		tmp.append(j.string.strip())
# 		tmp.append(k.string)
# 		result.append(tmp)
# 	return result
# def wrote_into_text(url):
# 	tmp1=tmp(url)
# 	zz1=zz(tmp1)
# 	print(zz1)
# 	f=open('films_soup_Beaut.csv','a',newline="") ####newline=""是避免写入文件后存在空行
# 	w=csv.writer(f)
# 	for i in zz1:
# 		w.writerow(i)

# 	# with open('films_soup_Beaut.json','a') as f:
# 	# 	f.write(json.dumps(zz1,ensure_ascii=False))  ####ensure_ascii=False是避免写入文件显示unicode

# 	return None
# for i in range(0,10):
#     url='https://maoyan.com/board/4?offset='+str(i*10)
#     wrote_into_text(url)



####day_nine

# def fisrt_sp(url):
# 	#设置头部信息，避免爬虫被屏蔽
# 	headers={'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
# 	#请求函数
# 	response=r.get(url,headers=headers)
# 	#判断是否请求成功
# 	if response.status_code==200:
# 		print('爬取url为:',url)
# 		return(response.text)
# 	else:
# 		print('地址函数出错')
# def second_sp(url_2):
# 	soup=BeautifulSoup(url_2,'lxml')
# 	second_result=[]
# 	if soup.select('#list_con > li > div.item_con.job_title > div.job_name.clearfix > a'):
# 		second_url=soup.select('#list_con > li > div.item_con.job_title > div.job_name.clearfix > a')
# 		for i in second_url:
# 			second_result.append(i.get('href'))
# 		return(second_result)
# 	else:
# 		print('当前网页无招聘信息')
	
# def zz(html):
# 	#用beautifulsoup库&lxml解析html文件
# 	#设置头部信息，避免爬虫被屏蔽
# 	headers={'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
# 	#请求函数
# 	response=r.get(html,headers=headers)
# 	if response.status_code==200:
# 		soup=BeautifulSoup(response.text,'lxml')
# 		result=[]
# 		title=soup.select('body > div.con > div.leftCon > div.item_con.pos_info > div.pos_base_info > span.pos_title')
# 		title_01=soup.select('body > div.con > div.leftCon > div.item_con.pos_info > span')
# 		salary=soup.select('body > div.con > div.leftCon > div.item_con.pos_info > div.pos_base_info > span.pos_salary')
# 		address=soup.select('body > div.con > div.leftCon > div.item_con.pos_info > div.pos-area > span.pos_area_span.pos_address')
# 		award=soup.select('body > div.con > div.leftCon > div.item_con.pos_info > div.pos_welfare')
# 		for i,j,k,l,m in zip(title,title_01,salary,address,award):
# 			tmp=[]
# 			tmp.append(i.string)
# 			tmp.append(j.string)
# 			tmp.append(k.text)
# 			tmp.append(l.text)
# 			tmp.append(m.text)
# 			result.append(tmp)
# 		return result
# 	else:
# 		print('地址函数出错')

# def wrote_into_text(url):
# 	tmp=fisrt_sp(url)
# 	try:
# 		zz1=second_sp(tmp)
# 		for i in zz1:
# 			time.sleep(1)
# 			final_word=zz(i)
# 			f=open('films_soup_Beaut.csv','a',newline="")
# 			w=csv.writer(f)
# 			for i in final_word:
# 				w.writerow(i)
# 	except:
# 		print('界面内无招聘信息')
# print('爬虫程序开始')
# for i in ['https://hz.58.com/ruanjiangong/pn{}/'.format(i) for i in range(6,8)]:
#     # url=['https://hz.58.com/ruanjiangong/pn{}/' i for i in range(10)] 
#     wrote_into_text(i)
#     time.sleep(1)
# print('爬虫程序结束')



#day_ten

#ajax数据提取（ajax实现异步更新）
#微博文本爬取

# url='https://movie.douban.com/j/chart/top_list?'
# headers={
#     'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
#     'X-Requested-With':'XMLHttpRequest',
#     'Host':'movie.douban.com',
#     'Referer':'https://movie.douban.com/typerank?'
# }

# def first(url,start):
# 	params={'type':'5','interval_id':'100:90','start':start,'limit':20}
# 	response=requests.get(url,headers=headers,params=params)
# 	items=response.json()
# 	# items=items.get('rating')
# 	for i in items:
# 		tmp=[]
# 		tmp.append(i.get('rank'))
# 		tmp.append(i.get('title'))
# 		tmp.append(i.get('types'))
# 		tmp.append(i.get('regions'))
# 		final_data.append(tmp)
# 	for i in final_data:
# 		print(i)

    
# for i in [i*20 for i in range(1)]:
# 	final_data=[]
# 	first(url,i)




####day_eleven_twelve

#正则表达式
#.    匹配\n之外所有任何字符，[.\n]表示全部
#\d   匹配数字，等于[0-9]
#\D   匹配一个非数字字符，等于[^0-9]
#\s   匹配任何空白字符，包括空格、制表符、换行符等等，等价于[\f\n\r\t\v]
#\w   匹配包括下划线的任何单词字符，等价于[A-Za-z0-9]
#\W   匹配任何非单词字符，等价于[^A-Za-z0-9]
#$    字符串结尾？
#贪婪匹配和非贪婪匹配 用问号？区分
#非贪婪匹配模式结果比较正确
#尽量使用泛匹配、使用括号得到匹配目标，尽量使用非贪婪模式，有换行符用re.S
#[\u4e00-\u9fa5] 匹配中文字符

# a='helloBC'
# b='helloB'
# c='helloA'
# d='helloBCX'
# test='.*BC?$'
# a=re.match(test,b)
# print(a.group())

# a='A1232344'
# b='abc1234'
# c='12345'
# d='b493034'
# test='[A-Za-z][0-9]+'
# a=re.match(test,d)
# print(a.group())

# a='0aaaax'
# b='aaab9'
# c='中哈哈'
# d='zz22zzss22'
# test='[\u4e00-\u9fa5]{3}'
# a=re.match(test,c)
# print(a.group())

#能用search不用match
#compile含义？


# # url='https://movie.douban.com/top250'
# headers={
#     'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
#     'X-Requested-With':'XMLHttpRequest',
#     'Host':'movie.douban.com',
#     'Referer':'https://movie.douban.com/typerank?'
# }
# abcd=string.ascii_lowercase+string.ascii_uppercase
# def first(url):
# 	response=requests.get(url,headers=headers)
# 	# tmp=re.compile('<li>.*?<span.class=\"title\">(.*?)</span>.*?class=\"other\">.*?<div.class=\"star\">.*?</li>',re.S)
# 	tmp=re.compile('<li>.*?<span.class=\"title\">(.*?)</span>.*?class=\"other\">.*?<div.class=\"bd\">.*?<p.class=\"\">(.*?)</p>.*?</div>.*?</li>',re.S)
# 	item=re.findall(tmp,response.text)
# 	for i in item:
# 		for j in i:
# 			print(j.strip().replace('&nbsp;','').replace('\n','').replace(' ',''))
# 		print()
	   
# for i in ['https://movie.douban.com/top250?start={}&filter='.format(i*25) for i in range(10)]:
# 	first(i)




####day_thirteen_fourteen

#scrapy
#安装scrapy
#开始第一个项目 scrapy startproject xxxx
#开始运行第一个项目 scrapy crawl xxxx
#scrapy ::: xpath css re extract


# from scrapy import Selector
# body='<html><title>sss</title></html>'
# selector=Selector(text=body)
# title=selector.xpath('//title/text()').extract_first()
# print(title)




####day_fifteen_sixteen

#scrapy-spider运行流程
#1.定义爬取网站的动作 2.分析爬取下来的网页

#使用步骤
#创建工程和spider模板，编写spider,编写item pipeline,优化配置策略

#downloader middlewares:修改user-agent,处理重定向，设置代理，失败重试，设置cookies

#item类

#项目实战：srapy抓取豆瓣信息

##yield????不会占用很大的内存，会生成一个迭代器
# def fab(max):
# 	n,a,b=0,0,1
# 	while n<max:
# 		yield ('a',a)
# 		yield b
# 		a,b=b,a+b
# 		n=n+1
# # for i in fab(5):
# # 	print(i)
# a=fab(10)
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))




####day_seventeen

#非关系型数据库-mongodb
#pymongo使用



###拉钩网绕过爬虫限制，代cookie
# cookie={'_ga':'GA1.2.26789794.1553589307',
# 'user_trace_token':'20190326163504-0d7377f9-4fa2-11e9-95b5-525400f775ce',
# 'LGUID':'20190326163504-0d737b3a-4fa2-11e9-95b5-525400f775ce',
# 'showExpriedIndex':'1',
# 'showExpriedCompanyHome':'1',
# 'showExpriedMyPublish':'1',
# 'hasDeliver':'59',
# 'index_location_city':r'%E6%88%90%E9%83%BD',
# 'sensorsdata2015jssdkcross':r'%7B%22distinct_id%22%3A%227576617%22%2C%22%24device_id%22%3A%22169bea636518e8-0c09fc9c93a061-5f1d3817-1049088-169bea6365266c%22%2C%22props%22%3A%7B%22%24latest_utm_source%22%3A%22m_cf_cpt_baidu_pcbt%22%2C%22%24os%22%3A%22Windows%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%2273.0.3683.86%22%7D%2C%22first_id%22%3A%22169bea636518e8-0c09fc9c93a061-5f1d3817-1049088-169bea6365266c%22%7D',
# 'JSESSIONID':'ABAAABAAADEAAFIB6BEF4733E1EF6386E6DA92CD7EB90E0',
# '_gid':'GA1.2.318481555.1554270899',
# 'Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6':'1553589308,1553681713,1554270899',
# 'LGSID':'20190403144045-68f0b5e1-55db-11e9-bd18-5254005c3644',
# 'TG-TRACK-CODE':'search_code',
# '_gat':'1',
# 'login':'false',
# 'unick':'',
# '_putrc':'',
# 'LG_LOGIN_USER_ID':'',
# 'X_MIDDLE_TOKEN':'551f0a1f1e5490a48786484249a9376e',
# 'X_HTTP_TOKEN':'4ab2b9bab119cbb644667245511bd14c6ed1b76751',
# 'Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6':'1554276645',
# 'LGRID':'20190403153044-6453ff87-55e2-11e9-bd1a-5254005c3644',
# 'SEARCH_ID':'bba023f5647249ef9d651d037613b6d4'
# }

####day_eighteen

#爬取拉钩数据
import time
import requests as r
import re
import random
import json

url=r'http://172.16.42.20:84/mspapi/login/dologin'
data={'px':'default','city':'成都','needAddtionalResult':'false','fisrt':'true','pn':'1','kd':'运营'}
data_ak={'username':'aa22222','password':'aaa','auth_code':'sdsd'}

cookie={'_ga':'GA1.2.26789794.1553589307',
'user_trace_token':'20190326163504-0d7377f9-4fa2-11e9-95b5-525400f775ce',
'LGUID':'20190326163504-0d737b3a-4fa2-11e9-95b5-525400f775ce',
'showExpriedIndex':'1',
'showExpriedCompanyHome':'1',
'showExpriedMyPublish':'1',
'hasDeliver':'59',
'index_location_city':r'%E6%88%90%E9%83%BD',
'sensorsdata2015jssdkcross':r'%7B%22distinct_id%22%3A%227576617%22%2C%22%24device_id%22%3A%22169bea636518e8-0c09fc9c93a061-5f1d3817-1049088-169bea6365266c%22%2C%22props%22%3A%7B%22%24latest_utm_source%22%3A%22m_cf_cpt_baidu_pcbt%22%2C%22%24os%22%3A%22Windows%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%2273.0.3683.86%22%7D%2C%22first_id%22%3A%22169bea636518e8-0c09fc9c93a061-5f1d3817-1049088-169bea6365266c%22%7D',
'JSESSIONID':'ABAAABAAADEAAFIB6BEF4733E1EF6386E6DA92CD7EB90E0',
'_gid':'GA1.2.318481555.1554270899',
'Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6':'1553589308,1553681713,1554270899',
'LGSID':'20190403144045-68f0b5e1-55db-11e9-bd18-5254005c3644',
'TG-TRACK-CODE':'search_code',
'_gat':'1',
'login':'false',
'unick':'',
'_putrc':'',
'LG_LOGIN_USER_ID':'',
'X_MIDDLE_TOKEN':'551f0a1f1e5490a48786484249a9376e',
'X_HTTP_TOKEN':'4ab2b9bab119cbb621187245511bd14c6ed1b76751',
'Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6':'1554278113',
'LGRID':'20190403155512-cf112eda-55e5-11e9-bd1b-5254005c3644',
'SEARCH_ID':'e75cb8f0bdd8447bbd04a9d44e726727'
}

header={'User-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
# 'Referer':r'https://www.lagou.com/jobs/list_%E8%BF%90%E8%90%A5?px=default&city=%E6%88%90%E9%83%BD',
# 'Host':'www.lagou.com',
# 'Origin':'https://www.lagou.com',
'X-Requested-With':'XMLHttpRequest',
# 'X-Anit-Forge-Token':'None',
# 'X-Anit-Forge-Code':'0',
'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8'}

pro=[{'http':'http://120.79.203.1:3128'},
     {'http':'http://115.151.6.52:9999'},
     {'http':'http://118.190.73.168:808'},
     {'http':'http://110.52.235.57:9999'},
     {'http':'http://219.159.38.209:56210'},
     {'http':'http://111.72.154.28:9999'},
     {'http':'http://111.77.22.20:9000'},

]
j_data=json.dumps(data_ak)
# a1=r.get(url,headers=header,params=data,cookies=cookie,proxies=random.choice(pro))
a1=r.post(url,j_data)
print(dir(a1))
# a1.encoding=a1.apparent_encoding 
print(a1.text)
print(a1.content)

# # print(a.text)
# print(a1.text)

##############识别验证码
# import pytesseract as py
# from PIL import Image
# a=Image.open(r'C:\Users\Administrator\Desktop\3.jpg')
# a1=Image.open(r'C:\Users\Administrator\Desktop\2.jpg')
# b=py.image_to_string(a)
# b1=py.image_to_string(a1)
# print(type(b))
# print(b)
# print(type(b1))
# print(b1)


###用webdriver爬取拉钩数据
# import re
# import time
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from bs4 import BeautifulSoup

# d=webdriver.Chrome()
# d.maximize_window()
# job='运营'
# city='成都'

# def next_page(html,window):
# 	soup=BeautifulSoup(html,'lxml')
# 	company=soup.select('div.s_position_list > ul > li > div.list_item_top > div.company > div.company_name > a')
# 	date=soup.select('div.s_position_list > ul > li > div.list_item_top > div.position > div.p_top > span')
# 	money=soup.select('div.s_position_list > ul > li > div.list_item_top > div.position > div.p_bot > div > span')
# 	require=soup.select('div.s_position_list > ul > li > div.list_item_top > div.position > div.p_bot > div ')
# 	name=soup.select('div.s_position_list > ul > li > div.list_item_top > div.position > div.p_top > a.position_link > h3')
# 	for i,j,k,l,m in zip(name,money,require,company,date):
# 		print('{0:<15}{1:<15}{2:<15}{3:<15}{4}'.format(i.string,j.string,re.search('经验(.*)',k.text.strip()).group(1),l.string,m.string))
# 	time.sleep(1)
# 	print('next page is going')
# 	if not '前' in str([i.string for i in date]):
# 		window.find_element_by_xpath('//div[@class="pager_container"]/span[@class="pager_next "]').click()
# 		time.sleep(1)
# 		next_page(window.page_source,window)
# 	else:
# 		window.close()
# def main():
# 	d.get(r'https://www.lagou.com/jobs/list_{0}?px=new&city={1}#order'.format(job,city,pn))
# 	next_page(d.page_source,d)

# if __name__ == '__main__':
# 	main()

# import requests as re
# import re as r
# import time
# import os
# from bs4 import BeautifulSoup


# def rob():
# 	try:
# 		header={'USER-AGENT':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# 		data={'leftTicketDTO.train_date':'2019-04-05','leftTicketDTO.from_station':'CDW','leftTicketDTO.to_station':'RXW','purpose_codes':'ADULT'}
# 		a=re.get('https://kyfw.12306.cn/otn/leftTicket/query?',params=data,headers=header)
# 		soup=BeautifulSoup(a.text,'lxml')
# 		a=r.search('(D5184).*?201904(.*?)null',str(soup))
# 		if '有' in a.group(2):
# 			print('抢到了！！！！')
# 			print(a.group(2))
# 			os._exit(0)
# 		return a.group(2)
# 	except:
# 		print('你的ip好像被封了')

# i=1
# while 1<1000:
# 	try:
# 		test=rob()
# 		print(test,i)
# 		time.sleep(1)
# 	except:
# 		pass
# 	i+=1
