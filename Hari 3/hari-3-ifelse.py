# Buatlah program untuk inputan x yang jika x lebih kecil dari 10, maka
# beri keterangan : "x lebih kecil dari 10"
# Selain itu, beri keterangan : "x sama dengan atau lebih besar dari 10"
# Liat kodenya aja, gw malas copas keterangannya yg di papan

x=int(input("Nilai x:"))

if x<10:
    print(x,"lebih kecil dari 10")
elif x > 10:
    print(x,"lebih besar dari 10")
else:
    print(x,"sama dengan 10")