#!/usr/bin/python3
fizzbuzz = __import__('12-fizzbuzz').fizzbuzz
def fizzbuzz():
    for i in range(1,100):
        if i % 3 == 0:
            print("Fizz",end=" ")
        elif i % 5 == 0:
            print("Buzz",end=" ")
        else:
            print(i,end=" ")
fizzbuzz()
