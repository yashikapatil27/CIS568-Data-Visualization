import pandas as pd

# Load the data from the CSV file
file_path = '/Users/yashika/Desktop/vz/data_sample.csv'
df = pd.read_csv(file_path)

# Calculate the ActualCost, SoldPrice, and MarginOfProfit using the correct column names
df['ActualCost'] = df['RawMaterial'] + df['Workmanship'] + df['StorageCost']
df['SoldPrice'] = df['EstimatedCost'] * 1.1
df['MarginOfProfit'] = df['SoldPrice'] - df['ActualCost']

# Select columns
df_final = df[['date', 'EstimatedCost', 'RawMaterial', 'Workmanship', 'StorageCost', 'ActualCost', 'SoldPrice', 'MarginOfProfit']]

# Save the final table to a new CSV
df_final.to_csv('/Users/yashika/Desktop/vz/table.csv', index=False)

# Display the table 
print(df_final)
