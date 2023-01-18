# from hashlib import md5, sha1
# user = kamilek
# pass = nigeria321234
# print(md5(b"nyGus!67").hexdigest())
# print(md5(b"myGus!67").hexdigest())

# NWD(a,b) = n

# x*a + y*b = NWD(a,b)

# 8*7 - 5*11 = NWD(7,11) = 1  # x=8 y=-5

# biorę 2 najlepiej duże liczby pierwsze 
p = 13
q = 11

# szukam F = (p-1) * (q-1) tzw funkcja Eulera
F = (p-1) * (q-1)

# obliczam moduł n=p*q
n=p*q

# wyznaczamy klucz publiczny e, ma on być względnie pierwszy z F
# algorytm euklidesa.... 
# NWD(e,F) = 1
# np NWD(143,7) = 1
e = 7

# wyznaczamy klucz prywatny d
# NWD(d,n) = 1


