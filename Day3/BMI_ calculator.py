Height = float(input("Enter your height in m: "))
Weight = float(input("Enter your weight in kg: "))

BMI = round(Weight / Height ** 2)

if BMI < 18.5:
    print(f"Your bmi is {BMI}, you are underweight.")
elif BMI < 25:
    print(f"Your bim is {BMI}, you are a normal weight")
elif BMI <30:
    print(f"Your bim is {BMI}, you are overweight")
elif BMI < 35:
    print(f"Your bim is {BMI}, you are obse")
else:
    print(f"Your bim is {BMI}, you are clinically obese")   