#---LIST---

#kumpulan data numbers
data_angka = [1, 2, 3, 4]
print(data_angka)

#kumpulan data str
data_str = ["ucup", "otong", "odah"]
print(data_str)

#kumpulan data bool
data_bool = [True, False, True, False]
print(data_bool)

#kumpulan campuran
data_campuran = [1,"bala bala",2,"cireng",3,"kepin",4,True]
print(data_campuran)

#cara alternatif membuat list
data_range = range(0, 8, 2) #-> start, stop, step
data_list = list(data_range)
print(data_list)

#membuat list dengan for loop, list comperhansion
list_pake_for = [i**2 for i in range(0,10)]
print(list_pake_for)

#membuat list pake for, pake if
list_pake_for_if = [i for i in range(0,10) if i != 5] #!=5, -> meniadakan angka 5
print(list_pake_for_if)

#untuk ganijl
list_pake_for_if = [i for i in range(0,10) if i%2 == 0] #i%2 == o, adalh bilangan yg habis di bagi 2
print(list_pake_for_if)

#untuk genap
list_pake_for_if = [i for i in range(0,10) if i%2 != 0] 
print(list_pake_for_if)