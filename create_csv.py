import csv

# Data from the original code
data = [
    ['Set', 'Venda Consinco', 'Venda App', 'Diferenca C5xApp', 'Percentual Dif C5xApp'],
    ['Set 1', 3641017.37, 3623222.88, 17794.49, 0.49],
    ['Set 2', 11538695.95, 11333705.72, 204990.23, 1.78],
    ['Set 3', 3744004.17, 3719142.68, 24861.49, 0.66]
]

# Write data to CSV file
with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("data.csv file has been created successfully.")
