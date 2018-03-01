import pandas as pd
import datetime

movie_pd = pd.read_csv('douban_movie.csv', header=0, sep='\t')
new_movie_pd = movie_pd.drop(['category', 'rank'], axis = 1)
drop_indexes = movie_pd[ movie_pd['regions'] == '[意大利]' ].index
new_movie_pd = movie_pd.drop(drop_indexes)
new_movie_pd = movie_pd.drop(['category', 'rank'], axis = 1)
new_movie_pd = new_movie_pd.drop_duplicates()
print (len(new_movie_pd))
print (new_movie_pd['id'].nunique())
movie_count = new_movie_pd.groupby('id').size().reset_index(name='count')
print (movie_count[ movie_count['count'] > 1 ])

movie_level_list = list()
for i in movie_pd.index:
	score = movie_pd.loc[i, 'score']
	if score < 7.5:
		movie_level = 'B'
	elif 7.5 <= score < 9.0:
		movie_level = 'A'
	else:
		movie_level = 'S'
	movie_level_list.append(movie_level)
movie_pd['movie_level'] = pd.Series(movie_level_list)
print (movie_pd[['score', 'movie_level']].head())

movie_pd['release_date'] = pd.to_datetime(movie_pd['release_date'])
movie_pd['total_day'] = movie_pd['release_date'].map(lambda x: (datetime.datetime.now() - x).total_seconds() / (3600 * 24))
movie_pd['daily_vote'] = movie_pd['vote_count'] / movie_pd['total_day']
print (movie_pd[['release_date', 'total_day', 'vote_count', 'daily_vote']].head())