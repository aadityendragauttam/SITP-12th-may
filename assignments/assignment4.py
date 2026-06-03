# #Q1. Explain Python Data Types in detail.Discuss the following data types with syntax and examples:
# #    Integer,Float,String,Boolean,List,Tuple,Set,Dictionary

# #Sol: Data type defines the kind of value a variable can store. We don't need to declare the type of variable in python.
# #Integer : Whole number without a decimal. Can be positive,negative or zero.
# #SYNTAX : variable_name = integer_value
# #Example:
# a = 12
# print(a)
# print(type(a))
# #Float : Represents decimal or real numbers
# #SYNTAX : variable_name = float_value
# #Example:
# a = 12.12
# print(a)
# print(type(a))
# #String : String is a Sequence of characters
# #SYNTAX : variable_name = "text"
# #Example: 
# name =  "Aadityendra"
# print(name)
# print(type(name))
# #Boolean : Represents Logical value: Ture or False
# #SYNTAX : variable_name = True   or   variable_name = False
# #Example:
# is_positive = True
# is_negative = False
# print(is_positive)
# print(is_negative)
# print(type(is_positive))

# #List : Ordered and Mutable collection of data.
# #SYNTAX : list_name = [item_1,item_2]
# #Example:
# lst = [1,2,3.23]
# print(lst)
# print(type(lst))

# #Tuple : Ordered but immutable collection of data.
# #SYNTAX : tuple_name = (item_1,item_2)
# #Example:
# tup = (11,22,"hello")
# print(tup)
# print(type(tup))

# #Dictionary : Collection of item in pair of key and value.
# #SYNTAX : dict_name = {key_1:val_1,key_2:val_2}
# #Example:
# dictionary = {"name" : "Aadityendra","age":18}
# print(dictionary)
# print(type(dictionary))

# #Sets : Unordered Collection of unique elements
# #SYNTAX : set_name = {item_1,item_2}
# #Example:
# nums = {1,2,2,3,4,1}
# print(nums)
# print(type(nums))


# #Q2. Write a Python program to demonstrate dynamic typing and type checking using the type() function.The program should:
# #    Declare variables of multiple data types,Print their values, Print their corresponding data types	

# integer = 1
# print(integer)
# print(type(integer))
# pi = 3.14
# print(pi)
# print(type(pi))
# name = "Aadityendra"
# print(name)
# print(type(name))
# lst = [1,2,3.23]
# print(lst)
# print(type(lst))
# tup = (11,22,"hello")
# print(tup)
# print(type(tup))
# dictionary = {"name" : "Aadityendra","age":18}
# print(dictionary)
# print(type(dictionary))
# nums = {1,2,2,3,4,1}
# print(nums)
# print(type(nums))

# #Q3. Differentiate between	Mutable	and	Immutable Data Types in Python	with suitable examples.
# #  Also explain: Why strings are immutable, Why	lists are mutable, Real-time use cases of both

# #Sol :
# # Mutable Data Types – Objects whose values can be changed after creation. E.g: List,Dictionary,Set etc.
# # Immutable Data Types – Objects whose values cannot be changed after creation. e.g: Tuple,String etc. 	

# # Why strings are immutable : Strings are immutable because once created, their contents cannot be changed.
# name = "Python"
# # name[0] = "J"         #returns TypeError

# # Why lists are mutable: Lists are mutable because it allows changing,adding or removing elements after creation
# lst = [1,3,"hello"]
# lst[1] = 2
# print(lst)          #returns 2 at index 1 instead of 3

# # Real-time use cases of both 
# # Immutable DT : String: Used for Username,Passwords, Tuple : Used for Database records,etc.
# # Mutable DT : List : Used for Student records,To-do lists, Dictionary : Used for User profile,JSON data etc.

# #Q4.Write a Python program to perform various operations on Python	collections:
# # List operations (append(),remove(),slicing)
# lst = [1,2,3.14,"Hello"]
# lst.append("Hii")
# print(lst)
# lst.remove(2)
# print(lst)
# print(lst[1:4])

# # Tuple indexing : 
# tup = (1,3,55.34,"Good Morning")
# print(tup[2])
# print(tup[::2])

# # Setoperations(union,intersection):
# set_1 = {1,2,3}
# set_2 = {3,4,5}
# union = set_1.union(set_2)
# print(union)
# intersection = set_1.intersection(set_2)
# print(intersection)

# # Dictionary operations(keys(),values(),item())
# dictionary = {"name":"Aadityendra","age":18,"height":6}
# print(dictionary.keys())
# print(dictionary.values())
# print(dictionary.items())

#Q5. Develop a mini	Student	Management	System	using Python datatypes.	
# The program	should:	
# ● Store student details using	Dictionary	
# ● Store subject marks	using List	
# ● Calculate total	and	average	marks	
# ● Display	the	output in proper format	

#Sol:
student = {"name":"Aadityendra",
           "roll_no.":1,
           "course":"AI & DS"}
marks = [85, 90, 78, 88, 92]
total = sum(marks)
average_marks = total / len(marks)

print("Roll Number   :", student["roll_no."])
print("Name          :", student["name"])
print("Course        :", student["course"])

print("Subject Marks :", marks)

print("Total Marks   :", total)
print("Average Marks :", average_marks)
