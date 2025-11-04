# deklarasi var
no_absen = []
nama = []
nilai_1=[]
nilai_2 = []
nilai_3 = [] 
nilai_tugas_akhir = []
# input banyak data
qty = int(input("masukkan banyak data : "))

# input
for i in range(qty):
    print(f"ini adalah no ke {i + 1}")
    no_absen.append(int(input("masukkan absen anda : ")))
    nama.append(input("masukkan nama anda : "))
    nilai_1.append(int(input("masukkan nilai 1 anda : ")))
    nilai_2.append(int(input("masukkan nilai 2 anda : ")))
    nilai_3.append(int(input("masukkan nilai 3 anda : ")))

# proses
for i in range(qty):
    nilai_tugas_akhir.append((nilai_1[i] + nilai_2[i] + nilai_3[i])/3)

# rekap nilai tugas akhir
print("rekap nilai tugas python")
print('='*40)
print("""
no absen | nama lengkap | tugas 1 | tugas 2 | tugas 3 | nilai tugas akhir
""")

for i in range(qty):
    print(f'{no_absen[i]}  {nama[i]} {nilai_1[i]} {nilai_2[i]} {nilai_3[i]} {nilai_tugas_akhir[i]}')

print("="*40)    

