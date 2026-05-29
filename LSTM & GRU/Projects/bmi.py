while True: 
    try:
        weight = float(input("Enter Your Weight(in kg) = "))
        if(weight <= 0):
            print("Weight must be a positive value.")
            continue
        while True:
            height = float(input("Enter Your Height (in m)= "))
            if(height <=0):                
                print("Height must be a positive value.")
                continue
            else:
                break
        bmi = weight/(height**2)
        if (bmi<18.5):
            print(f"Your bmi is { bmi:.2f} and you are Underweight")
        elif(bmi <= 24.9):
            print(f"Your bmi is { bmi:.2f} and you are Normal")
        elif(bmi <=29.9):
            print(f"Your bmi is { bmi:.2f} and you are Overweight")
        else:
            print(f"Your bmi is { bmi:.2f} and you are Obese")
    except ValueError:
        print("Please Enter in digits ")
    except Exception:
        print("Something went wrong!")
    finally:
        print("Want to check again?")
    quit_choice = input("Type 'q' to Quit or press Enter to continue : ")
    if quit_choice.lower() == 'q':
        break

