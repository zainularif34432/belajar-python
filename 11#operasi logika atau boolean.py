# operasi logika atau boolean

#not, or, and, xor

#Not
print('=====NOT=====')
a = True
c = not a
print('data a =',a)
print('-----------Not')
print('data c =',c)


#Or(Jika salah satu true, maka hasilnya adalah true)
print('=====OR=====')
a = False
b = False
c = a or b
print(a,'or',b,'=',c)

a = False
b = True
c = a or b
print(a,'or',b,' =',c)

a = True
b = False
c = a or b
print(a,'or',b,' =',c)

a = True
b = True
c = a or b
print(a,'or',b,'  =',c)

#AND(Jika dua buah nilai true, maka hasil true)
print('=====AND=====')
a = False
b = False
c = a and b
print(a,'and',b,'=',c)

a = False
b = True
c = a and b
print(a,'and',b,' =',c)

a = True
b = False
c = a and b
print(a,'and',b,' =',c)

a = True
b = True
c = a and b
print(a,'and',b,'  =',c)


#XOR(akan true jika salah satu true, sisanya false)
print('=====XOR=====')
a = False
b = False
c = a ^ b
print(a,'xor',b,'=',c)

a = False
b = True
c = a ^ b
print(a,'xor',b,' =',c)

a = True
b = False
c = a ^ b
print(a,'xor',b,' =',c)

a = True
b = True
c = a ^ b
print(a,'xor',b,'  =',c)