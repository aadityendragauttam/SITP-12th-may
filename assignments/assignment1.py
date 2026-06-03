#Question 1

"""import sys

num = int(sys.argv[1])

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not a prime number") 
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")"""


#Question 2

"""a = 10
b = 10
print(a == b)
print(a is b)
x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)
print(x is y)
s1 = "hello"
s2 = "hello"
print(s1 == s2)
print(s1 is s2)"""

#Question 3

"""num = [2,4,-5,3.4,"hello",-7,3,0,3,6]
for val in num:
    try:
        if not isinstance(val, int):
            raise TypeError
        elif val < 0:
            continue
        elif val == 0:
            break
        else:
            print(val)
    except TypeError:
         print("Item isn't integer")"""

#Question 4

"""lst = [(x * x) for x in range(1,21) if x % 2 == 0 and x % 5 == 0]
print(lst)"""

#Question 5

def show(num):
    item = num[0]
    for val in num:
        if val > item:
            item = val
    print(item , "is the biggest number")
    
    item = num[0]
    for val in num:
        if val < item:
            item = val
    print(item,"is the smallest number")

lst = [2,545,66,4,435,456,6]
show(lst)