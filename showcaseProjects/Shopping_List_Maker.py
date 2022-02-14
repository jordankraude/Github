#Needed variables and definitions before
from numpy import true_divide
from validaterClass import validater
validater = validater()

def main():
    shopping_list = []
    food_item = None
    shopping_price_total = []
    shopping_price_total_string = []
    item_price = None
    another_item = None
    z = -1
    running = True
    main_menu = ['1. Add a new item', '2. Display the contents of the shopping cart',
    '3. Remove an item', '4. Compute the total', '5. Checkout']

    print ('Hello there! This is the main menu. Please select one of the following: ')
    print('')

    #Loop to keep the custumer in the program if they don't choose to quit
    while running is True:
        for item in main_menu:
            print(item)
        
        try:
            valid = False
            while not valid:
                main_menu_choice = int(input('Please enter an action: '))
                print('')
                if main_menu_choice >= 1 and main_menu_choice <= 5:
                    valid = True
                else:
                    print('Please enter a number between 1 and 5:')
        except:
            print('That is an invalid input')

    #Choice 1. If they choose number 1 to add a item
        if main_menu_choice == 1:
            while another_item != "no":
                food_item = input('What item would you like to add? ')
                item_price = float(input(f'What is the price of {food_item}? '))
                capitalized_food_item = food_item.capitalize()
                print(f'{capitalized_food_item} has been added to the cart. ')

    #Variable Z to store the max range of items
                z = z + 1

                item_price_final = (f'{item_price:.2f}')

                shopping_list.append(capitalized_food_item)
                shopping_price_total_string.append(item_price_final)
                shopping_price_total.append(item_price)


                another_item = validater.validate_input('Do you want to add another item? ', "Y/N")  
            print('')

    #Choice 2. If they want to see their cart
        elif main_menu_choice == 2:

            print ('The items in your cart include: ')
            for i in range(len(shopping_list)):
                complete_shopping_list = shopping_list[i]
                complete_shopping_total= shopping_price_total_string[i]

                print(f'{i+1}.{complete_shopping_list} - ${shopping_price_total_string[i]}')
            print('')

    #Choice 3. If they want to remove a item
        elif main_menu_choice == 3:
            for i in range(len(shopping_list)):
                complete_shopping_list = shopping_list[i]
                print(f'{i+1}. {complete_shopping_list}')
                
    #Create a index
            y = int(input('Here are the items in your cart. Which item would you'
            ' like to remove? Please enter one of the item numbers: '))
            a = y - 1

    #Make sure their choice is actually something they can remove
            if a <= z:

                user_choice_removal = shopping_list[a]
                shopping_list.pop(a)
                
                print(f'{user_choice_removal} has been removed.')
                print('')

                z = z - 1

            else:
                print('Invalid choice.')
                print('')

    #Choice 4. If they would like to see the total of all of their items
        elif main_menu_choice == 4:

            total_sum = sum(shopping_price_total)
            print (f'The total price of the items in the shopping cart is {total_sum:.2f}')
            print('')
        
        elif main_menu_choice == 5:
            running = False
        #Out of the loop, show the cart items and prices with the total
            print('Have a great day! We hope you shop with us again')

        else:
            print('Invalid Choice')



main()
