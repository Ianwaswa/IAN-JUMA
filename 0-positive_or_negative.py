#Tells whether a number is positive or negative
import random

number = random.randint(-10, 10)
for number in range(-10, 11):
    if number > 0:
        print(f"{number} is positive")
    elif number < 0:
        print(f"{number} is negative")
    else:
        print(f"{number} is zero")