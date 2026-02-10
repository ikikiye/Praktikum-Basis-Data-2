import random as rd

print("=============Kalkulator yang tidak berguna=================")

a=int(input("Tuliskan Angka Pertama = "))
b=int(input("Tuliskan Angka Kedua = "))
c=input("Tuliskan Operator (x, :, +, -) = ")
randomNum = rd.randrange(1,a+b)

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