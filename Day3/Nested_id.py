print("Welcome to the rorercoster ")
Height = int(input("Enter your height: "))

if Height > 120:
    print("Can ride")
    age=int(input("How is your age "))    
    if age >=18:
     print("You pay $22")
    elif age <= 12:
     print("You pay $7")
    else:
     print("You pay $12")            
else:
    print("Cant ride next time")
