from string import Template
name = "Harry"
Template = Template("$name wishes you a happy birthday!")
birthday_wish = Template.substitute(name=name)

print(birthday_wish) # Harry wishes you a happy birthday!