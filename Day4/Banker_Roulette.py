import random

name_string = input("Give me everybody's names, separated by a comma. ")

names = name_string.split(", ")

print(names)

name_len = len(names)

Who = random.randint(0, name_len - 1)

person_who_will_pay = names[Who]

print(person_who_will_pay +"is going to buy the meal today.")

