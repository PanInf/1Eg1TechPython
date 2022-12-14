# Zad 1

# a = int(input())
# b = int(input())
# c = int(input())

# # arytm
# if b - a == c - b: print("C jest arytmetyczny")

# # geom
# if b / a == c / b: print("C jest geometryczny")

# # rosnący
# if a < b < c: print("C jest rosnący")

# # malejący
# if a > b and b > c: print("C jest rosnący")

# Zad 2

# suma = 0
# for i in range(100, 1000):
#     if i % 8 == 0 and i % 16 != 0:
#         suma = suma + i
# print(suma)

# Zad 3

# for i in range(99,9,-1):
#     if i % 7 == 0:
#         wielok = i
#         break

# ilość = 0
# for i in range(1000, 10000):
#     if i % wielok == 0:
#         ilość = ilość + 1

# print(ilość)

# Zad 4

# ilosc = 0
# for i in range(10,100):
#     if i // 10 >= 2 * (i % 10):
#         ilosc += 1
# print(ilosc)


# Zad 6
# n = int(input())
# suma = 0
# i = 1
# while n > 0:
#     if i % 19 == 0:
#         suma = suma + i
#         n = n - 1
#     i = i + 1
# print(suma)


# zad 8

n = int(input())
suma  = 0
czynnik = -1
for i in range(n):
    czynnik = czynnik * (-1)
    suma = suma + (3*i+2) * czynnik
print(suma)