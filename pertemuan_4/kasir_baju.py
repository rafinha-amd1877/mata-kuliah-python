print("""
============================================================
                SELAMAT DATANG DI TOKO BAJU
============================================================      
""")


kode_baju = input("masukkan kode baju [AD/ad, PM/pm] : ")
ukuran = input ("masukkan ukuran baju [S/s, M/m] : ")


if kode_baju == 'AD' or kode_baju == 'ad':
    merk = 'Adidas'
    if ukuran == 'S' or ukuran =='s':
        harga = 50000
    elif ukuran == 'M' or ukuran == 'm':
        harga = 45000
    else:
        harga = 0
elif kode_baju == 'PM' or kode_baju == "pm":
    merk = 'PUMA'
    if ukuran == 'S' or ukuran =='s':
        harga = 100000
    elif ukuran == 'M' or ukuran == 'm':
        harga = 90000
    else:
        harga = 0
else:
    merk = "kode tidak sesuai"
    harga = 0
    
print("""
============================================================
                    HASIL
============================================================      
""")

print('Merk baju yang anda pilih adalah', merk)
print('ukuran baju yang anda pilih adalah', ukuran)
print("harga baju dengan ukuran yang anda pilih adalah", harga)