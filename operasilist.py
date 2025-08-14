#OPERASI

data = ["ucup", "otong", "dudung"]

#Mengambil data dr list

data_0 = data[0]
print(f"data index 0 -> {data_0}")

data_terakhir = data[-1]
print(f"data index terakhir -> {data_terakhir}")

data_ucup = data[-3]
print(f"data index ucup -> {data_ucup}")

#MENGAMBIL JUMLAH DATA DALAM LIST
panjang_data = len(data)
print(f"panjang data -> {panjang_data}")

#MANIPULAS DATA LIST

#menabah item pada list sesuai posisi
#di tengah list
print(f"\ndata sebelum ditambah -> {data}")

data.insert(1, "nunung")
print(f"\ndata setelah ditambah -> {data}")

#di akhir list
data.append("kento")
print(f"\ndata setelah ditambah lagi -> {data}")

#menambahkan list dengan list
data_baru = ["ujang", "pikri", "esap"]
data.extend(data_baru)
print(f"\ndata gabungan = \n{data}")

#merubah data
#merubah data 2 menjadi sopyan
data[2] = "sopyan"
print(f"\ndata setelah dirubah =\n {data}")

#menghapus data
data.remove("kento")
print(f"\ndata remove =\n {data}") #HURUF PADA DATA HARUS SESUAI

#menghapus data palling belakang
data.pop()
print(f"\ndata remove terakhir =\n {data}") #HURUF PADA DATA HARUS SESUAI


data_angka = [1,2,3,4,6,9,2,3,5,6,7,4,3]
print(f"data angka -> {data_angka}")


#count data -> menghitung berapa kali data angka keluar
jumlah_data_4 = data_angka.count(4)
jumlah_data_3 = data_angka.count(3)

print(f"jumlah angka 3 -> {jumlah_data_3}")
print(f"jumlah angka 4 -> {jumlah_data_4}")

#ambil posisi data
data_terbaru = ["maman", "nopal", "kipli", "kelek"]
print(f"data = {data_terbaru}")

index_kipli = data_terbaru.index("kipli")
print(f"index si kipli -> {index_kipli}")
index_nopal = data_terbaru.index("nopal")
print(f"index si nopal -> {index_nopal}")

#Mengurutkan list
print(f"data angka sebelum disort -> {data_angka}")
data_angka.sort()
print(f"data angka setelah disort -> {data_angka}")

print(f"data_terbaru = {data_terbaru}")
data_terbaru.sort()
print(f"data_terbaru stlh sort = {data_terbaru}")

#membalik list
data_angka.reverse()
print(f"data angka setelah direverse -> {data_angka}")
data_terbaru.reverse()
print(f"data_terbaru stlh reserve = {data_terbaru}")
