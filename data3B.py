import pandas as pd

# Load the dataset to get an overview of its structure and contents
file_path = 'Netflix_TV_Shows_and_Movies.csv'
netflix_data = pd.read_csv(file_path)

# Display basic information about the dataset and the first few rows to understand its structure and contents
netflix_data_info = netflix_data.info()
netflix_data_head = netflix_data.head()

(netflix_data_info, netflix_data_head)