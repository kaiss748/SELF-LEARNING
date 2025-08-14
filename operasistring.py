#OPERASI DAN MANIPULASI STRING

# 1. Menyambung string (concatenate)
nama_pertama = "Iori"
nama_tengah = "D"
nama_akhir = "Keii"

nama_lengkap = nama_pertama +" "+ nama_tengah +" "+ nama_akhir
print(nama_lengkap)

# 2. Menghitung panjang string
panjang = len(nama_lengkap)
print("panjang dari", nama_lengkap,"=", str(panjang))

# 3. Operator untuk string
# mengecek apakah ada komponen char atau string di dlm string

d = "d"
status = d in nama_lengkap
print(d, "ada di" ,nama_lengkap, "=", str(status))

D = "D"
status = D in nama_lengkap
print(D, "ada di" ,nama_lengkap, "=", str(status))

d = "d"
status = d not in nama_lengkap
print(d, "tidak ada di" ,nama_lengkap, "=", str(status))

# Mengulang string
print("awok"*3)

# Indexing
print("index ke-0 :" + nama_lengkap[0]) # index dr depan
print("index ke-0 :" + nama_lengkap[8])
print("index ke-(-1) :" + nama_lengkap[-1]) # index dr blkg
print("index ke-[0:5] :" + nama_lengkap[0:5]) # range
print("index ke-[0,2,4,6,8,10] :" + nama_lengkap[0:11:2]) # loncat/menjangka

# Item paling kecil
print("paling kecil : " + min(nama_lengkap))
# Item paling besar
print("paling besar : " + max(nama_lengkap))

ascii_code = ord (" ")
print("ASCII code utk spasi adl " + str(ascii_code))
data = 97
print("char untuk ascii code 97 adl " + chr(data))

# 4. operator dalam bentuk method
data = "popo el nino contolo paradino"
jumlah = data.count("o")
print("jumlah o pada " + data + "=" + str(jumlah))

#merubah case dari string
##merubah case dr string

#merubah semua ke uppercase
salam = "hi all"
print ("normal = " + salam)
salam = salam.upper()
print ("upper = " + salam)

#merubah semua ke lower
alay = "Goks, kEren BEut luh!"
print ("normal = " + alay)
alay = alay.lower()
print ("lower = " + alay)

##pengecekan dengan isX method
#contoh pengecekan lowercase
sapaan = "sist!!"
apakah_lower = sapaan.islower() #hasilnya akan bool
print(sapaan + " is lower = " + str(apakah_lower))
apakah_upper = sapaan.isupper() #hasilnya akan bool
print(sapaan + " is upper = " + str(apakah_upper))

#isalpha() ---> untuk mengecek semuanya huruf
#isalnum() ---> huruf dan angka
#isdecimal() ---> angka saja
#isspace() ---> spasi, tab, newline \n
#istitle() ---> semua kata dimulai huruf besar

judul = "Life Is Better Without Feelings"
cek_judul = judul.istitle() #hasilnya akan bool
print(judul + " is title? " + str(cek_judul))

#mengecek komponen startswith() endswith() ---> keren
cek_start = "Serafina Kara".startswith("Serafina")
print("start = " + str(cek_start))

cek_end = "Serafina Kara".endswith("Kara")
print("end = " + str(cek_end))

##penggabungan komponen join() split()
pisah = ['aku','kangen','dia']
gabung = ",".join(pisah)
print(pisah)
print(gabung)

gabung = ' '.join(pisah)
print(gabung)

gabung = ' ehm '.join(pisah)
print(gabung)

gabung = "akucuihbencicuihdia"
print(gabung.split('cuih')) 

#alokasi char rjust() ljust() center()

kanan="kanan".rjust(10)
print("'" + kanan + "'")

kiri="kiri".ljust(10)
print("'" + kiri + "'")

tengah="tengah".center(16,"-")
print("'" + tengah + "'")

#kebilakannya --> strip()
tengah="tengah".strip("-") #menghilangkan tanda -
print("'" + tengah + "'")