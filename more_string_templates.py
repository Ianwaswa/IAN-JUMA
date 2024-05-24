from string import Template
username = "John"
age = 25
Template = Template("Hello $username, you are $age years old.")
response = Template.substitute(username=username, age=age)
print(response) # Hello John, you are 25 years old.