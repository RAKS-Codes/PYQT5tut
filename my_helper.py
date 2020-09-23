import math
import os 
import random

def cube_root(y):
    print(y)
    return y **(1/3)


print("What do you wanna test today?") 
print("Choose from the optons below: \n")

print("1. Find the square of the given number: ")

print("2. Find the cube of the given number: ")

print("3. Find the square root of the given number: ")

print("4. Find the cube root of the given number: ")

x = random.randint(0,50)
y = random.randint(0,15)
choice = int(input())

if (choice == 1):
    print("What is the SQUARE of" , x)
    d = int(input("Enter your answer: "))
    if (d == x * x):
        print("Perfecto")
    else:
        print("Practice more you moron")
        print("The answer is" , x * x)

elif (choice == 2):
    print("What is the cube of" , y)
    d = int(input("Enter your answer: "))
    if (d == (y * y * y)):
        print("Perfecto")
    else:
        print("The right answer is" , (y * y * y))
        print("Practice and come back you moron.")

elif (choice == 3):
    print("What is Square root of" , x)
    d = int(input("Enter your answer: "))
    if (d == (math.sqrt(x))):
        print("Perfecto, Wonderful job")
    else:
        print("The correct answer is: " , math.sqrt(x))
        print("Good try")
else:
    print("Enter the cube root of" , cube_root )
    d = int(input("Enter your answer: "))
    if (d == cube_root):
        print("Perfecto")
    else:
        print("The correcct answer is:" , cube_root)
        print("Practice hard and come back")