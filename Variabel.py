#variabel adl tempat menyimpan data

#menaruh assignment nilai
a = 10
x = 5
panjang = 1000

#pemanggilan pertama
print ("nilai a =", a)
print ("nilai x = ", x)
print ("nilai panjang = ", panjang)

#penamaan
nilai_y =  15 #bisa menggunakan underscore
juta10 = 10000000 #tidak boleh angka di depan
nilaiz = 17.5 #bgni juga bole

#pemanggilan kedua
print ("nilai a =", a)
a = 7
print ("nilai a =", a)

#assignment indirect
b = a
print ("nilai b = ", b)

#compile python ke bytecode


#tipe data : integer (angka satuan)
data_int = 11
print ("data = ", data_int)
print ("- bertipe : ", type (data_int))

#tipe data : float (angka pecahan)
data_float = 7.5
print ("data = ", data_float)
print ("- bertipe : ", type (data_float))

#tipe data : string (kumpulan karakter/text)
data_string = "monyet"
print ("data = ", data_string)
print ("- bertipe : ", type (data_string))

#tipe data : boolean (binary true/false)
data_bool = True
print ("data = ", data_bool)
print ("- bertipe : ", type (data_bool))

##tipe data khusus

#bilangan kompleks
data_complex = complex (5,6)
print ("data = ", data_complex)
print ("- bertipe : ", type (data_complex))

#tipe data dari bahasa C

from ctypes import c_double

data_c_double = c_double (10.5)
print ("data = ", data_c_double)
print ("- bertipe : ", type (data_c_double))

#belajar casting
#merubah dari satu tipe ke tipe data lain

#INTEGER
print ("----INTEGER----")
data_int = 11;
print("data = ", data_int, ",type = ",type(data_int))

data_float = float (data_int)
data_string = str (data_int)
data_bool = bool (data_int)
print ("data = ", data_float, ",type =", type (data_float))
print ("data = ", data_string, ",type =", type (data_string))
print ("data = ", data_bool, ",type =", type (data_bool)) #False jika bernilai 0

#FLOAT
print ("----FLOAT----")
data_float = 8.9    ;
print("data = ", data_float, ",type = ",type(data_float))

data_int = int (data_float)
data_string = str (data_float)
data_bool = bool (data_float)
print ("data = ", data_int, ",type =", type (data_int)) #akan dibulatkan kebawah
print ("data = ", data_string, ",type =", type (data_string))
print ("data = ", data_bool, ",type =", type (data_bool)) #False jika float bernilai 0

#BOOLEAN
print("----BOOLEAN----")
data_bool = True;
print ("data = ", data_bool, ",type = ",type(data_bool))

data_int = int (data_bool)
data_string = str (data_bool)
data_float = float (data_bool)
print ("data = ", data_int, ",type =", type (data_int)) 
print ("data = ", data_string, ",type =", type (data_string))
print ("data = ", data_float, ",type =", type (data_float)) 

#STRING
print ("----STRING----")
data_string = "lebah ganteng";
print ("data = ", data_string, ",type = ",type(data_string))

data_int = int (data_string) #string harus angka
data_float = float (data_string) #string harus angka
data_bool = bool (data_string) #False jika string kosong
print ("data = ", data_int, ",type =", type (data_int)) 
print ("data = ", data_float, ",type =", type (data_float)) 
print ("data = ", data_bool, ",type =", type (data_bool))

