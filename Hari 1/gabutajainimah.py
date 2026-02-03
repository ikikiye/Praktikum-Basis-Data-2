import random as rd

print("RANDOM NUMBER GUESSER")

a = rd.randrange(1,10)
b = None

print("Guess a number = ")
input(b)

if a == b:
    print("wow, genius")
else:
    print("hahahhahaha")