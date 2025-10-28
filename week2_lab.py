"""
1) This program converts a temprerature from Celsius to Fahrenheit
"""
name = "Celsius" 
print (name)
Celsius = 29 
# This number represents the Celsius
Fahrenheit = (Celsius * 9/5) + 32
# This is a formula that takes the tempreture of Celcius which was 25 and times it by 9/5 and adds 32 to it.
print (Fahrenheit)
# This is the temperature in Fahrenheit
print ("The Temperature is", Celsius, "in", name)
print ("The temperature is", Fahrenheit, "in Fahrenheit")
# The print comand ensures to display what the user wants this to display. 
"""
By simpy changing the integer we can observe how the actual output changes. 
"""

"""
2) Data types & variables
"""
# This is an example of string
a = ("Hello Josh")
print(type(a))
# This is an example of integer
b = 22
print(type(b))
# This is an example of float
c = 1.70 
print(type(c))
# This is an example of bool
d = True
print(type(d))

# Python assures to figure our the type based on the value that has been asssigned. And if new variables gets assigned, Python will ensure to change these according to tyhe new ones that have been assigned to it. 

"""
3) String formatting
"""
x = ("Ujala")
y = ("BSC Computer Science with AI student")
z = x, y
print (z)
txt = "Selling this book for only {price:.2f}pounds!"
print(txt.format(price = 21))
