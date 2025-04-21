import csv

with open('sales_data.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row (optional)
    for row in reader:
        product, quantity, price = row
        print(f"Product: {product}, Quantity: {quantity}, Price: ${price}") 

"""sales_data.csv
Product,Quantity,Price
Apples,10,1.5
Bananas,5,0.75
Oranges,8,0.9
"""
