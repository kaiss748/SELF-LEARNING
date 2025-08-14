#latihan datetime

import datetime as dt

hari_ini = dt.date.today()
print(hari_ini)
print(f"Hari ini adalah hari : {hari_ini:%A}")

tanggal_brojol = dt.date(2007,10,2)
print(tanggal_brojol)

print("silahkan masukan tanggal lahir anda")
tanggal = int(input("tanggal \t: "))
bulan = int(input("bulan \t\t: "))
tahun = int(input("tahun \t\t: "))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"confirmed, tanggal lahir kamu adalah : {tanggal_lahir:%A}")

print(f"hari ini tanggal : {hari_ini}")
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan_sisa = (umur_hari.days % 365) // 30
print(umur_hari)
print(f"umur anda adalah : {umur_tahun} tahun, {umur_bulan_sisa} bulan")