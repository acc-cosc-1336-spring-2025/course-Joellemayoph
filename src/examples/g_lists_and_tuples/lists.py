
#Program to calculate the sum of a series of numbers entered by the user 
#Program to calculate the number of b ugs 
def get_bugtotal():

    bugs = 0

    for counter in range(5):
        caught = int(input(f'How many bugs did you catch on Day {counter+1}? '))
        bugs += caught

    print(f' You have caught a total of {bugs} bugs!')

def calories_burned():

    minutes = int(input('How long have you ran for? '))
    calories = 0 

    for counter in range(minutes):
        burned = 4.2
        calories += burned

    print(calories)

#Table 
def calories_burned2():

    print('Minutes\tCalories')
    print('-----------------')

    for counter in range(10,31,5):
        burned = counter * 4.2
        print(f'{counter}\t{burned}')

def budget_analysis():

    maximum = int(input('What is your budget for this month?'))
    spending = 0

    for counter in range(maximum):
        expense = int(input('Enter your expense: '))
        spending += expense

    if spending > maximum:
        print('You are over budget!')

def budget_analysis2():

    maximum = int(input('What is your budget for this month?'))
    spending = 0

    while spending <= maximum:
        expense = int(input('Enter your expense: '))
        spending += expense
        print(f'You have spent {spending}')

    if spending > maximum:
        print(f'You are over budget by {spending-maximum}')