#Q1 : Write a program to declare variables of different data types and print them. 
name = "Aadityendra"
age = 18
height = 6.0
grade = 'A'
lst = [1,2,3,4]
tup = ('a','b','c')
dictionary = {"name" : "Aadityendra", "age" : 18, "height" : 6.0, "grade" : 'A'}
seT = {11,22,33}
print("Name = ",name)
print("Age = ",age)
print("height = ",height)
print("Grade = ",grade)
print("List = ",lst)
print("Tuple = ",tup)
print("Dictionary = ",dictionary)
print("Set = ",seT)

#Q2 : Write a program to create a string and perform operations like uppercase,lowercase, and length check. 
string = "UpFlairs"
print("\nString = ",string)
print(string.upper())
print(string.lower())
print(len(string))

#Q3 : Write a program to create a list of numbers and print its elements using indexing. 
lst = [1,2,3,4,5,6,7]
for i in range(0,7):
    print(lst[i])

#Q4 : Write a program to concatenate two strings and store the result in a variable. 
str1 = "Up"
str2 = "Flairs"
concatenate = str1 + str2
print(concatenate)

#Q5 : Write a program to create a list of student names and add a new name into the list.
lst = ["Aadityendra","Zendaya","Tobey","Tom"]
lst.append("Andrew")
print(lst)