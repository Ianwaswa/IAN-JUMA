#Manifesting good times ahead

age = 20
name = "John"
my_str = "Kindly be %s years old first" % age
mysecond_str = "Hello %s, you are %s years old. You can join our Night Club" % (name, age)
for i in range(1, 20):
    if i >= age:
        print(my_str)
    else:
        print(mysecond_str)