import random

def test_config():
    return True

value = 100 #global variable 
VALUE = 1000 #GLOBAL constant - read only 

def echo_variable(num):
        return num

def read_global_variable():
      print(value)

def write_global_variable():
    global value
    value = 50 
    print(value)
    global VALUE
    VALUE = 10001
    print(VALUE)

    #when you write a constant, global variable, it cannot be changed 

def get_random_number(min, max):
      return random.randint(min, max)