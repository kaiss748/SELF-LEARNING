# operasi logika atau boolean

# not, or, xor

print('---not---')
a = True
c = not a
print('data a = ',a)
print('-----NOT')
print('data c = ',c)

#AND (jika keduanya true, maka hasilnya adl "true", selainnya "false")
print('----AND----')
a = False
b = False
c = a and b
print(a, 'and', b, '=', c)
a = True
b = False
c = a and b
print(a, ' and', b, '=', c)
a = False
b = True
c = a and b
print(a, 'and', b, ' =', c)
a = True
b = True
c = a and b
print(a, ' and', b, ' =', c)

#OR (jika salah satunya true, maka hasilnya adl "true")
print('----OR----')
a = False
b = False
c = a or b
print(a, 'or', b, '=', c)
a = True
b = False
c = a or b
print(a, ' or', b, '=', c)
a = False
b = True
c = a or b
print(a, 'or', b, ' =', c)
a = True
b = True
c = a or b
print(a, ' or', b, ' =', c)

#XOR (jika salah satunya true, maka hasilnya "true", jika 2 buah nilai sama maka "false")
print('----XOR----')
a = False
b = False
c = a ^ b
print(a, 'xor', b, '=', c)
a = True
b = False
c = a ^ b
print(a, ' xor', b, '=', c)
a = False
b = True
c = a ^ b
print(a, 'xor', b, ' =', c)
a = True
b = True
c = a ^ b
print(a, ' xor', b, ' =', c)