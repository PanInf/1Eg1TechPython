# PRE
# from math import gcd
# print(gcd(20,15))

# 1. Wybór 2 dużych liczb pierwszych
p = 101
q = 97
print(p,q)

# 2. Obliczyć n = p * q oraz f. Eulera F = (p-1)*(q-1)
n = p * q
F = (p-1)*(q-1)
print(n)
print(F)

# 3. Generowanie klucza publicznego e : NWD(F,e) = 1
from math import gcd
for i in range(2,F):
    if gcd(i,F) == 1:
        e = i
        break
print(e,n)

# 4. Generowanie klucza prywatnego d: e*d % F = 1 (odwrotność modulo)
for j in range(2,F):
    if ((e*j) % F) == 1:
        d = j
        break
print(d,n)

# 5. Przykład działania
# m - message (wiadomość do zaszyfrowania)
# c = m**e % n (cipher - szyfrogram - tekst zaszyfrowany)
# t = c**d % n (text - tekst jawny czyli wiadomość m)

m = input()
cipher = ""
for i in m:
    cipher += chr((ord(i)**e) % n)
print(cipher)

tekst = ""
for j in cipher:
    tekst += chr((ord(j)**d) % n)
print(tekst)




