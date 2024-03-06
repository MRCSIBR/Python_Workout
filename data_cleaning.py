import pandas as pd

# Load data from CSV file (replace 'your_data.csv' with your actual file)
data = pd.read_csv('your_data.csv')

# Check for missing values
print(data.isnull().sum())  # Shows count of missing values per column

# Fill missing values (e.g., with mean or median)
data['column_name'] = data['column_name'].fillna(data['column_name'].mean())

# Get descriptive statistics
print(data.describe())  # Shows summary statistics for numerical columns

# Check for duplicate entries
duplicates = data.duplicated().sum()
print(f"Number of duplicate rows: {duplicates}")

# Remove duplicates (optional)
# data = data.drop_duplicates()

# Visualize data distribution (using matplotlib)
import matplotlib.pyplot as plt

data['column_name'].hist()
plt.xlabel('column_name')
plt.ylabel('Frequency')
plt.title('Distribution of column_name')
plt.show()
