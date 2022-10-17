# Zad 1
# n = int(input("Podaj ile chcesz liczb: "))
# for i in range(n):
#     print(i**3 + 3, end=" ")

# Zad 2
# for i in range(105,1000,15):
#     print(i, end=" ")

# Zad 3 
# n = int(input("Podaj liczbę n:\n"))
# for i in range(1, n+1):
#     if n%i == 0:
#         print(i, end=" ")

# Ankieta
# User wprowadza dwie liczby. 
# Sprawdz czy druga jest 
# o ponad 30% większa niż pierwsza
# WE: p, q
# WY: TAK/NIE

# p, q = int(input()), int(input())
# if (1.3*p > q):
#     print("TAK")
# else:
#     print("NIE")

# 1. pętla liczb dwucyfrowych od 10 do 21
# for i in range(10,22): print(i, end=" ")
# 2. pętla liczb dwucyfrowych nieparzystych od 15 do 31  
# for i in range(15,32,2): print(i, end=" ")
# 3. pętla liczb dwucyfrowych malejąco (step ujemny)
# for i in range(99,9,-1): print(i, end=" ")
# 4. pętla liczb dwucyfrowych malejąco (step dodatni)
# for i in range(10,100,1): print(109-i, end=" ")
# 5. pętla liczb 3-cyfrowych podzielnych przez 20
# for i in range(100, 1000, 20): print(i, end=" ")

# Zad 4

# suma = 0
# for i in range(10, 100):
#     suma = suma + i
# print(suma)

# Zad 5

# n = int(input())
# suma = n*(n+1) // 2
# for i in range(n-1):
#     x = int(input())
#     suma = suma - x
# print(suma)

#Zad 6

# n = 8
# a = 1
# b = 2
# print(a, b, end=" ")
# for i in range(n-2):
#     a, b = b, a+b
#     print(b, end=" ")

# UPGRADE
# 7 - silnia iteracyjnie
# 5! = 1*2*3*4*5 = 120
# n = int(input())
# silnia = 1
# for i in range(1,n+1):
#     silnia = silnia * i
# print(silnia)




