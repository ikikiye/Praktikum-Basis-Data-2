import pymysql.cursors

userDB = pymysql.connect(
  host="localhost",
  user="root",
  password="",
  database="barang"
)

SQL = userDB.cursor()

def tampilData():
    SQL.execute("SELECT * FROM barang")

def editData():
    