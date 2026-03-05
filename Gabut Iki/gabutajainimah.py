import random as rd

print("RANDOM NUMBER GUESSER")

a = rd.randrange(1,10)
b = input("Guess a number = ")

if a == b:
    print("wow, genius")
    print("Jawabannya = ", a)
else:
    print("hahahhahaha")
    print("Jawabannya = ", a)
