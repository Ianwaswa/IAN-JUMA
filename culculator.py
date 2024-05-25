#Prompt users to enter numbers and the operators they want to use
#Operators are +, -, *, /, % and //
num1,operator, num2 = input("Enter Calculation: ").split()
#Convert all strings to integers
num1 = int(num1)
num2 = int(num2)
#If operator is +, add the two numbers and print the result based on sum
if operator == '+':
    print("{} {} {} = {}".format(num1, operator, num2, num1 + num2))

#If operator is -, subtract the two numbers and print the result based on difference
elif operator == '-':
    print("{} {} {} = {}".format(num1, operator, num2, num1 - num2))
elif operator == '*':
    print("{} {} {} = {}".format(num1, operator, num2, num1 * num2))
elif operator == '/':
    print("{} {} {} = {}".format(num1, operator, num2, num1 / num2))
elif operator == '%':
    print("{} {} {} = {}".format(num1, operator, num2, num1 % num2))
elif operator == '//':
    print("{} {} {} = {}".format(num1, operator, num2, num1 // num2))
else:
    print("Invalid operator")
#Print the result of the operation