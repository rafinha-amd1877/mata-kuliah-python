#list
int_list = [1,2,3] #list integer
mix_list = [1,0.1,'hallo'] #list campuran
nested_list = ['hallo', [1,2,3], ['world',1,1.5]]

# print(int_list)
# print(mix_list)
# print(nested_list)

# mengakses list

print(nested_list[1]) # mengakses list index dan index ke sekian

my_list = ['p','y','t','h','o','n']

# print(my_list[-1])

# jika negatif maka dia akan mengambil mundur dari index 0

# slicing

print(len(my_list))
print(my_list[1:5])

print(my_list[:3]) #mengambil dari index 0 sampai sebelum index yang ditentukan misal :3 maka akan berhenti sebelum index 3

print(my_list[3:]) #mengambil dari index yang ditentukan sampai selesai

# menambahkan anggota list
# append() = menambahkan anggota ke list
# extend() = menambahkan list ke list

ganjil = [1,3,5]
print(ganjil)
ganjil.append(7)
print(ganjil)
ganjil.extend([9,11,13])
print(ganjil)
