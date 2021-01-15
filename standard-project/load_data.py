
import pandas as pd
#load the data
movie_data = pd.read_csv('C:/Users/erhicakorf/Documents/GitHub/recommender-system/standard-project/movies_metadata.csv', low_memory=False)
movie_data = movie_data[0:20000]
movie_data.head()


movie_data['overview'].head(10)


