#FORMAT STRING

#contoh gerenic
#a. string

nama = "chels"
format_str = f"hai {nama}"

print(format_str)

#c. boolean
boolean = True
format_str = f"boolean = {boolean}"
print(format_str)

#b. angka
angka = 29
format_str = f"angka = {angka}"
print(format_str)

#c. angka bulat
angka = 15
format_str = f"bilangan bulat = {angka:d}"
print(format_str)

#d. bilangan ribuan
angka = 2500
format_str = f"ribuan = {angka:,}" #memberi koma pada bilangan ribuan
print(format_str)

#e. bilangan desimal
angka = 2902.53412
format_str = f"desimal = {angka:.1f}" #fungsi f, untuk memberi nilai stlh titik
print(format_str)

#f. menampilkan leading zero
angka = 2902.53412
format_str = f"desimal = {angka:09.3f}" #fungsi 0, memberi nilai didepan angka pertama
print(format_str)

#g. menampilkan tanda + atau -
minus = -7
plus = 7.45678
format_minus = f"minus = {minus:+2d}"
format_plus = f"plus = {plus:+.3f}"

print(format_minus)
print(format_plus)

#h. menformat persen
persentase = 0.074
format_persen = f"persen = {persentase:.3%}"
print(format_persen)

#i. melakukan operasi aritmatika didalam placeholder
harga = int(input("masukkan harga barang : "))
jumlah = int(input("masukkan jumlah barang : "))

total_harga = f"total harga = {harga*jumlah}"
print(total_harga)

#j. format angka lain (binary, octal, hexadecimal)
angka = int(input("masukkan angka : "))
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hex = f"hexadecimal = {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hex)

