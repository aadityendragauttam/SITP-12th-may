print ("Welcome to the Quiz Contest")
while True:
    try:
        score = 0
        print("What is 2 + 2 ?")
        q1 = int(input("Your answer : "))
        if q1 == 4:
            print("Correct")
            score += 1
        else:
             print("Incorrect")
        print("What is the Capital of India ?")
        q2 = input("Your answer : ")
        if q2.lower() =="delhi":
            print("Correct")
            score +=1
        else:
            print("Incorrect")
        print("____ ke aage koi kuch bol skta h kya ?")
        q3 = input("Your answer :")
        if q3.lower()=="elvish bhai":
            print("Correct")
            score += 1
        else:
            print("Incorrect")
        print ("Yha immandari chalata babu na te ghare jake ____ babu?")
        q4 = input("Your answer :")
        if q4.lower() == "sutti":
            print("Correct")
            score +=1
        else:
            print("Incorrect")
        print("2026 me ky khtm h ?")
        q5 = input("Your answer : ")
        if q5.lower() == "duniya":
            print("Correct")
            score +=1 
        else:
            print("Incorrect")
    
        print(f"Thank you for participating in Quiz! You scored {score} out of 5")
    except ValueError:
        print("Please Enter a Valid Input...")

    quit_choice = input("Press 'q' to Quit or Press continue to play : ")
    if quit_choice.lower() == 'q':
        break