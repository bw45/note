####代码整洁之道
#变量：易懂的名字
#类名：应该是名词 不是动词
#函数名：应当是动词或者动词短语，前面加上get\set\is
#函数第一规则是要短小，第二规则还是要更短小
#import numpy as np
#import matplotlib.pyplot as plt
#
#x=np.array([1,2,3,4,5,6,6])
#y=np.array([3,4,5,6,2,3,4])
#plt.plot(x,y,'r')
#plt.plot(x,y,'g',lw=10)


#小象学院_AI

############day_01
# 未来发展方向
# 1.数据分析 2.自然语言处理 3.社交网络分析 4.人工智能 5.深度学习 6.计算机视觉 7网络爬虫 8.量化交易

############day_02
# 计算机理论阐述：输入-处理-输出
# 确定问题-算法设计-算法实现-测试-验证

############day_03
# 1990年 guido van rossum设计开发
# 2000年10月 python2.0发布
# 2010年 python2.x发布，最后一班2.7-------遗产
# 2008年12月 python3.0发布-------未来的语言

############day_04
# 开发环境anaconda
# 集成开发环境-ide
# 查看函数的具体用法help('xxx')

############day_05
# pycharm

############day_06
# 汇率兑换

############day_07
# python基础语法解析
# 注释井号#，多行注释，三引号换行注释
#'''
#   author:wb
#   func:xxx
#   date:xxx
#'''

############day_08
# 汇率兑换2
# 切片a[x:y],得到的长度y-x

############day_09
# 汇率兑换3
# if and elif and else
# while

############day_10
# 汇率兑换4
# 结构化程序，封装函数，模块化函数
# 定义是形参，调用是实参

############day_11
# 汇率兑换5
# 简化代码
# if __name__ == '__main__':
#     xx()
# lambda

############day_12_13_14_15_16
# 绘制图形turtle库
# import turtle as tt 
# tt.forward(45)
# tt.right(144)
# tt.forward(50)
# tt.backward()
# tt.right()
# tt.exitonclick()
# tt.penup()
# tt.pendown()
# 递归函数，调用本身即递归
# import turtle as tt

# def rollback(size1,dg):       
# #    tt.penup()
#     tt.backward(size1)
# #    tt.pendown()
#     tt.left(dg*2)
#     tt.forward(size1)#画
# #    tt.penup()
# #    size1+=20

#     tt.backward(size1)
# #    tt.pendown()
#     tt.right(dg+10)
#     size1+=20

#     if size1<=100:
#         rollback(size1,dg)


# def draw(size,dg):
#     tt.right(dg)
#     tt.forward(size)
#     size-=20
#     if size >=60:
#         draw(size,dg)
# #    else:
# #        rollback(size,dg*2)

# def main():
#     #
#     size=100
#     dg=20
#     #
#     tt.left(90)
#     draw(size,dg)
#     rollback(60,dg*2)
#     tt.exitonclick()


# if __name__=='__main__':
#     main()

############day_17_18_19_20
# B分R计算器
# 数值类型
# 格式化输出
# 异常处理

############day_21_22_23_24_25
# 52周存钱挑战
# 全局变量，局域变量
# datetime.datetime
# 返回年、第几周、周几：datetime.datetime.isocalendar()
# 返回日期格式：datetime.datetime.strptime()
# 返回字符串：datetime.datetime.strftime()
# def test(i):
# 	im=10
# 	save=0
# 	if i == 1:
# 		return im+save
# 	else:
# 		return test(i-1)+10*(i-1)+10
# 	# yield save+im

# a=test(3)
# print(a)

############day_26_27_28_29
# 判断是第几天
# 元祖
# 元祖表示的是结构、列表表示的是顺序？
# 集合是无序可变

############day_30_31_32_33_34_35
# 判断密码强弱
# def x():
# 	def y():
# 		print('1')
# 	print('2')
# 	y()
# x()
# break是终止整个循环，continue是停止本次循环，剩下的继续
# 文件写入
# read()返回整个文件内容字符串,readline()返回下一行内容字符串,readlines()返回整个文件列表
# 面向过程pop：以程序执行过程为设计流程的变成思想
# 面向对象oop：以事物为中心的编程思想
# 现实世界中的对象：属性、行为

############day_36_37_38_39_40
# 模拟丢骰子
# 打乱列表的顺序：random.shuffle(list)
# 从指定列表获取K个元素：random.sample(list,k)
# import random as rd 
# l=list(range(100))
# rd.sample(l,8)
# print(rd.sample(l,8))
# print(l)
# 可视化matplotlib
# numpy

