# https://zhuanlan.zhihu.com/p/29324349

import pandas as pd

movie_pd = pd.read_csv('douban_movie.csv', header = 0, sep = '\t')#pd.read_csv( ) 负责把 csv 文件读入
print (movie_pd.info())# info( ) 查看数据有哪些字段和字段对应的数据类型
print (movie_pd.describe())# describe( ) 对数值型变量进行统计性描述
print (movie_pd.head())# head( n ) 显示数据前 n 行,n默认为5
print (movie_pd.tail())# tail( n ) 显示数据后 n 行




