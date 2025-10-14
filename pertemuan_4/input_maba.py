print("""
============================================================
    SELAMAT DATANG DI UNIVERSITAS BINA SARANA INFORMATIKA   
============================================================   
""")

nis = input("masukkan NIS anda : ")
nama = input("masukkan nama anda : ")
kode_jurusan = input(
    "masukkan kode jurusan [SI/si = Sistem Informasi, IF/if = Informatika, SIA/sia = Sistem Informasi Akuntansi] : ")


print("""
============================================================
                        HASIL
============================================================      
""")

if kode_jurusan == 'SI' or kode_jurusan == 'si':
    nama_jurusan = "Sistem Informasi"
    ukt = 2400000
elif kode_jurusan == 'IF' or kode_jurusan == 'if':
    nama_jurusan = "Informatika"
    ukt = 2500000
elif kode_jurusan == 'SIA' or kode_jurusan == 'sia':
    nama_jurusan = "Sistem Informasi Akuntansi"
    ukt = 2600000
else:
    nama_jurusan = "kode yang anda pilih tidak sesuai"
    ukt = 0
    
    
print("kode jurusan yang anda pilih adalah", kode_jurusan)
print("jurusan yang anda pilih adalah", nama_jurusan)
print("jumlah ukt dari jurusan", nama_jurusan, 'adalah', f"{ukt:,}")

