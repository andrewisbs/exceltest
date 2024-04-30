import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Read the CSV file into a DataFrame
df = pd.read_csv("DATA_ECOM_VAS_v1-.xlsx-Grossreport.csv")

# Display the first 5 rows
print(df.head().to_markdown(index=False, numalign="left", stralign="left"))

# Print the column names and their data types
print(df.info())

# Get the frequency of different values in `Payment System Name`
payment_frequency = df['Payment System Name'].value_counts()

# Pick the top most frequent value
top_payment_method = payment_frequency.index[0]

# Print the result
print(f"Most frequent payment method: {top_payment_method}")