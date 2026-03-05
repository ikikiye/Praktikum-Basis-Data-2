import os
import random as rd

Pixel = ["@","#","&","=","+","o","*","."," "]

def randGen(inputResolusiX, inputResolusiY, inputKontras, inputKecerahan):
    for i in range(inputResolusiY):
        for i in range(inputResolusiX):
            randomValue = rd.randrange(inputKecerahan)
            print(Pixel[randomValue*inputKontras], end=" ")
        print()

while True:
    os.system('clear')
    inputResolusiX = int(input("Resolusi X = "))
    inputResolusiY = int(input("Resolusi Y = "))
    inputKecerahan = int(input("Kecerahan = "))
    inputKontras = int(input("Kontras = "))
    print()

    randGen(inputResolusiX, inputResolusiY, inputKontras, inputKecerahan)

    confirmationCont = input("\nApakah ingin mengulang program? (y/n) ").strip().upper()

    if confirmationCont == "Y":
        os.system('clear')
        continue
    else:
        os.system('clear')
        break