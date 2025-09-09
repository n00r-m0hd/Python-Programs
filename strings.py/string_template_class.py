from string import Template

# Defining template string
str = "Hi my name is $name"

# Creating template object
templateObj = Template(str)

# Now Provide values

new_str = templateObj.substitute(name="Noor Mohd")

print(new_str)