import pymysql

userDB = pymysql.connect(
  host="localhost",
  user="root",
  password="",
  database="barang"
)

SQL = userDB.cursor()

def ambilBarang():
    SQL.execute("SELECT * FROM barang")
    dataBarang = SQL.fetchall()
    banyakBaris = SQL.rowcount
    return dataBarang, banyakBaris

def ambilField():
    SQL.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'barang' ")
    namaKolom = SQL.fetchall()
    banyakKolom = SQL.rowcount
    return namaKolom, banyakKolom