# # LIst
# lst = [1,2,4,565,"hello",3.56]
# # print(lst)
# # print(type(lst))
# # print(len(lst))
# # print = 10
# # print(print)              #whyyyyyyyyyyy
# # list = 10
# # print(list)         #whyyyyyyyyyyyyyyyyy
# print(lst[0])
# print(lst[1])
# print(lst[2])
# print(lst[3])
# print(lst[4])
# print(lst[5])

# print(lst[-1])

# print(lst[0:7:2])

# fruits = ["mango","banana","tomato","Pineaaple","Watermalon","Dragon Fruit"]
# # fruits.append("Apple")              #adds element in the last position
# # #print(fruits.append("Apple")    )  #wont work
# # print(fruits)
# # fruits.insert(0,"Strawbary")          #insert value at specific given index
# # print(fruits)
# # fruits.remove("mango")                #remove specific element
# # print(fruits)
# # fruits.pop()             #pop last element
# # print(fruits)
# # fruits.pop(2)           #pop elements at 2nd index
# # print(fruits)
# # fruits.clear()            #clear all the elements from the list
# # print(fruits)
# fruits.copy()               #creates a copy of list
# print(fruits)
# print(fruits.count("banana"))
# print(fruits.index("Dragon Fruit"))
# print(fruits[::-1])             #reverse the list
# fruits.reverse()                #reverse the list using reverse function
# print(fruits)
# #len,max,min,sum,sorted 
# lst1 = [2,3,1]
# lst2 = [3,4,5]
# print(lst1 + lst2)
# print(max(lst1))                #return max element of list
# print(min(lst2))                #return min element of list
# print(sum(lst1))
# print(sorted(lst1))

##Tuples

# tup = 23,34,23,"hello",43,00.00         #default stored in tuple, Manually : tup = (23,34,23,"hello",43,00.00)
# #tup[1] = 34            #not allowed in tuple
# print(type(tup))
# print("Length : ",len(tup))
# print(tup)
# print("Element at 2nd position :",tup[1])
# print(tup[1:5])
# print(tup.count(0))            #returns no. of occurence of argument in tuple
# print(tup.index(34))            #returns index of first occurence


# # #Adding element in Tuple
# lst = list(tup)
# lst.append(123)
# lst.remove(23)
# tup = tuple(lst)
# print(tup)

# # #Tuple Unpacking
# a,b,c = (1,2,3)
# print(a)
# print(b)
# print(c)

#Dictionary
# Student = {
#     "name":"Aadityendra",
#     "age":18,
#     "Roll no. : ":1,
#     "Branch":"AI & DS"
# }
# print(Student)
# print(Student.keys())
# print(Student.values())
# print(Student.items())
# print(Student["name"])
# print(Student["age"])
# print(Student["Roll no. : "])
# print(Student["Branch"])
# Student["subject"] ="Python"            #Adding element in Dicitionary
# print(Student)                  #Task 1 : Use update function #fromkey()
# print(Student.get("name"))
# copydict = Student.copy()
# print(copydict)
# print(Student.pop("name"))
# print(Student.popitem())
# Student.update({"age":20})
# print(Student)
# Student.setdefault("height",6)      #Task 2 : Deep copy
# print(Student)
# Student["height"]=7
# print(Student)
# Student.clear()
# print(Student)

# car = {"brand":["BMW","Rolls Royce"]}
# for x in car.items():
#      print(x)
# print(car)

# #Set

# Set = {1,3,45,233,465,3,446,575,32}
# print(Set)
# print(type(Set))
# Set.remove(3)
# print(Set)
# #Set.remove(4)   #gives error
# Set.discard(45)
# print(Set)                                      #Removes gives error when argument goes out of range 
# Set.discard(4)      #doesn't gives error
# print(Set)



