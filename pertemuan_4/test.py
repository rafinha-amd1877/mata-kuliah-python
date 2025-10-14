# nilai = 5
# if nilai > 0:
#     print("bilangan positif")
# nilai = -1
# if nilai > 0:
#     print("bilangan positif")


nilai = int(input("input nilai : "))
nilai_min = int(input('input nilai minimum : '))

if nilai > nilai_min:
    print(nilai, 'lebih besar dari', nilai_min, 'status : anda lulus')
else:
    print(nilai, 'kurang dari', nilai_min)

