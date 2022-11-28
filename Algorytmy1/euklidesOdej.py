a, b = int(input()), int(input())
while a != b:
    if a > b : a = a - b
    if b > a : b = b - a
print(a)