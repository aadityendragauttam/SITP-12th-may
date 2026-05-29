import random
print("Welcome ,Please guess a number between 1 - 100 :",end = " ")
random_num = random.randint(1,100)
while True :
    try:
        number = int(input())
        if number == random_num :
            print("Congrats!!, that's Correct🎉")
            break
        elif number < random_num :
            print("Guess a bigger number :",end = "")
        else :
            print("Guess a smaller number :", end = "")
    except ValueError:
        print("Please Enter a Valid Input :",end = "")
print("----- Game Over -----")