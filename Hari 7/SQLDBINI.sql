CREATE DATABASE sekolah-kita;

CREATE TABLE master_mhs (
  npm varchar(10) PRIMARY KEY,
  nama_mhs varchar(30) NOT NULL,
  asal varchar(30)
);

CREATE TABLE nilai (
  npm varchar (10),
  nama_mata_kuliah varchar(50) NOT NULL,
  nilai int(11),
  CONSTRAINT fk_npm
  FOREIGN KEY npm
  REFERENCES master_mhs(npm)
);

INSERT INTO master_mhs
VALUES 
("20220001", "Andika Wahyudi", "Jakarta"),
("20220002", "Nandiyah Rizki Sari", "Bandung"),
("20220003", "Muhammad Fadlan Aulia", "Surabaya"),
("20220004", "Dewi Anggraeni", "Semarang"),
("20220005", "Bintang Setia Nugroho", "Palembang"),
("20220006", "Rizki Alif Rahman", "Yogyakarta"),
("20220007", "Aulia Fadilah Sari", "Malang"),
("20220008", "Muhammad Irfan Maulana", "Sragen"),
("20220009", "Widi Cahyono", "Tangerang"),
("20220010", "Novita Nurmalasari", "Bekasi");

INSERT INTO nilai VALUES
("20220001", "Matematika Dasar", 85),
("20220002", "Kalkulus I", 92),
("20220003", "Persamaan Diferensial", 78),
("20220004", "Teori Graf", 95),
("20220005", "Topologi", 88),
("20220001", "Bahasa Indonesia", 90),
("20220002", "Persamaan Diferensial", 85),
("20220003", "Topologi", 92),
("20220004", "Kalkulus I", 88),
("20220005", "Kalkulus II", 95),
("20220006", "Matematika Dasar", 85),
("20220007", "Kalkulus II", 82),
("20220008", "Pengantar Ilmu Antropologi", 98),
("20220009", "Aljabar Linear", 92),
("20220010", "Kalkulus Vektor", 88),
("20220003", "Kalkulus II", 78),
("20220004", "Topologi", 95),
("20220005", "Analisis Ril", 88),
("20220006", "Matematika Diskrit", 85),
("20220007", "Perancangan Algoritma", 82),
("20220009", "Analisis Imajiner", 92),
("20220010", "Persamaan Diferensial", 88);