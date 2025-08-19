#Perulangan (Loop)

#for kondisi :
#aksi

# ini dengan method list
angka2_list = [0,1,2,3,4,5,6]
print (angka2_list)

for i in angka2_list:
    print(f"i sekarang -> {i}")

print("akhir dr program 1")

#method range
angka2_range = range(6)
for i in range (6):
    print(f"i sekarang -> {i}")

print("akhir dr program 2")

tahun_lahir = 2007


# Membuat tabel perkalian sederhana
# Loop luar untuk baris (angka 1 sampai 3)
for i in range(1, 4):
# Loop dalam untuk kolom (angka 1 sampai 3)
    for j in range(1, 4):
# end='\t' membuat print tidak ganti baris, tapi memberi tab
        print(f"{i}x{j}={i*j}", end='\t')
# Setelah loop dalam selesai, ganti baris
print() # print kosong akan membuat baris baru
