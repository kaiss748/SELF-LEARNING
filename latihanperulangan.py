#Latihan perulangan sgitiga

sisi = 10   

#MENGGUNAKAN FOR
#dummy variabel
print("===awal dari for===")
count = 1
for i in range(sisi):
    print("*"*count)
    count += 1

print("===akhir dari for===")

#MENGGUNAKAN WHILE
#HANYA GANJIL SAJA
print("===awal dari while===")
count = 1
spasi = int(sisi/2)

while True:
    if (count %2):
        print(" "*spasi,"*"*count) #akan print jika ganjil
        spasi -= 1
        count += 1  

    else: #kembali ke atas jika genap
        count += 1
        continue

    if count > sisi: #akan break ketika melebihi sisi
        break

print("===akhir dari while===")


