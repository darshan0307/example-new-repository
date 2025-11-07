import random

names = input("Enter your frnds names seprerated with comma(,):")
a = names.split(",")
c = random.choice(a)
print(f"{c} you will pay the bill...")