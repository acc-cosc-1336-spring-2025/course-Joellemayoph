from tuples import get_p_distance, get_p_distance_matrix
import ast

def display_menu():
        print('1-GET P DISTANCE MATRIX')
        print('2-EXIT')

def run_menu():
    user_option = '0'

    while(user_option != '2'):
        display_menu()

        user_option = input("Enter a menu option(1 or 2): ")
        handle_menu(user_option)

def handle_menu(user_option):
    if(user_option == '1'): 
        strands = [0] * 4

        for index in range(4):
            inputstrands = input(f'Please enter strand #{index+1} ')
            strands[index] = ast.literal_eval(inputstrands)

        result = get_p_distance_matrix(strands)

        print(result)
        print()

             
    elif(user_option == '2'):
        print('EXITING ...')

    else:
        print("TRY AGAIN")

run_menu()