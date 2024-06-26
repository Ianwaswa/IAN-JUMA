# Print all even numbers between 1 and 10
count = 0
for  x in range(1, 10):
    if  x % 2 == 0:
        count += 1
        print(x)
print(f'We have {count} even numbers')