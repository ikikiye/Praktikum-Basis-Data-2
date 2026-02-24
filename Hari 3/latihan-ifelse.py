x=int(input("Nilai x = "))

if x > 0 and x < 10:
    print(x, "positif, dan lebih kecil dari 10")
elif x > 0 and x > 10:
    print(x, "positif, dan lebih besar dari 10")
elif x == 0:
    print(x, "adalah nol")
else:
    print(x, "adalah bilangan negatif")