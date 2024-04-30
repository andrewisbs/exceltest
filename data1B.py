import pandas as pd

# Load the dataset
file_path = 'DATA_ECOM_VAS_v1-.xlsx-Grossreport.csv'
data = pd.read_csv(file_path)

# Display the first few rows to understand the structure
data.head()
data.columns.to_list()

# Analyze the 'Payment System Name' column to find the most used payment method
payment_method_counts = data['Payment System Name'].value_counts()
print(payment_method_counts)
