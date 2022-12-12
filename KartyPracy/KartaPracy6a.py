# Zad 1

# n = int(input())

# suma = 0
# while n>0:
#     suma += n % 10
#     n = n // 10
# print(suma)

# Zad 3
# 6 28 496

# n = int(input())
# suma = 0
# for i in range(1,n):
#     if n % i == 0:
#         suma += i
# if suma == n: print("Jesteś doskonała")
# else: print("No nie jesteś doskonała")
    
# Zad 4
# a = int(input())
# b = int(input())

# while b>0:
#     a, b = b, a % b
# if a==1: print("a i b były względnie pierwsze")
# else: print("a i b nie były względnie pierwsze")

# Zad 5

# n = int(input())
# for i in range(10,20):
#     a = n
#     b = i
#     while a != b:
#         if a > b: a -= b
#         if b > a: b -= a
#     if a == 1:
#         print(f"({n},{i})")


# Zad 6

a = int(input())
b = int(input())

x, y = a, b
while y > 0:
    x, y = y, x % y

c = a // x
d = b // x

print(f"{a}/{b} = {c}/{d}")