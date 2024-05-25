#Prompt users to enter their age
age = input("How old are you? ")
#condition to determine the grade of the user
age = int(age)
if age < 5:
    print("You are a baby!")
elif age == 5:
    print("You are a kindergartener!")
elif age > 5 and age <= 18:
    print("You are a student!")
else:
    print("You are an adult!")