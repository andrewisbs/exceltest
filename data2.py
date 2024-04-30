import pandas as pd

# Load the dataset
file_path = 'car_price_prediction.csv'
data = pd.read_csv(file_path)

#👨:any interesting trends that you can share?
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
