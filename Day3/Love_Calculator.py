print("Welcome to the Love Calculator! ")

name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_string = name1 + name2
lower_case_string = combined_string.lower()

t = lower_case_string.count("t")
a = lower_case_string.count("a")
h = lower_case_string.count("h")

tah = t+a+h

s = lower_case_string.count("s")
i = lower_case_string.count("i")
n = lower_case_string.count("n")

sin = s+i+n

Love_Score = int(str(tah) + str(sin))

if (Love_Score < 10) or (Love_Score > 90):
    print(f"Your score is {Love_Score}, you go together like coke and mentos")

elif (Love_Score < 40) and (Love_Score > 50):
    print(f"Your score is {Love_Score}, you are all together.")

else:
    print(f"Your score is {Love_Score}")



