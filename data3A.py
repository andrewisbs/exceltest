import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Read the CSV file into a DataFrame
df = pd.read_csv("Netflix_TV_Shows_and_Movies.csv")

# Display the first 5 rows
print(df.head().to_markdown(index=False, numalign="left", stralign="left"))

# Print the column names and their data types
print(df.info())
                  

# Get the count, mean and median of `imdb_votes`, `tmdb_popularity`, and `tmdb_score`
summary_stats = df[['imdb_votes', 'tmdb_popularity', 'tmdb_score']].describe().loc[['count', 'mean', '50%']]

# Rename the index for better readability
summary_stats.index = ['count', 'mean', 'median']

# Print the results
print(summary_stats.to_markdown(numalign="left", stralign="left"))
                  
                  