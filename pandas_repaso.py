import pandas as pd

# Create a sample DataFrame
data = {'Name': ['John', 'Jane', 'Bob', 'Alice'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'London', 'Paris', 'Tokyo']}
df = pd.DataFrame(data)

# Select specific columns
selected_columns = df[['Name', 'Age']]
print(selected_columns)

# Filter data based on a condition
filtered_df = df[df['Age'] > 30]
print(filtered_df)

# Group data and calculate aggregations
grouped_df = df.groupby('City')['Age'].mean()
print(grouped_df)
