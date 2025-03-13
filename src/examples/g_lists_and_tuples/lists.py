import array

def test_config():
    return True

def use_int_array():
    list_array = array.array('i')
    list_array.append(3)
    
    #i stands for interger data type 
    print(list_array[0])
    list_array.append(1)
    print(list_array[1])

    list_array.append(5)
    print(list_array[2])
    #numbers require 4 bytes to display memory
    #Bracket 1 = value 1, the syntax for bracketing works for strings and for lists 

def modify_list_array_elements():
    #We cannot modify elements 
    #lang = 'Python'
    #lang[0] = 'p'
#change letter p to lower case p
#It'll return an error, we can't 

    list_array = array.array('i', [3, 1, 5])
    print(list_array[2])

    list_array[1] = 2 

    print(list_array[1])

def use_float_array():
        float_array = array.array('f')
        float_array.append(3.5)
        float_array.append(9.1)
        float_array.append(77.6)

        size=len(float_array)
        print(size)

        for i in range(0,size):
            print(float_array[i])

def use_char_array():
#Arrays with characters
    char_array = array.array('u')

    char_array.append('P')
    char_array.append('y')
    char_array.append('t')
    char_array.append('h')
    char_array.append('o')
    char_array.append('n')

    for char in char_array:
        print(char)

def arrays_in_memory():
     #id gives us the real memory 

     int_array = array.array('i')
     print(id(int_array))

     int_array.append(7)
     print(id(int_array[0]))

     int_array.append(20)
     print(id(int_array[1]))

    #string is a sequence of characters 
    #arrays are lists that allow you to work with one type of data 
    #lists involve mixed types of data 

def intro_to_lists():
     even_numbers = [2, 4, 6, 8, 10] #list 
     print(even_numbers)

def loop_list_w_while():
    even_numbers = [2,4,6,8,10]
    index = 0

    while(index < len(even_numbers)):
         print(even_numbers[index])
         index += 1

def loop_list_w_for():
    even_numbers = [2,4,6,8,10]
    
    for num in range(0, len(even_numbers)):
         print(num, even_numbers[num])

def loop_list_w_for_range():
     even_numbers = [2,4,6,8,10]

     for i in even_numbers:
        print(i) 