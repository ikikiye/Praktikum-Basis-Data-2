import pymysql.cursors

userDB = pymysql.connect(
  host="localhost",
  user="root",
  password="",
  database="sekolah_kita"
)

SQL = userDB.cursor()

wildcard = input("Nama:")
SQL.execute("SELECT * FROM master_mhs WHERE nama_mhs LIKE '%"+wildcard+"%';")
hasilnya=SQL.fetchall()
jumlahRow = SQL.rowcount

if jumlahRow == 0:
    print("Data tidak ada")
else:
    for wow in hasilnya:
        npm, nama, alamat = wow
        print("%s, %s, %s" % (npm, nama, alamat))