import pandas as pd

movie_df = pd.read_csv(r'D:\PythonForAIML\DataSets\movies.csv')
rating_df = pd.read_csv(r'D:\PythonForAIML\DataSets\ratings.csv')

# print(movie_df.head())
# print(rating_df.head())

df = pd.merge(rating_df, movie_df, on='movieId')

movie_matrix = df.pivot_table(index='userId', columns='title', values='rating')

print(movie_matrix.head())