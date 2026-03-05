listSaya=[]

z = int(input("\nMasukkan Nilai z (jumlah data): "))
print()
for i in range(z):
    x = int(input("Masukkan Nilai x (Datanya): "))
    listSaya.append(x)

print("\nHasil Output:")
for i in range(z):
    print("Data ke", i, " = ",listSaya[i])
