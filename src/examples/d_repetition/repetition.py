def test_config():
    return True

def use_a_while_loop(num):

    counter = 0 

    while(counter < num): #boolean expression loops while true, false stops loop 
        print(counter, counter < num, 'Hello')
        counter = counter + 1 
        #statement that makes the boolean expression false 

#4 1*1 + 2*2 + 3*3 + 4*4 = 30 
#4 1*1 + 2*2 + 3*3 + 4*4 + 5*5 = 55 
def get_sum_of_squares(num):
    
    sum = 0 

    while(num > 0):
        sum = sum + num * num 
        num = num - 1 #will make num > 0 false 

    return sum 
