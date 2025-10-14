nilai = int(input("masukkan nilai : "))
tugas = int(input("masukkan tugas : "))
nilai_min = int(input("masukkan minimum nilai : "))
tugas_min = int(input("masukkan minimum tugas : "))


if nilai > nilai_min:
    print("lulus")
elif  tugas > tugas_min:
    print("remedial")
else:
    print("tidak lulus")