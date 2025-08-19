#width and multiline

#data
data_nama = "konol otol"
data_umur = 17
data_tinggi = 167
data_nomor_sepatu = 43

#string standard
print(5*"-"+"DATA STRING"+5*"-")
data_string = f"nama = {data_nama}, umur = {data_umur}, tinggi = {data_tinggi}, sepatu = {data_nomor_sepatu}"
print(data_string)

#string multiline -> using \n
data_string = f"nama = {data_nama}, \numur = {data_umur}, \ntinggi = {data_tinggi}, \nsepatu = {data_nomor_sepatu}"
print("\n"+5*"-"+"DATA MULTILINE"+5*"-")
print(data_string)

#string multiline triplets
data_string = f"""nama = {data_nama}
umur = {data_umur}
tinggi = {data_tinggi}
sepatu = {data_nomor_sepatu}
"""
print("\n"+5*"-"+"DATA MULTILINE"+5*"-")
print(data_string)

#mengatur lebar -> using :>
data_nama = "otol"
data_string = f"""
nama = {data_nama:>5}
umur = {data_umur:>5}
tinggi = {data_tinggi:>5}
sepatu = {data_nomor_sepatu:>5}
"""
print("\n"+5*"-"+"DATA MULTILINE"+5*"-")
print(data_string)
