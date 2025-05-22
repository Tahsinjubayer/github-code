print("Welcome to the Rollercoster ")
Height = int(input("Enter your height: "))
bill = 0

if Height > 120:
    print("Can ride")
    age=int(input("What is your age? "))    
    if age >=18:
     bill = 22
     print("Adult tickets $22")
    elif age <= 12:
     bill = 7
     print("Child tickets $7")
    else:
     bill = 12
     print("Youth tickets $12")
    wants_photo = input("Do you want a photo taken? Y or N.\n")
    if wants_photo == "Y":
     bill += 3
     
    print(f"Your total bill: {bill}")

else:
    print("Cant ride next time")
