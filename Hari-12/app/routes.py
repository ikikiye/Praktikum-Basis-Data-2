from flask import render_template
from app import app
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

def gabungKeList(namaKolom, dataBarang):
    listBarang = []
    listKolom = []
    for kolom in namaKolom:
        listKolom.append(f"{kolom}")
    for barang in dataBarang:
        listBarang.append(dict(zip(listKolom, barang)))
    return(listBarang,listKolom)

@app.route("/")
@app.route("/index")
def index():
   dataBarang = ambilBarang()
   namaKolom = ambilField()
   dataTabel = gabungKeList(dataBarang[0], namaKolom[0])
   return render_template('index.html', dataTabel=dataTabel)

"""@app.route("/random")
def defRandom():
    randomNum = random()
    return render_template('index.html', randomNum=randomNum)"""
