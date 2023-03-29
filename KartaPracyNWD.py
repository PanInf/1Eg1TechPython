róć ułamek
# from math import gcd
# a, b = map(int, input().split("/"))
# dz = gcd(a,b)
# c = a // dz
# d = b // dz

# print(f"{a}/{b} = {c}/{d}")
           
# 2. Zamień ułamek niewłaściwy na mieszanke i skróć

from math import gcd
a, b = map(int, input().split("/"))

c = a // b
l = a % b
m = b

dz = gcd(l,m)
x = l // dz
y = m // dz

print(f"{a}/{b} = {c} {x}/{y}")

# 3. Pomnóż dwa ułamki i skróć

# 4. Dodaj ze sobą 3 ułamkix
# a, b, c
# a*b*c
