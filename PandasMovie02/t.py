import pandas as pd
#https://zhuanlan.zhihu.com/p/29686957
movie_pd = pd.read_csv('douban_movie.csv', header = 0, sep = '\t')
print (type(movie_pd))
# 按列创建
temp_dict =  {
        'score':  [ 8.9, 8.2, 9.3 ],
        'category': ['悬疑', '动作', '爱情']
    }
temp_pd = pd.DataFrame(temp_dict)
print (temp_pd)
# 按行创建
row1 = [8.9, '悬疑' ]
row2 = [8.2, '动作']
row3 = [9.3, '爱情' ]
temp_pd = pd.DataFrame([ row1, row2, row3 ], columns = ['score', 'category'])
print (temp_pd)

print (len(temp_pd))#默认的索引都是从 0 ~ N-1 的数字，其中 N 为 DataFrame 的长度，可以使用 len( ) 来获取
print ('index:')
print (temp_pd.index)
temp_pd.index = ['movie_1', 'movie_2', 'movie_3']# index 可以获取 DataFrame 的索引
print ('colums:' )
print(temp_pd.columns)
temp_pd.columns = ['movie_score', 'movie_category']# columns 可以获取 DataFrame 的列名
print('----------')
print (temp_pd)
print('----------')
print (temp_pd.values)#values 则可以获取 DataFrame 的值
#================================================================================#
#https://zhuanlan.zhihu.com/p/30100954
# loc( ) 按照索引筛选数据
# Series DataFrame 中某一行或某一列的数据类型
# & 和 | 多条件筛选时 同时满足 和 只满足其一即可
# isnull( ) 空值、notnull( ) 非空值、isin( ) 值在给定列表中

# 按一行或多行筛选
# 使用非常好用的 loc( ) 函数，可以按照索引进行筛选
movie_pd = pd.read_csv('douban_movie.csv', header = 0, sep = '\t')
print (movie_pd.loc[0])
print (movie_pd.loc[range(10)])
print (movie_pd.loc[[1, 3, 8]])
#loc( ) 函数既可以传入某个索引值，也可以传入索引值的列表，
# 一般情况下，DataFrame 的索引值是 0 ～ N-1 的数字 ( 其中 N 为 DataFrame的长度 )。
# 所以，loc[0] 查询的其实是第一行的数据，loc[range(10)] 查询的是前 10 行的数据，
# (而 loc[[1, 3, 8]]则是跳着查询第 2、4、9 行的数据。

# 按一列或多列筛选
# 按列筛选就比较简单了，不需要用到什么函数，直接筛就可以，简单粗暴。
# 比如说筛选电影数据的标题 title 和 评分 score 中的一列或两列：

print (movie_pd['title'])
print (movie_pd[ ['title', 'score'] ])

# 按一行一列或多行多列同时筛选
# 也是借助 loc( ) 函数，但这个时候需要通过传入两个参数。

print (movie_pd.loc[5, 'actors'])
print (movie_pd.loc[[1, 5, 8], ['title', 'actors'] ])

print (movie_pd['title'])#带有一个中括号的类型是 Series，带有两个中括号的类型是 DataFrame。
print (movie_pd[['title']])#带有一个中括号的类型是 Series，带有两个中括号的类型是 DataFrame。

# 筛选电影类型是剧情的 title 和 score 两列
print (movie_pd[ movie_pd['category'] == '剧情' ][['title', 'score']])

# 筛选电影排名小于等于 5 且评分高于 9.0 的 title 一列
print (movie_pd[ (movie_pd['rank'] <=5) & (movie_pd['score'] > 9.0) ][['title']])
print('--------------------------------------------------------------------------')
# 筛选电影发布日期大于 2010-01-01 或 评论数超过 50万 的所有列
print (movie_pd[ (movie_pd['release_date'] > '2010-01-01') | (movie_pd['vote_count'] > 500000) ])
print('----------')
print (movie_pd[ movie_pd['url'].isnull() ])
print('----------')
print (movie_pd[ movie_pd['regions'].notnull() ])
print('----------')
print (movie_pd[ movie_pd['score'].isin([8.0, 9.0, 9.5]) ])#isin( ) 函数：筛选某个字段的值在给定列表中