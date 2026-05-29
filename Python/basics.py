print("Hello world")
x = 10
y = "Aadityendra"
print(x,y)
print(type(x))
print(type(y))
x = y = z = "Orange"
print (x,y,z)
a = "ABC"                   
x= "A"
y="B"
z="C"
print(x,y,z)
"""
VARIABLE -- Containers for storing data values
Variable name must start with a letter or underscore character
variable name cannot start with a number
Can only contain alpha numeric characters and underscores (A-z,0-9)
This means uppercase and lowercase letters are treated and different variables
variabe name cannot be any of the python keyword
"""
myvar = "john"
my_var = "john"
_my_var = "john" 
myVar = "john"
MYVAR = "john"
myvar2 = "john"

#print() pretty flexible you can enter multiple value output seprated by space

print(34)
print("Aadityendra")
#print(salman khan)
print("Aadi",23,56.8,True)
print("Aadityendra ",56,"Max")

print("Hello ",end=",")
print("My name is Aadityendra")

print("I am from",end= " ")
print("India")

print("Hello"); print("Guys");print(1234)
print(x,y,z)

#dynamic typing --- c, c++ lsngusgr you hsve tell the datatype before giving value to the variable

#int a = 20
x = 56
print(x)
print(type(x))

#dynamic binding == in pythonvthere is no fix datatype

a = 45
print(a)

a = "divya"
print(a)

a = int('5')
b = ('5')
print(a)
print(type(a))          #casting
print(b)
print(type(b))
# Many value to many variable -- Python allows you to assign values to multiple variables

x,y,z = "apple","orange","banana"
print(x,y,z)

x = y = z = "Watermelon"
print(x,y,z)


#Unpack aa collection... if you have a collection of values in a list,tuple etc.
#Python allows try to extract the value into variables

#list unpacking

a = ["Aadi",123,"Hello"]
x,y,z = a
print(x)
print(y)
print(z)

#tuple unpacking

x = (3,4,5)
a,b,c = x
print(a,b,c)

#string unpack

a = "ABC"
x,y,z = a
print(x+y+z);print(x,y,z)

#Casting --- if you want to specify the data type of a variabe. this can be done with casting

x = int(3)
y = float(3)
z = str(3)
print(x);print(type(x)) 
print(y);print(type(y))
print(z);print(type(z))

#Type Conversion --- You can convert from one type to another with the int(),float(),str()
#1. Implicit type onversion -- Internally know the data type

print(5 + 5.8)
print(type(5),type(5.8))

#2. Explicit type conversion -- programmer request to change the data type

x = float (20)
print(x)

##User input--
#Static VS Dynamic software -- Static dont talk with user they only gives information (ex - calender,blog,clock) 
#Dynamic -- user input data hai (ex - - youtube,ola,zomato)

a = input( "What is your name: ")
b = input("Enter your age : ")
print( a , b)

a = int(input("Enter first number: "))
b = int(input("Enter second number : "))
c = a + b
print(c)

name = input("ENter your name : ")
print("Hello ", name)

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
sum = a * b
print("Total = ",sum)

#Swap TWo numbers program 

a= 20
b =12
a,b = b,a
print("A : ",a, "B: ",b)

a = 23
b = 12
c = 34
a,b,c = c,a,b
print("A : ",c, "B: ",a, "C: ", b)

#string rule 
# 1 - sequence of charracters written inside quotes
# 2 - includes letter, numbers and spaces 
# 3 - string are immutable/unchangable
# 4 - but we can manipulate strings - use methods like concatenation,licing,formatting to create new str
# 5 - delete an entire string variable (In python it is not possible to delete individual characters)

a = "hello"
print(a)
b = "Python isnt tuff"
print(b)
c = ''' hey how you
sb badhiya
main thik hu'''
print(c)