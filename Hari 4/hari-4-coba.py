# Input a number and decide the remarks based on the number
x=int(input("Please enter an integer: "))

if x<0:
    a = abs(x)
    for i in range(a):
        print("*", end="")
    x=0
    print("\nNegative changed to zero")
elif x==0:
    print("Zero")
elif x==1:
    print("Single")
else:
    print("More")

print("Selesai")