import decisions

def main(): 
    num1 = input("Enter your options: ")
    num2 = input("Enter your total: ")

    opratio = decisions.get_options_ratio(int(num1), int(num2))
    result = decisions.get_faculty_rating(opratio)

    print(result)

main()