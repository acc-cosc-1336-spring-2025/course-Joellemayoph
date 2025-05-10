from class_a import Die

def main():
    #object 
    my_die = Die()

    print('The dice is on: ', my_die.get_rolled_value())

    print('I am tossing the dice...')

    my_die.roll()

    print('You rolled:', my_die.get_rolled_value())

def display_menu():
    print('1 - ROLL DICE')
    print('2 - EXIT')

def run_menu():
    user_option = '0'

    while(user_option != '2'):
        display_menu()

        user_option = input("ENTER A MENU OPTION(1 or 2): ")
        handle_menu(user_option)

def handle_menu(user_option):
    if(user_option == '1'):
        main()
        
        user_option1 = input('WOULD YOU LIKE TO ROLL AGAIN? (Y/N): ')
        
        while(user_option1 == 'Y'):
            main()

            user_option1 = input('WOULD YOU LIKE TO ROLL AGAIN? (Y/N): ')

    elif(user_option == '2'):
        print('EXITING ...')

    else:
        print('INVALID INPUT')

run_menu()