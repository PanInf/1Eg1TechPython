li, mi = int(input()), int(input())
a, b = li, mi
from math import ceil, gcd
L = []
while li > 0:
    x = ceil(mi/li)
    L.append(x)
    nww = mi * x // gcd(mi, x)
    # li/mi - 1/x
    li = (nww // mi) * li
    mi = nww
    y = nww // x
    li = li - y

print(f"{a}/{b}", end= " = ")
for x in L:
    print(f"1/{x}", end= " + ")