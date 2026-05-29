import random
import string
val = string.ascii_letters + string.digits + string.punctuation
try:
    length = int(input("Enter Length of your Password : "))
    if length <= 0:
        print("Length must be positive...")
    else :
        password = ""
        for i in range(length):
            password += random.choice(val)
        print("Your Random Password is : ",password)
except ValueError:
    print("Please Enter a Valid Input...")