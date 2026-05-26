import fungsiSQL

namaKolom = fungsiSQL.ambilField()
dataBarang = fungsiSQL.ambilBarang()

def gabungKeList(namaKolom, dataBarang):
    listBarang = []
    listKolom = []
    for kolom in namaKolom:
        listKolom.append("%s"%kolom)
    for barang in dataBarang:
        listBarang.append(dict(zip(listKolom, barang)))
    return(listBarang,listKolom)

listbar, listkol = gabungKeList(namaKolom[0], dataBarang[0])
print(listbar)
for i in listbar:
    print(i)
