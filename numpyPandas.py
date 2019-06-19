###########chapter_01_准备工作
# 利用python进行数据控制、处理、整理、分析
# 结构化数据：表格型数据、多维数组、关键列、序列
# Numpy：快速高效的多维数组对象ndarray、对数组执行元素级计算以及对数组执行数学运算的函数、用于读写硬盘上基于数组的数据集的工具、线性代数运算、傅里叶变换、随机数生成、在算法和库之间传递数据的容器
# Pandas：快速便捷处理结构化数据的大量数据结构和函数(用的最多的对象DataFrame)、提供复杂精细的索引功能、能更加敏捷的完成重塑、切片和切块、聚合以及选取数据子集等操作
# Ipython："执行-探索"的交互工具，tab补全，保存历史命令，可以执行shell命令，断点调试，命令提示符进行编号，？显示对象签名和文档字符串和代码位置，？？显示源代码
# Scipy：解决科学计算中各种标准问题域的包的集合
# Scikit-learn：通用机器学习工具包
# Statsmodels：包含经典统计学和经济计量学的算法
# python_Ide：Pydev、Pycharm、VisualStudio、Spyder、KomodoIde
# 社区：pydata、pystatsmodels、scikit-learn@python.org、numpy-discussion、scipy-user
# 工作分类：读文件和数据存储；数据分析；转换数据；建模和计算；可视化展示
# 数据规整(munge)：将非结构化和散乱数据处理为结构化或整洁形式的整个过程
# 伪码算法或者过程的"代码式"描述
# 语法糖：编程语法，只会让代码更加易读、易写

###########chapter_02_page(8)_python语法基础
# python_cookbook,流畅的python,高效的python

###########chapter_03_page(31)_python的数据结构、函数和文件
# 拆分：tup=(1,2,3,4,5)  a,b,*rest=tup
# 排序：List.sort(key=len)
# 二分查找bisect(已排序)：bisect.bisect(list,value)找到插入值插入后的位置，bisect.insort(list,value)向已排序的列表插入到对应位置
# zip函数处理的函数取决于最短的序列
# zip可以解压被压缩的序列：x,y=zip(*nrange_list)
# 字典的值可以是任意类型python对象，而键通常是不可变的，这个称为"可哈希性"(hash())
# 嵌套列表推导式：[i for ii in x for i in ii if i>0 ] 或者 [[x for x in j] for j in tup]
# lambda是匿名函数的原因：函数对象本身没有__name__属性
# try:xxx except:xxx finally:xxx(finally总会被执行)
# with open(path) as f: 会在代码执行完成自动关闭文件

###########chapter_04_page(56)_Numpy基础:数组和矢量计算
# numpy：1.ndrray多维数组 2.用于对整组数据进行快速运算的标准数学函数 3.用于读写磁盘数据的工具 4.线性代数、随机数生成等 5.集成c、c++等代码api
# numpy功能：1.数据整理和清理 2.常用的数组算法、排序、唯一化、集合运算 3.高效的描述统计和聚合摘要运算 4.异构数据集的合并/连接运算的数据对齐和关系型数据运算 5.将条件逻辑表述未数组表达式 6.数据的分组运算
# numpy算法要比纯python快10-100倍！！！！
# 创建数组的方式：np.array(list)或者np.arange(15).reshape((3,5))接受一切序列型对象
# nddray.astype(np.int)数据类型转换
# nddray.T数组转置
# 未完,待续

###########chapter_05_page(85)_pandas入门
# pandas:数据清洗和分析工作变得更快更简单的数据结构和操作工具
# pandas是基于numpy数组构建的
# pandas为处理表格和混杂数据设计,numpy更适合处理统一的数值数组数据
# pd.series是一种类似于一维数组的对象，由一组数据(各种numpy数据类型)以及一组与之相关的数据标签(即索引)组成
# x=pd.Series(list,index=list), x.values ,x.index
# x=pd.Series(dict):字典的键是索引，值是值
# 条件查询：x[条件](x[x>0])
# pd.isnull(obj);pd.notnull(obj)
# obj.isnull();obj.notnull()
# Series最重要的一个功能是：根据运算的索引标签自动对齐数据
# Series自带name以及index.name,默认为空,进行赋值后才会显示
#
# DataFrame:表格型的数据结构，它含有一组有序的列，每列可以是不同的值类型
# DataFrame既有行索引也有列索引，可以看成由Series组成的字典(共用同一个索引)，数据是以一个或多个二维块存放的
# frame=pd.DataFrame(data)：直接传入一个由等长列表或numpy数组组成的字典
# frame.head():选取前5行数据进行展示
# frame=pd.DataFrame(data，columns=['x','y','z'])：按照执行顺序进行排列
# frame=pd.DataFrame(data,columns=['x','y','z'],index=['a','b','c'])：如果传入索引或者列不存在就会显示为缺失值
# 访问数据的方式：frame['attribute'] 或者 frame.attribute
# frame.loc[index]
# del frame['columns']:只能用这种方式
# 转置：frame.T
# frame.index.name=x;frame.columns.name=y
# frame.values;frame.index
# index对象是不可变的,但是可以重新赋值obj.reindex([list]):list可以比原index大,但是索引名称不存在则所有条目显示为NAN
# 删除行：obj.drop(index_name),obj.drop([index_name1,index_name2])
# 删除列：obj.drop(column_name,axis=列索引),obj.drop(column_name,axis='columns')
# 条件查询：obj[条件](obj[obj>3])
# 转换数据类型：obj=obj.astype('int')-------数据只有一列时
# 按行查询：obj.loc[行索引,[按输入顺序显示列]];obj.iloc[行数字索引]
# 标签运算符loc和iloc：使用轴标签(loc)和整数索引(iloc)
# obj[val]：通过标签，选取单列或一组列
# obj.loc[val]：通过标签，选取单个行或一组行
# obj.loc[:,val]：通过标签，选取单列或列子集
# obj.loc[val1,val2]：通过标签，同时选取行和列
# obj.iloc[where]：通过整数位置，选取单个行或行子集
# obj.iloc[:,where]：通过整数位置，选取单个列或列子集
# obj.iloc[wherei,wherej]：通过整数位置，同时选取行和列
# obj.at[vali,valj]：通过行和列标签，选取单一的标量
# obj.iat[vali,valj]：通过行和列标签(整数)，选取单一的标量
# 对行和列索引进行重新排序：obj.sort_index(ascending=True);obj.sort_index(axis=1)
# 对单一列进行排序：obj.sort_values(by='column_name')
# 对数据进行排名：newchart.rank(ascending=False)
# 对数据所有列进行求和：obj.sum()
# 对数据所有列进行求平均数：obj.mean()
# 通过重新指定索引，来进行填充值：注意因为索引值不可变的，所以如果重新赋值索引时，以前的索引值和现在不一直，则全部显示为NAN
# 查询最大值的行索引号(数值型数据)：obj.idxmax(),obj.idxmin()
# 汇总统计：obj.describe()
# 最大值、最小值：obj.min(),obj.max(),obj.sum(),obj.mean()
# 计算series中唯一值：series.unique()
# 计算series一组数据中数据的出现频率：pd.value_counts()
# DataFrame补充缺失值：obj.fillna(value)

