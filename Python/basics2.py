name = "Aadityendra"
upper_case = name.upper()               #capitalize the string in variable
print("Upper case :- ",upper_case)
lower_case = name.lower()               #uncapitalize the string
print("Lower case :- ",lower_case)

print(name.casefold())          #lower case vs casefold

s = "Straße"
print(s.lower())   #s = straße                  lower for std. lowercase conversion
print(s.casefold())   #s = strasse              for case insensitive string comparision 
a = "Straße"
b = "STRASSE"

print(a.lower() == b.lower())       # False
print(a.casefold() == b.casefold()) # True

name = "aadityendra gAUTTAM"
print(name.title())             #Title makes the first letter of every word uppercase

print(name.capitalize())        #Capitalize only makes the first letter of First word uppercase

company_name = "Aadtiyendra Gauttam     "
print(len(company_name.strip()))
print(company_name.strip())

name = "Aadityendra Gauttam"
print(name[len(name)-1])
print(name[:12])                    

#reverse the string
a = "Aadityendra"
rev = a[::-1]
print(rev)

reverse = ''.join(reversed(a))
print(reverse)

# mul = company_name + 2
# print(mul)

add = name + company_name
print(name)

print(name * 2)

#task : difference btw name = 'dev' and name = "dev"

# print(name.split("a"," "))   spilt function

print(f"My name is {name}")
path = r"C:\Users\user\OneDrive\Desktop"
print(path)

age = int(input("Enter your age : "))
print(age)
print(type(age))