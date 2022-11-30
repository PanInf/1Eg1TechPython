a, b = map(int, input().split())
iloczyn = a * b
while b > 0:
    a, b = b, a%b    
nwd = a
print(iloczyn // nwd)
