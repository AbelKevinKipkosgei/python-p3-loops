#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    number = 10
    while(number >= 1):
        print(number)
        number -= 1
    print("Happy New Year!")

def square_integers(int_list):
    # code goes here!
    int_list = [integer * integer for integer in int_list]
    print(f"Squared List: {int_list}")
    return int_list

def fizzbuzz():
    # code goes here!
    for number in range(1, 101):
        if (number % 3 == 0 and number % 5 == 0):
            print("FizzBuzz")
        elif(number % 5 == 0):
            print("Buzz")
        elif(number % 3 == 0):
            print("Fizz")
        else:
            print(number)

happy_new_year()
square_integers([1,2,3,4,5])
fizzbuzz()