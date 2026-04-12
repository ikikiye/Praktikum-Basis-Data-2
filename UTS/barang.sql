CREATE TABLE barang (
    kode_barang varchar(50) PRIMARY KEY,
    deskripsi varchar(255),
    harga_jual int
);

INSERT INTO barang (kode_barang, deskripsi, harga_jual)
VALUES 
("BR001", "Pulpen", 2000),
("BR002", "Buku", 4000);