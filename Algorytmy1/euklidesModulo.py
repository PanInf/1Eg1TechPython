a, b = int(input()), int(input())
while b > 0:
    a, b = b, a % b
print(a)
