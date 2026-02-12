import os
import random as rd

def main():
    os.system('clear')
    print("=============Kalkulator yang tidak berguna=================")

    a=int(input("Tuliskan Angka Pertama = "))
    b=int(input("Tuliskan Angka Kedua = "))

    c=input("Tuliskan Operator (x, :, +, -) = ")
    randomNum = rd.randrange(1,1000)

    if c == "x" and a*b != randomNum:
        Hasil = a*b
        print("Bukan Hasilnya =", randomNum)
        #print(Hasil)
    elif c == ":" and a*b != randomNum:
        Hasil = a/b
        print("Bukan Hasilnya =", randomNum)
        #print(Hasil)
    elif c == "+" and a*b != randomNum:
        Hasil = a+b
        print("Bukan Hasilnya =", randomNum)
        #print(Hasil)
    elif c == "-" and a*b != randomNum:
        Hasil = a-b
        print("Bukan Hasilnya =", randomNum)
        #print(Hasil)
    else:
        print("        FLASHBANG        ")
        print("===== ehdn of program =====")

while True:
    main()
    konfirmasi = input("Apakah ingin lanjut? (y/n) :").strip().upper()

    if konfirmasi == "Y":
        alif = 4
    elif konfirmasi == "N":
        os.system('clear')
        break
    else:
        print("woi yang bener ngetiknya")
        input()