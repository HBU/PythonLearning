import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#http://blog.csdn.net/yifei301/article/details/77529840?locationNum=3&fps=1

df = pd.read_csv('douban.csv')

# 按照豆瓣评分排序，并查看排名前5的电影
print(df.sort_values('豆瓣评分', ascending=False).head())
print('---------------------------------------------------------')
# 豆瓣评分超过9.5分
print(df[df['豆瓣评分'] > 9.5])
print('---------------------------------------------------------')
# 上榜次数最多的导演们
print(df['导演'].value_counts())
print('---------------------------------------------------------')
print(df.describe())
print(df[['排名', '片名']].head(10))