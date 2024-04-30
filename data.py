import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
#Split the date column in both datasets into separate "Year," "Month," and "Day" columns to facilitate data-based analysis.

df_tsv = pd.read_csv("FAL Projects NY - West SM.tsv", sep="\t", skiprows=9)

df_tsv[['Month', 'Day', 'Year']] = df_tsv['Create Date:'].str.replace('/', ' ').str.split(' ', n=1, expand=True).fillna('0')
df_tsv['Month'] = df_tsv['Month'].fillna('0')
df_tsv['Day'] = df_tsv['Day'].fillna('0')
df_tsv['Year'] = df_tsv['Year'].fillna('0')


# I know I am not done here, I didn't want to run out the clock


print(df_tsv.head().to_markdown(index=False, numalign="left", stralign="left"))
