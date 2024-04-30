import pandas as pd

# Load the dataset
file_path = 'car_price_prediction.csv'
data = pd.read_csv(file_path)

# Preview the first few rows of the dataset
data.head(), data.info()


# Analysis of common manufacturers, price distribution, and fuel types

# Most common manufacturers
top_manufacturers = data['Manufacturer'].value_counts().head(10)

# Price distribution
price_description = data['Price'].describe()

# Fuel type distribution
fuel_type_distribution = data['Fuel type'].value_counts()

top_manufacturers, price_description, fuel_type_distribution
                  
