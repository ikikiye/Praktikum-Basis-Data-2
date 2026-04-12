import pymysql.cursors

userDB = pymysql.connect(
  host="localhost",
  user="root",
  password="",
  database="buku_db"
)

SQL = userDB.cursor()

SQL.execute("SELECT * FROM barang")
hasil = SQL.fetchall()

for x in hasil:
    print(x)