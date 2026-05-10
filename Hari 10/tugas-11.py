import pymysql.cursors

userDB = pymysql.connect(
  host="localhost",
  user="root",
  password="",
  database="sekolah_kita"
)

SQL = userDB.cursor()

nis = input("NIS : ")
SQL.execute("SELECT * FROM master_mhs WHERE npm LIKE '%"+nis+"%';")
pencarian = SQL.fetchall()
banyakData = SQL.rowcount

for data in pencarian:
    print(data)

if banyakData > 0:
    nama = input("Nama :")
    asal = input("Asal :")

    if len(nama)>0:
        namanya=nama
    else:
        namanya=data[1]
    
    if len(asal)>0:
        asalnya=asal
    else:
        asalnya=data[2]
    
    SQL.execute("UPDATE master_mhs SET nama_mhs = '"+namanya+"', asal ='"+asalnya+"' where npm='"+nis+"'")
    userDB.commit()
    print("Data sudah berhasil diupdate")
else:
    print("Data tidak ditemukan")