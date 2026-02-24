a=int(input("Masukkan Nilai a = "))
b=int(input("Masukkan Nilai b = "))

for i in range(a,b+1):
    if i == 2 or i == 4 or i == 7:
        print(i,"**")
    else:
        print(i)