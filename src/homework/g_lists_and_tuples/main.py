from lists import get_highest_list_value, get_lowest_list_value

def display_menu():
        print('1-SHOW THE LIST LOW/HIGH VALUES')
        print('2-EXIT')

def run_menu():
    user_option = '0'

    while(user_option != '2'):
        display_menu()

        user_option = input("Enter a menu option(1 or 2): ")
        handle_menu(user_option)

def handle_menu(user_option):
    if(user_option == '1'): 
        inputlist = [] 

        again = 'Y'

        for i in range(3):
             ent = int(input('Enter a number: '))
             inputlist.append(ent)

        again = input('Would you like to enter another number? Y/N ')

        while again =='Y' or again == 'y':
             ent=int(input('Enter another number: '))
             inputlist.append(ent)
             

             again = input('Would you like to enter another number? Y/N ')
        
        high = get_highest_list_value(inputlist)
        low = get_lowest_list_value(inputlist)

        print(f'The highest value is {high}')
        print(f'The lowest value is {low}')
        print()

             
    elif(user_option == '2'):
        print('EXITING ...')

    else:
        print("TRY AGAIN")

run_menu()