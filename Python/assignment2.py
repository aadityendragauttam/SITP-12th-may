# Question 1: Write a Python program to print your name, course, and city using proper formatting.

name = "Aadityendra"
course = "Data Science with ML and AI"
city = "Jaipur"
print(f"Good morning {name}, Kindly confirm that your course name is '{course}' and you are from '{city}' city.")

# Question 2: Take user input for name and age, then print: "Hello <name>, you are <age> years old" 

name = input("Enter your Name : ")
age = int(input("Enter your Age : "))
print(f"Hello {name}, You are {age} years old")

# Question 3: Write a program to: Take a string input, Print its reverse, Count total number of characters 

name = input("Enter your Name  : ")
rev = name[::-1]
print(rev)
print(len(name))


