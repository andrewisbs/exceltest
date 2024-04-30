import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Read the CSV file into a DataFrame
df = pd.read_csv("car_price_prediction.csv")

# Display the first 5 rows
print(df.head().to_markdown(index=False, numalign="left", stralign="left"))

# Print the column names and their data types
print(df.info())

# Replace '-' with '0' in `Levy` column
df['Levy'] = df['Levy'].astype(str).str.replace('-', '0', regex=False)

# Convert `Levy` to numeric
df['Levy'] = pd.to_numeric(df['Levy'])

# Replace ' Turbo' with '' in `Engine volume` column
df['Engine volume'] = df['Engine volume'].astype(str).str.replace(' Turbo', '', regex=False)

# Convert `Engine volume` to numeric
df['Engine volume'] = pd.to_numeric(df['Engine volume'])

# Replace ' km' with '' in `Mileage` column
df['Mileage'] = df['Mileage'].astype(str).str.replace(' km', '', regex=False)

# Convert `Mileage` to numeric
df['Mileage'] = pd.to_numeric(df['Mileage'])

# Select the columns for correlation calculation
columns_for_correlation = ['Prod. year', 'Mileage', 'Cylinders', 'Airbags', 'Levy', 'Engine volume']

# Calculate the correlation between `Price` and selected columns
correlations = df[['Price'] + columns_for_correlation].corr()['Price']

# Print the correlations
print(correlations.to_markdown(numalign="left", stralign="left"))