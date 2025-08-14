data_0 = [1, 2]
data_1 = [3, 4]

data_list_biasa = [1, 2, 3, 4]
print(f"list biasa -> {data_list_biasa}")

data_2d = [data_0, data_1, 10] # -> list ini bisa dicampur apa saja, baik list yg lain, angka, dll.
data_2d_copy = data_2d.copy()
print(f"data 2d -> {data_2d}")
print(f"data 2d copy -> {data_2d_copy}")

data = data_2d[0] 
print(f"data = {data}")

data = data_2d[0][0]
print(f"data = {data}")

"""
fungsi [0] ini untuk mengambil index pertama dalam data_2d
jika menggunakannya 2 kali maka dia mengambil index di dalam data_0
"""
#address
print(f"address asli = {hex(id(data_2d))}")
print(f"address copy = {hex(id(data_2d_copy))}")

print("address member ke-1")
print(f"address asli = {hex(id(data_2d[0]))}")
print(f"address copy = {hex(id(data_2d_copy[0]))}")

print(f"data 2d -> {data_2d}")
print(f"data 2d copy -> {data_2d_copy}")

data_2d[1][0] = 5
data_2d_copy[2] = 9
"""
data yang selain list tidak ikut terubah ketika dicopy seperti 10 -> 9
"""

"""
Sulosinya menggunakan deepcopy
"""

from copy import deepcopy

data_2d = [data_0, data_1, 10]
data_2d_deepcopy = deepcopy(data_2d)
print(f"address asli = {hex(id(data_2d))}")
print(f"address deep = {hex(id(data_2d_deepcopy))}")

print("address member ke-1")
print(f"address asli = {hex(id(data_2d[0]))}")
print(f"address deep = {hex(id(data_2d_deepcopy[0]))}")

data_2d[1][0] = 30
print(f"data 2d -> {data_2d}")
print(f"data 2d copy -> {data_2d_copy}")
print(f"data 2d deep -> {data_2d_deepcopy}")
#contoh kegunaan

peserta_0 = ["maman",18,"laki-laki"]
peserta_1 = ["ucup",20,"laki-laki"]
peserta_2 = ["kotoha",19,"wanita"]

list_peserta = [peserta_0, peserta_1,peserta_2]
print(f"list peserta -> {list_peserta}")

for peserta in list_peserta:
    print(f"nama -> {peserta[0]}")
    print(f"umur -> {peserta[1]}")
    print(f"gender -> {peserta[2]}\n")

#dengan reference

list_copy = list_peserta.copy();
print(f"peserta -> {list_copy}")
peserta_0[0] = "kento"
print(f"peserta -> {list_copy}")
print(f"peserta -> {list_peserta}")
