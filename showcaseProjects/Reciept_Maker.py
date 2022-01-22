'''
03-04 Prove Asignment
Jordan Kraude
CSE 111
1/25/2021

Purpose: To make a receipt excercising knowledge in dictionarys and functions
'''


#Prep work
import csv
import datetime
import time

x = 0 
subtotal = 0

# Get the current date and time from the operating system.
# and change it into strife time format
now = datetime.datetime.now()
strife_time_format = now.strftime('%c')

# Create dictionary
products = {}

# Open the file products (supplied by the store)
with open('products.csv') as infile1:
    products_reader = csv.reader(infile1)

    # Skip the first line in products because it is no bueno
    next(products_reader)

    # Store the rows in the products into variables
    for row in products_reader:
        product_number = row[0]
        product_name = row[1]
        price = float(row[2])

        # store the variables of products into a dictionary with the product
        # number as the key
        products[product_number] = product_name, price

# I mean this works haha, and I can do this. I don't think it really matters but
# this is just easier to print the Inkom Emporium up here to make sure the format
# is 100 percent the same. I don't want to put it into the loop and what I did to print
# the receipt exactly how it was formated needs to be in the loop
print('Inkom Emporium')
print('')

receipt = {}
# For the code to work exactly as required the file inside would need to be a variable with the
# name changing to whatever the computer supplied from the customer
with open ('request.csv') as infile2:
    request_reader = csv.reader(infile2)
    next(request_reader)

    for row in request_reader:
        # Store the info of the receipt into variables
        requested_product = row[0]
        quantity_of_product = int(row[1])
        # Code to keep track of the amount of items ("row[1]" is the qunatity of product)
        x += int(row[1])

        # Exchange the requested items into the products dictionary key
        requested_items = products[requested_product]

        # Put the desired info into the dictionary for the receipt
        receipt[requested_product] = requested_items[0], quantity_of_product, requested_items[1]

        # As I said earlier, it is easier to have the correct format by doing this. I think 
        # this should be alright. If not we can just say I was being creative
        print(f'{requested_items[0]}: {quantity_of_product} @ {requested_items[1]:.2f}')

        # Code finding the requested item from the products dictionary and multiplying
        # it by the amount desired. (The subtotal is added because that is needed
        # or else the subtotal would only hold the value of one item times its desired quantity
        subtotal += quantity_of_product * requested_items[1]
        
# Code to take the subtotal and multiply it by the sales tax
sales_tax = subtotal * 0.06
# Code to find the total with the tax
total = sales_tax + subtotal

# The final print statements for the formatting
print('')
print(f'Number of items: {x}')
print(f'Subtotal: {subtotal:.2f}')
print(f'Sales Tax: {sales_tax:.2f}')
print(f'Total: {total:.2f}')
print('')
print('Thank you for shopping at the Inkom Emporium.')
print(strife_time_format)