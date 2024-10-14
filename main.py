import matplotlib.pyplot as plt
import pandas as pd

# Read data from CSV file
df = pd.read_csv('data.csv')

# Extract data from the DataFrame
columns = df.columns[1:].tolist()
data = {}

for column in columns:
    data[column.lower().replace(' ', '_')] = df[column].tolist()

# Create a bar chart for all numeric columns
x_labels = df['Set'].tolist()
x = range(len(x_labels))

plt.figure(figsize=(12, 6))

# Dynamically create bar chart for all numeric columns
bar_width = 0.35
num_columns = len(columns)
offsets = [i * bar_width - (num_columns - 1) * bar_width / 2 for i in range(num_columns)]

for i, column in enumerate(columns):
    column_key = column.lower().replace(' ', '_')
    if df[column].dtype in ['int64', 'float64']:
        plt.bar([xi + offsets[i] for xi in x], data[column_key], width=bar_width, label=column, align='center')

plt.xlabel('Data Sets')
plt.ylabel('Value')
plt.title('Comparison of All Numeric Columns')
plt.xticks(x, x_labels)
plt.legend()
plt.tight_layout()
plt.legend()

# Show the plot
plt.tight_layout()
plt.show()