###########chapter_06_page(116)_数据加载、存储与文件格式
# 输入输出划分为：读取文本文件和其他更高效的磁盘存储格式，加载数据库中的数据，利用WEB API操作网络资源
# pandas读取文件函数功能分类：1. 索引 2.类型推断和数据转换 3.日期解析 4.迭代 5.不规整数据问题
# pd.read_csv(pwd,encoding=?,names=列名list,index_col=某一列,skiprows=list)
# pd.read_json(),pd.read_excel()
# pd.options.display.max_rows=int;pd.read_csv(nrows=10)
# data.to_csv(pwd,encoding=用什么解码，就用什么编码)

###########chapter_07_page(133)_数据清洗和准备
# 查询缺失数据：data.isnull()
# 滤除缺失数据(只要包含NA就丢弃,不对原数据进行修改)：data.dropna()等价于data[data.notnull()];除非data.dropna(0,inplace=True)
# 滤除缺失数据(单行所有列都是NA就丢弃)：data.dropna(how='all')
# 滤除缺失数据(单列所有行都是NA就丢弃)：data.dropna(axis=1,how='all')
# 填充缺失数据：data.fillna(0)不会对原数据进行修改;除非data.fillna(0,inplace=True)
# 移除重复数据(DataFrame)：data.drop_duplicates();data.drop_duplicates([列名])
# 替换值：data.replace(before_value,after_value,inplace=True)
# 重命名轴索引：data.index=list;data.index=data.index.map(lambda函数);data.rename(index=dict,columns=dict,inplace=true)
# 离散化和面元划分：将数据按照区间展示出来pd.cut(listobj,区间list)
# np.random.randint(4,high=10,size=(2,3))
# 随机取样：data.sample(n=3)

###########chapter_08_page(154)_数据规整:聚合、合并、重塑
# 层次化索引:....index=[list1,list2]
# 重排与分级排序：frame.swaplevel()
# 根据级别汇总统计：frame.sum()
# 使用dataframe的列进行索引：obj.set_index(['name1','name2'])
# 使用列索引后复原：obj.reset_index()
# 合并数据集(两个obj必须有相同的列数据才能进行合并)：pd.merge(obj1,obj2)
# 索引上的合并：pd.merge(obj1,obj2,left_on=...,right_index=True)
# 轴向连接：pd.concat([obj1,obj2])
# 合并重叠数据：np.where()
# 重塑和轴向旋转：obj.stack()将数据的列转为行，obj.unstack()将数据的行转为列
# 将长格式旋转为宽格式？
# 将宽格式旋转为长格式？

###########chapter_08_page(176)_绘图和可视化

import pymongo as py
import pandas as pd
import numpy as np

window=py.MongoClient('localhost',27017)
db=window.oldhouse
table=db.newData190513

# test=pd.DataFrame(table.find().limit(5))
test=pd.DataFrame(np.arange(10).reshape(2,5),index=['0','1'],columns=['meter_price','develop','a','test','c'])
test1=pd.DataFrame(np.arange(10).reshape(5,2),index=['0','1','2','3','4'],columns=['meter_price','test'])
# print(test)
# print(test1)
# test.index=test['area','village']
# print(test)
pd.options.display.max_rows=3000
# newt=test.sort_values(by=['area','village'])
# test['village']=test['village'].astype('str')
# a=test['village'][1]
print(test1)
print(test.stack())
print(test1.unstack())
# test.drop('_id',axis=1,inplace=True)
# test.set_index(['area','village'],inplace=True)
# print(test.sort_index())
# print(test.reset_index())
# print(newt[newt['village']==r'合能耀之城'])
# test['meter_price']=test['meter_price'].astype('int')
# # test.drop(2,inplace=True)
# test.loc[10]=[1,2,3,4,5,6]
# test.drop(test['meter_price'][2],inplace=True)
# print(test)
# # print(test['meter_price'].idxmax())
# print(test.loc[95])
# print(test[test['meter_price']>10000])