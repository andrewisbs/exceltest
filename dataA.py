import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Read the CSV file into a DataFrame
df_nyc_office = pd.read_excel('FAL Projects NY - office NY - FAL Proyectos.xlsx', skiprows=9)

# Read the TSV file into a DataFrame
df_west_sm = pd.read_csv('FAL Projects NY - West SM.tsv', sep='\t', skiprows=9)

# Display the first 5 rows
print(df_nyc_office.head().to_markdown(index=False, numalign="left", stralign="left"))
print(df_west_sm.head().to_markdown(index=False, numalign="left", stralign="left"))

# Print the column names and their data types
print(df_nyc_office.info())
print(df_west_sm.info())
                  



# ERROR ERROR ERROR
# Change the `Create Date:` column to datetime
# df_nyc_office['Create Date:'] = pd.to_datetime(df_nyc_office['Create Date:'])
# df_west_sm['Create Date:'] = pd.to_datetime(df_west_sm['Create Date:'])

# # Extract components from `Create Date:`
# for df in [df_nyc_office, df_west_sm]:
#   df['Year'] = df['Create Date:'].dt.year
#   df['Month'] = df['Create Date:'].dt.month_name().str[:3]
#   df['Day'] = df['Create Date:'].dt.day

# # Print the first 5 rows
# print(df_nyc_office[['Create Date:', 'Year', 'Month', 'Day']].head().to_markdown(index=False, numalign="left", stralign="left"))
# print(df_west_sm[['Create Date:', 'Year', 'Month', 'Day']].head().to_markdown(index=False, numalign="left", stralign="left"))
                  

import numpy as np

# Get all unique non-datetime values from `Create Date:`
non_datetime_date_value = df_west_sm[pd.to_datetime(df_west_sm['Create Date:'], errors='coerce').isna()]['Create Date:'].unique()

if (len(non_datetime_date_value) > 20):
  # Sample 20 of them if there are too many unique values
  print(f"Non-datetime values in Create Date: {np.random.choice(non_datetime_date_value, 20, replace=False)}")
else:
  # Otherwise print all unique non-datetime values from `Create Date:`
  print(f"Non-datetime values in Create Date: {non_datetime_date_value}")

# Convert `Create Date:` to datetime with format `%m/%d/%y`
df_west_sm['Create Date:'] = pd.to_datetime(df_west_sm['Create Date:'], format='%m/%d/%y', errors='coerce')

# Extract components from `Create Date:`
for df in [df_nyc_office, df_west_sm]:
  df['Year'] = df['Create Date:'].dt.year
  df['Month'] = df['Create Date:'].dt.month_name().str[:3]
  df['Day'] = df['Create Date:'].dt.day

# Print the first 5 rows
print(df_nyc_office[['Create Date:', 'Year', 'Month', 'Day']].head().to_markdown(index=False, numalign="left", stralign="left"))
print(df_west_sm[['Create Date:', 'Year', 'Month', 'Day']].head().to_markdown(index=False, numalign="left", stralign="left"))