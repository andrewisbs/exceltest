import pandas as pd


file_path = 'RAP_Journal_Engagement.csv'
data = pd.read_csv(file_path)

# NOTE: I am just outputing what I need to know to review
#I have all the stats in the terminal, enough to evaluate the response.
data.head()
print(data.columns.to_list())




for column in data.columns:
    
    print("Column:", column)
    print("Data type:", data[column].dtype)
    print("Non-null count:", data[column].count())
    print("Unique values:", data[column].unique()[:5])
    
    value_counts_data = data[column].value_counts()
    print(value_counts_data)
    if pd.api.types.is_numeric_dtype(data[column]):
        print("Summary statistics:")
        print(data[column].describe())
    
    print("\n")


file_path = 'RAP_Journal_Engagement.csv'
data = pd.read_csv(file_path)
data.head()
data.columns.to_list()

payment_method_counts = data['Region'].describe()
print(payment_method_counts)

import pandas as pd
import matplotlib.pyplot as plt

# Read the Excel file into a DataFrame
df_graph = pd.read_csv('RAP_Journal_Engagement.csv')

# Assuming the first column is 'Region' and the second column is 'Amount'
# Replace 'Region' and 'Amount' with your actual column names
region_column = df_graph['Region']
amount_column = df_graph['Engaged sessions per user']

# Plotting the data
plt.figure(figsize=(10, 6))
plt.bar(region_column, amount_column, color='skyblue')
plt.xlabel('Region')
plt.ylabel('Engagement')
plt.title('Amount by Region')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to prevent overlapping labels
plt.show()

