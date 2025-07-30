import pandas as pd

movie_df = pd.read_csv(r'DataSets/movies.csv')
rating_df = pd.read_csv(r'DataSets/ratings.csv')

# print(movie_df.head())
# print(rating_df.head())

df = pd.merge(rating_df, movie_df, on='movieId')

ratings_summary = pd.DataFrame(df.groupby('title')['rating'].mean())
ratings_summary['number_of_ratings'] = df.groupby('title')['rating'].count()

movie_matrix = df.pivot_table(index='userId', columns='title', values='rating')


#Handle null values
movie_matrix.fillna(0, inplace=True)

#Star Wars
toy_story_rating = movie_matrix['Toy Story (1995)']


similar_to_toy_story = movie_matrix.corrwith(toy_story_rating)

# print(similar_to_toy_story.head())
corr_df = pd.DataFrame(similar_to_toy_story, columns=['Correlation'])
corr_df.dropna(inplace=True)

corr_df = corr_df.join(ratings_summary['number_of_ratings'])

final_recommendation = corr_df[corr_df['number_of_ratings'] > 100].sort_values('Correlation', ascending=False)

print("---Recommendation for Toy Story (1995) ---")
print(final_recommendation.head(10))