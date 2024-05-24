from string import Template
name = "Harry"
second_name = "Potter"
Template = Template("$name and $second_name wish you a happy birthday!")
birthday_wish = Template.substitute(name=name, second_name=second_name)

print(birthday_wish) # Harry wishes you a happy birthday!