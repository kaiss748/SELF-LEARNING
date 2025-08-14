#teknik duplikat list

a= ["tong", "ucup", "pona"]
print(f"a = {a}")

b = a #pass by reference
print(f"b = {a}")


#kita merubah member dari a

#ini akan mengubah kedua list
a[1] = "mikael"
b.sort()
print(f"a = {a}")
print(f"b = {b}")

#addres dari kedua list
print(f" addres a -> {hex(id(a))}")
print(f" addres b -> {hex(id(b))}")

#menduplikat list dengan copy
# -> fungsi a.copy() ini menduplikat list dengan addres yg berbeda.
print("membuat list c dengan a.copy()")
c = a.copy()
print(f" addres a -> {hex(id(a))}")
print(f" addres b -> {hex(id(b))}")
print(f" addres c -> {hex(id(c))}")
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")


print("kita ubah data 0 ")
c[0] = "yoru"

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print("kita ubah data  ")
c[1] = "kotoha"

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

