import pymysql.cursors

userDB = pymysql.connect(
  host="localhost",
  user="root",
  password="",
  database="sekolah-kita"
)

SQL = userDB.cursor()
SQL.execute("select * from master_mhs order by nama_mhs")
hasilnya = SQL.fetchall()

for x in hasilnya:
    print(x)

def pencarian_data(wildcard):
    SQL.execute("select * from master_mhs where nama_mhs like '%"+wildcard+"%'")
    rowrow = SQL.rowcount
    print("jumlah row = ", rowrow)
    hasilnya = SQL.fetchall()
    for x in hasilnya:
        print(x)

def tambah_data(jumlahData):
    for i in range(jumlahData):
        NPM = input("Input NPM = ")
        Nama = input("Input Nama = ")
        Asal = input("Input Asal = ")
        SQL.execute("insert into master_mhs (nim, nama_mhs, asal) values ('"+NPM+"','"+Nama+"','"+Asal+"')")
        userDB.commit()
    print(jumlahData, "data berhasil ditambah")

def hapus_npm(NPM):
    SQL.execute("delete from master_mhs where nim="+NPM)
    userDB.commit()
    print("data berhasil dihapus")

wildcard = int(input("wildcard = "))
tambah_data(wildcard)