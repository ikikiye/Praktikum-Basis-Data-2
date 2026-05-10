import pymysql.cursors
import os

userDB = pymysql.connect(
  host="localhost",
  user="root",
  password="",
  database="barang"
)

SQL = userDB.cursor()

def userInterface():
    print("========================================")
    print("Aplikasi Pengelolaan Data Barang")
    print("\nMenu")
    print("1. Entri Data\n2. Tampil Data\n3. Hapus Data\n4. Edit Data\n5. Keluar")
    print("========================================\n")

def cekInputKosong(dataDiambil, editDeskripsi, editHarga):
    if len(editDeskripsi) > 0:
        deskripsiBaru = editDeskripsi
    else:
        deskripsiBaru = dataDiambil[1]
    
    if len(editHarga) > 0:
        hargaBaru = editHarga
    else:
        hargaBaru = dataDiambil[2]
    
    return (deskripsiBaru, hargaBaru)

def ambilData(wildcard):
    if len(wildcard) > 0:
        SQL.execute("SELECT * FROM barang WHERE kode LIKE '%"+wildcard+"%';")
    else:
        SQL.execute("SELECT * FROM barang")
    dataDiambil = SQL.fetchall()
    banyakData = SQL.rowcount
    return (dataDiambil, banyakData)

def tampilData():
    semuaData = ""
    dataDiambil, banyakData = ambilData(semuaData)
    print()
    print(banyakData, "data ditemukan\n")
    for data in dataDiambil:
        print(data)

def tambahData():
    banyakTambahanData = int(input("Banyak data yang akan ditambahkan: "))
    for inkremen in range(banyakTambahanData):
        tambahKode = input("\nKode (F1,varchar): ")
        tambahDeskripsi = input("Deskripsi (F2,varchar): ")
        tambahHarga = input("Harga (F3,int): ")
        SQL.execute("INSERT INTO barang (kode, deskripsi, harga) VALUES ('"+tambahKode+"', '"+tambahDeskripsi+"', "+tambahHarga+");")
        inkremen = inkremen + 1
    userDB.commit()
    print(banyakTambahanData, "data ditambahkan")

def editData():
    kodeDataYangDiedit = input("Kode data yang ingin diedit: ")
    dataDiambilTuple, banyakData = ambilData(kodeDataYangDiedit)
    dataDiambil = dataDiambilTuple[0]
    editDeskripsi = input("Deskripsi baru: ")
    editHarga = input("Harga baru: ")
    deskripsiBaru, hargaBaru = cekInputKosong(dataDiambil, editDeskripsi, editHarga)
    SQL.execute("UPDATE barang SET deskripsi = '"+deskripsiBaru+"', harga = "+str(hargaBaru)+" WHERE kode = '"+kodeDataYangDiedit+"'")
    userDB.commit()
    print("Data berhasil diedit")

def hapusData():
    kodeDataYangDihapus = input("Kode data yang ingin dihapus: ")
    SQL.execute("DELETE FROM barang WHERE kode = '"+kodeDataYangDihapus+"'")
    userDB.commit()
    print("Data berhasil dihapus")

while True:
    os.system('clear')
    userInterface()
    pilihanMenu = int(input("Pilihan Menu: "))
    if pilihanMenu == 1:
        tambahData()
        input()
        os.system('clear')
    elif pilihanMenu == 2:
        tampilData()
        input()
        os.system('clear')
    elif pilihanMenu == 3:
        hapusData()
        input()
        os.system('clear')
    elif pilihanMenu == 4:
        editData()
        input()
        os.system('clear')
    elif pilihanMenu == 5:
        break
    else:
        print("Menu tersebut tidak tersedia\nProgram dihentikan")
        break