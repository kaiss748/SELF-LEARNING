print('---For Loop---')
kumpulan_angka = [2,5,6,3,9,1]
for angka in kumpulan_angka:
    print(f"angka -> {angka}")

peserta = ["ucup","otong","sabda","pepen"]
for nama in peserta:
    print(f"nama -> {nama}")

#for loop dan range
print('\n---For Loop and Range---')

kumpulan_angka = [4,3,2,1,5,6]
panjang = len(kumpulan_angka)
for i in range(panjang):
    print(f"angka -> {kumpulan_angka[i]}")

print('\n---While Loop---')
kumpulan_angka = [4,3,2,1,5,6]
panjang = len(kumpulan_angka)
i = 0

while i < panjang:
    print(f"angka -> {kumpulan_angka[i]}")
    i += 1

print('\n---Comprehension---')
data =["ucup",1,2,3,"epan"]

[print(i) for i in data]
[print(f"data={i}") for i in data]

"""
Dua duanya bisa, terserah mau yang mana
"""
angka = [2,5,6,3,9,1]
angka_kuadrat = [i**2 for i in angka]
print(angka_kuadrat)
"""
membuat list baru dari list, dan menjadikan bilangan kuadrat
"""


print('\n---Enumerate---')
data_list = ["ucup",1,2,3,"otong"]

for index,data in enumerate(data_list):
    print(f"index = {index}, data = {data}")

"""
enumerate() itu sebenarnya bukan pengganti for loop,
tapi alat bantu yang bikin for loop lebih rapi kalau kamu butuh index + value sekaligus
"""