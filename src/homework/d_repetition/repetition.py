def get_factorial(num):
        
    result = 1

    for n in range(1, num+1):
        result = n * result

    return result
    
def sum_odd_numbers(number):

    sum = 0 
    counter = 1 

    while(counter <= number): #boolean expression loops while true, false stops loop 
            sum = counter + sum
            counter = counter + 2 
            #statement that makes the boolean expression false 
            
    return sum

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
        result = get_factorial(int(num))
        print("THE FACTORIAL IS:  ", result)
    elif(user_option == '2'):
        num = input("Enter a number")
        result = sum_odd_numbers(int(num))
        print("THE SUM OF ODD NUMBERS IS: ", result)
    elif(user_option == '3'):
        print('EXITING ...')
    else:
        print("TRY AGAIN")

