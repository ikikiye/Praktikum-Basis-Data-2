def cetak():
    print("Selamat Datang")

def hitung(x):
    vol=x*x*x
    print(vol,"meter kubik")

n = int(input("n:"))
p = int(input("p:"))

if p==1:
    for m in range(n):
        cetak()
elif p==2:
    hitung(n)