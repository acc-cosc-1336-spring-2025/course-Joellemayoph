from strings import get_hamming_distance, get_dna_complement
    
def display_menu():
        print('1-HAMMING DISTANCE')
        print('2-DNA COMPLEMENT')
        print('3-EXIT')

def run_menu():
    user_option = '0'

    while(user_option != '3'):
        display_menu()

        user_option = input("Enter a menu option(1,2,3): ")
        handle_menu(user_option)

def handle_menu(user_option):
    if(user_option == '1'): 
        dna1 = input('Enter your first DNA sequence: ')
        dna2 = input('Enter your second DNA sequence: ')
        result = get_hamming_distance(dna1, dna2)
        print(f'The hamming distance between the two DNA strands is: {get_hamming_distance(dna1, dna2)}!')

    elif(user_option == '2'):
        dna = input("Enter the DNA sequence to determine it's complement: ")
        result = get_dna_complement(dna)
        print(f' The DNA complement is: {get_dna_complement(dna)}')

    elif(user_option == '3'):
        print('EXITING ...')

    else:
        print("TRY AGAIN")

run_menu()


