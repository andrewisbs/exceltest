import pandas as pd

# Load the first dataset (TSV file)
df1 = pd.read_csv('FAL Projects NY - West SM.tsv', sep='\t')

# Load the second dataset (Excel file)
df2 = pd.read_excel('FAL Projects NY - office NY - FAL Proyectos.xlsx')

# Check the first few rows of both datasets to understand their structures
df1.head(), df2.head()
                  


# Attempt to skip the initial metadata and locate the actual data in both datasets
# This step involves guessing the starting row of the data based on the structure seen above

# For the TSV file, let's try skipping the first 10 rows (as an initial guess)
df1_data_start_guess = pd.read_csv('FAL Projects NY - West SM.tsv', sep='\t', skiprows=10)

# For the Excel file, let's also try skipping the first 10 rows
df2_data_start_guess = pd.read_excel('FAL Projects NY - office NY - FAL Proyectos.xlsx', skiprows=10)

# Preview to find the data sections and the 'Date' column if present
df1_data_start_guess.head(), df2_data_start_guess.head()


# For the first dataset, let's assume the second column is the date column based on the preview
df1_date_column = pd.to_datetime(df1_data_start_guess.iloc[:, 1], errors='coerce')  # Handle non-date entries safely
df1_data_start_guess['Year'] = df1_date_column.dt.year
df1_data_start_guess['Month'] = df1_date_column.dt.month
df1_data_start_guess['Day'] = df1_date_column.dt.day

# For the second dataset, the date column is the second column as well based on the preview
df2_date_column = pd.to_datetime(df2_data_start_guess.iloc[:, 1], errors='coerce')  # Handle non-date entries safely
df2_data_start_guess['Year'] = df2_date_column.dt.year
df2_data_start_guess['Month'] = df2_date_column.dt.month
df2_data_start_guess['Day'] = df2_date_column.dt.day

# Preview the results after splitting
print(df1_data_start_guess[['Year', 'Month', 'Day']].head(), df2_data_start_guess[['Year', 'Month', 'Day']].head())