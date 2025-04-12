from dictionary import add_inventory, remove_inventory

inventory = {'Widget1' : 10, 'Widget2' : 20}

def display_menu():
    print('1 - ADD OR UPDATE ITEM')
    print('2 - DELETE ITEM')
    print('3 - EXIT')

def run_menu():
    user_option = '0'

    while(user_option != '3'):
        display_menu()

        user_option = input("ENTER A MENU OPTION(1, 2, 3): ")
        handle_menu(user_option)

def handle_menu(user_option):
    if(user_option == '1'):
        widget = str(input('ENTER YOUR WIDGET NAME: '))
        quantity = int(input('ENTER THE QUANTITY OF WIDGETS: '))

        add_inventory(inventory, widget, quantity)

        print('HERE IS THE CURRENT DICTIONARY:' )
        print(inventory)

    elif(user_option == '2'):
        widget = str(input('ENTER THE WIDGET NAME YOU WOULD LIKE TO REMOVE: '))

        remove_inventory(inventory, widget)

        print('HERE IS THE CURRENT INVENTORY:')
        print(inventory)

    elif(user_option == '3'):
        print('EXITING ...')

    else:
        print('INVALID INPUT')

run_menu()