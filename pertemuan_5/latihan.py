print('GEROBAK FRIED CHICKEN')
print('='*40)
print("""
KODE | JENIS POTONG | HARGA
================================
  D  | DADA         | RP. 2,500      
  S  | SAYAP        | RP. 2,000      
  P  | PAHA         | RP. 1,500      
================================
""")

qty = int(input('Banyak jumlah yang di pesan : '))
for q in range(qty):
    print(f"Pesanan ke : {q+1}")
    kd_potong = input("Kode potong [D/S/P] : ")
    banyak_potong = int(input("Banyak potong : "))
    print('='*40)

print(qty)

if kd_potong == 'D':
    harga_satuan = 25000
elif kd_potong == 'S':
    harga_satuan = 20000
elif kd_potong == 'P':
    harga_satuan = 15000
else:
    harga_satuan = 0
    
    