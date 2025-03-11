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

