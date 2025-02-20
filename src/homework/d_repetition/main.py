import repetition

def main():

    def display_menu():
        print('1-FACTORIAL')
        print('2-SUM ODD NUMBERS')
        print('3-EXIT')

    def run_menu():
        user_option = '0'

        while(user_option != '3'):
            display_menu()

            user_option = input("Enter a menu option(1,2,3): ")
            handle_menu(user_option)

    def handle_menu(user_option):
        if(user_option == '1'): 
            num = input("Enter a number: ")
            result = repetition.get_factorial(int(num))
            print("THE FACTORIAL IS:  ", result)
        elif(user_option == '2'):
            num = input("Enter a number")
            result = repetition.sum_odd_numbers(int(num))
            print("THE SUM OF ODD NUMBERS IS: ", result)
        elif(user_option == '3'):
            print('EXITING ...')
        else:
            print("TRY AGAIN")

    run_menu()
    
main()
