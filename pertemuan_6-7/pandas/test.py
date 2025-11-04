import pandas as pd

# deklarasi variabel
no_absen = []
nama = []
nilai_1 = []
nilai_2 = []
nilai_3 = [] 
nilai_tugas_akhir = []
nilai_ujian = []
total_akhir = []
keterangan = []

# input banyak data
qty = int(input("masukkan banyak data : "))

# input data
for i in range(qty):
    print(f"\nini adalah no ke {i + 1}")
    no_absen.append(int(input("masukkan absen anda : ")))
    nama.append(input("masukkan nama anda : "))
    nilai_1.append(int(input("masukkan nilai 1 anda : ")))
    nilai_2.append(int(input("masukkan nilai 2 anda : ")))
    nilai_3.append(int(input("masukkan nilai 3 anda : ")))
    nilai_ujian.append(int(input("masukkan nilai ujian anda : ")))

# proses
for i in range(qty):
    tugas_akhir = (nilai_1[i] + nilai_2[i] + nilai_3[i]) / 3
    nilai_tugas_akhir.append(tugas_akhir)

    total = (tugas_akhir + nilai_ujian[i]) / 2
    total_akhir.append(total)

    if total > 60.0:
        keterangan.append("lulus")
    else:
        keterangan.append("tidak lulus")

# buat DataFrame
data = {
    'no absen': no_absen,
    'nama': nama,
    'nilai tugas akhir': nilai_tugas_akhir,
    'nilai ujian': nilai_ujian,
    'total akhir': total_akhir,
    'keterangan': keterangan
}

data_siswa = pd.DataFrame(data)

