# for i in range(1, 11):
#     for j in range(1, 11):
#         print(i*j, end="\t")
#     print()

# narysuj takie oto figury - user podaje n (ilość wierszy)

# *
# **
# ***
# ****

# ***
# **
# *

#   *
#  **
# ***

# ***
#  **
#   *

# n = int(input())
# for i in range(n):
#     for j in range(i+1):
#         print("*", end="")
#     print()
    
# print()
# print()

# for i in range(n):
#     for j in range(n-i):
#         print("*", end="")
#     print()

# print()
# print()

# for i in range(n):
#     for j in range(n-i-1):
#         print(" ", end="")
#     for k in range(n-i-1, n):
#         print("*", end="")
#     print()


# print()
# print()

# for i in range(n):
#     for j in range(n-i-1):
#         print("*", end="")
#     for k in range(n-i-1, n):
#         print("", end="")
#     print()

# Zad 1

# n = int(input())
# for i in range(n):
#     print("*-|", end="")
# print()

# Zad 2 - PRE

# print("Bartosz" + 5)
# print("Bartosz" * 5)
# print("*"*3)

# n = int(input())
# for i in range(1,n+1):
#     print("*"*i, end="")
#     if i % 2:
#         print("||", end="")
#     else:
#         print("--", end="")
# print()

# Zad 3

# n = int(input())
# for i in range(1,n+1):
#     print("*", end="")
#     if i % 2 == 1:
#         print("|"*i, end="")
#     else:
#         print("-"*i, end="")

# PRE 
# n = int(input())

# for i in range(n):
#     for j in range(n):
#         print("*", end="")
#     print()

# Zad 5


n = int(input())


for i in range(1, n+1):
    for j in range(1, n+1):
        if j == n//2 + 1:
            print("*", end="")
        elif i == n//2 + 1:
            print("-", end="")
        else:
            print(" ", end="")
    print()

# Zad 7

# n = int(input())

# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if i == 1 or j == 1 or i == n or j == n or (i == n//2 + 1 and j == n//2 + 1):
#             print("*", end="")
#         else: 
#             print(" ", end="")
#     print()
