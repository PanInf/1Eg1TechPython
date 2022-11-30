a, b = int(input()), int(input())
iloczyn = a * b
while a != b :
    if a > b : a = a - b
    if b > a : b = b - a
nwd = a
print(iloczyn // nwd)
