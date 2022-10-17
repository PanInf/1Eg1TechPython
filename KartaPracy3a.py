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

n = int(input())
for i in range(n):
    for j in range(i+1):
        print("*", end="")
    print()
    
print()
print()

for i in range(n):
    for j in range(n-i):
        print("*", end="")
    print()

print()
print()

for i in range(n):
    for j in range(n-i-1):
        print(" ", end="")
    for k in range(n-i-1, n):
        print("*", end="")
    print()


print()
print()

for i in range(n):
    for j in range(n-i-1):
        print("*", end="")
    for k in range(n-i-1, n):
        print("", end="")
    print()