import pymysql.cursors

userDB = pymysql.connect(
  host="localhost",
  user="root",
  password="",
  database="mahasiswaDB_Basdat"
)

SQL = userDB.cursor() #inisiasi kayaknya

def pencarianData(wildcard):

    # ini buat nyari jumlah baris mahasiswanya dulu
    SQL.execute("SELECT * FROM master_mhs WHERE nama LIKE '%"+wildcard+"%';")
    jumlahRow = SQL.rowcount
    print(jumlahRow, "data ditemukan")

    # ini baru buat nyari data mahasiswa dan juga nilainya
    SQL.execute("SELECT master_mhs.npm, master_mhs.nama, master_mhs.asal, nilai.nama_mata_kuliah, nilai.nilai FROM `master_mhs` " \
    "JOIN nilai ON master_mhs.npm = nilai.npm WHERE master_mhs.nama LIKE '%"+wildcard+"%';")
    hasilnya = SQL.fetchall()

    # INI PENJELASAN PANJANG BUAT DIRI SENDIRI
    # jadi si hasilnya itu outputnya dalam tuple. Nah di for loop itu emg buat ngeiterasi data yang banyak (list, tuple, dictionary, set, sama string)
    # fungsi variabel awal (formatBaris) itu untuk ngeprint masing2 nilai dari tuple tersebut, jadi kayak misah2in si data yang banyak itu
    # nah tapi karena tuple dari SQL itu udh berformat sendiri pake tanda kurung, kutip, dkknya, ini kita pisahin
    # "pisahinnya gmn bang?" dari tuple SQL itu kita kasih masing2 nilainya sbuah variabel, abistu kita format dari stringnya
    # begitu

    indeksData = 0 # buat indeks si datanya 
    for formatBaris in hasilnya:
        dataSebelum = hasilnya[indeksData - 1]
        npmFB, namaFB, asalFB, namaMataKuliahFB, nilaiFB = formatBaris
        npmDS = dataSebelum[0]
        
        if indeksData == 0 and npmFB != npmDS:  # buat inisiasi nama dan nilai baris pertama
            indeksData = indeksData + 1 
            print("\n%s, %s, %s" % (npmFB, namaFB, asalFB))
            print("%s %d" % (namaMataKuliahFB, nilaiFB))
        elif indeksData > 0 and npmFB == npmDS:  # ini baru mulai nyari kesamaan sama npm terus buang namanya kalo masi sama, abistu >0 supaya gak stuck di 0 if pertama terus
            indeksData = indeksData + 1
            print("%s %d" % (namaMataKuliahFB, nilaiFB))
        else:  # ini buat kalo udh ganti nama mahasiswanya
            indeksData = indeksData + 1
            print("\n%s, %s, %s" % (npmFB, namaFB, asalFB))
            print("%s %d" % (namaMataKuliahFB, nilaiFB))

namaMahasiswa = input("Nama : ")
pencarianData(namaMahasiswa)