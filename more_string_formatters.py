from string import Template
user_input = ("Jack")
email_template = Template("Hello $name, welcome to the world of Python!")
email = email_template.substitute(name=user_input)
print(email)