import pandas as pd
import numpy as np

movie_pd = pd.read_csv('douban_movie.csv', header=0, sep='\t')

print(movie_pd.groupby('category').size().reset_index(name = 'num'))

# agg_pd = movie_pd.groupby('id').agg({
# 	'score': [ np.max, np.min ], 'vote_count': np.mean
# }).reset_index()
# print(agg_pd.columns)
# for temp in agg_pd.columns:
# 	print(temp)

print (movie_pd.groupby(['category', 'id']).agg({
	'score': np.mean, 'vote_count': np.mean
}).reset_index().sort_values('score', ascending = False))