############day_41_42_43_44_45_46_47_48_49_50_51
# 空气质量指数
# lambda函数
# json格式读取写入
# csv格式写入
# 判断文件格式
# 网络爬虫
# from bs4 import BeautifulSoup
# pandas





####Numpy
#numpy.astype  数据类型转换  创建一个新的数组
#数组切片修改值时，原数组数据会自动更新
#数组递归访问[1][1]=[1,1]
#数组切片要产生新的数组时，需要使用.copy()



####pandas
#Series

#DataFrame

#解决pandas在读取中文CSV文件时，乱码问题encoding='GB2312'




####绘图和可视化matplotlib
##plot
#
#import matplotlib.pyplot as plt 
#
##plt.plot([11,12,13,14],[21,18,15,18],'r')
##plt.plot([11,12,13,14],[11,11,11,11],'g')
#x=[11,12,13,14]
#y=[21,18,15,18]
#y1=[11,12,10,14]
#plt.plot(x,y,x,y1,linewidth=5.0,color='#00e3e3')
#plt.title('weather')
#
#plt.axis([10,15,0,25])###图像显示范围
#
#plt.xlabel(u'日期')
#plt.ylabel('tmperture')
#
#
#plt.show()
import matplotlib.pyplot as plt
import pymongo as py
import pandas as pd
import pyecharts as pc
#window=py.MongoClient('localhost',27017)
#db=window['test']
#col=db['json']
#
#time_zone=['2016-01-01','2016-01-02','2016-01-03','2016-01-04','2016-01-05','2016-01-06','2016-01-07']
##time_zone=['2016-01-01']
#
#cellphone=[]
#laptop=[]
#computer=[]
##获取北京二手市场数据
#cellphone.append([i['pub_date'] for i in col.find() if '北京二手手机' in i['cates']])
#
##去掉不符合要求的日期
#cellphone=cellphone[0]
#cellphone_time=list(set(cellphone))
#
#for i in list(set(cellphone)):
#    if not i in time_zone:
#        cellphone_time.remove(i)
#cellphone_time.sort()
#
#cellphone_number=[]
#cellphone_number.append([cellphone.count(i) for i in cellphone_time])
#
#
##获取北京二手笔记本数据
#laptop.append([i['pub_date'] for i in col.find() if '北京二手笔记本' in i['cates']])
#laptop=laptop[0]
#laptop_time=list(set(laptop))
#
#for i in list(set(laptop)):
#    if not i in time_zone:
#        laptop_time.remove(i)
#laptop_time.sort()
#
#laptop_number=[]
#laptop_number.append([laptop.count(i) for i in laptop_time])
##
##获取北京二手电脑数据
#computer.append([i['pub_date'] for i in col.find() if '北京二手台式机' in i['cates']])
#computer=computer[0]
#computer_time=list(set(computer))
#
#for i in list(set(computer)):
#    if not i in time_zone:
#        computer_time.remove(i)
#computer_time.sort()
#
#computer_number=[]
#computer_number.append([computer.count(i) for i in computer_time])
#
#
##pyecharts可视化数据展示
#bar=pc.Bar('1','2')
#(bar.add('二手手机',cellphone_time,cellphone_number[0],is_stack=True)
#.add('二手笔记本',laptop_time,laptop_number[0],is_stack=True)
#.add('二手台式机',computer_time,computer_number[0],is_stack= True))
#
##line=pc.Line()
##line.add('title1',cellphone_time,cellphone_number[0])
#
#overlap=pc.Overlap()
#overlap.add(bar)
##overlap.add(line)
#
#overlap.render(r'D:\pyechart\view_seven.html')

#matplotlib可视化数据展示
#plt.rcParams['font.sans-serif'] = ['SimHei'] #设定字体，避免显示乱码
##画图
#plt.figure(figsize=(10,6))
#plt.plot(cellphone_time,cellphone_number[0],'r-',laptop_time,laptop_number[0],'g',computer_time,computer_number[0],'b')
##cellphone_time,cellphone_number[0],'r-',laptop_time,laptop_number[0],'g',
##展示
#plt.show()
a=[1,2,3,4,5]
b=sum(a)
print(b)
line=pc.Line('1','2')
line.add('3',[1,2,3],[3,4,5])
line
