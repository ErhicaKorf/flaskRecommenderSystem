
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
#load the data
movie_data = pd.read_csv('C:/Users/erhicakorf/Documents/GitHub/recommender-system/standard-project/movies_metadata.csv', low_memory=False)
movie_data = movie_data[0:20000]
movie_data.head()

movie_data['overview'].head(10)

tfidf_vector = TfidfVectorizer(stop_words='english')

movie_data['overview'] = movie_data['overview'].fillna('')

tfidf_matrix = tfidf_vector.fit_transform(movie_data['overview'])

from sklearn.metrics.pairwise import linear_kernel
sim_matrix = linear_kernel(tfidf_matrix, tfidf_matrix)

indices = pd.Series(movie_data.index, index=movie_data['title']).drop_duplicates()
indices[:10]

def content_based_recommender(title, sim_scores=sim_matrix):
    idx = indices[title]
    sim_scores = list(enumerate(sim_matrix[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    movie_indices = [i[0] for i in sim_scores]

    df_movies = pd.DataFrame(movie_data['title'].iloc[movie_indices])
    # print('df_movies',df_movies)
    data = {
            'movies': df_movies.to_json(orient='records')
        }
    return data


 

# content_based_recommender('Father of the Bride Part II')


