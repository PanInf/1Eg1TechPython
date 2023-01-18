L = [4, 7, 7, 3, 2, 4, 1, 4, 6, 8]

print(L)
print(len(L))
print(L[1])
print(L[8])

print(L[1:6:2])
print(L[:3])
print(L[::3])
print(L[::-4])
print(L[2:7:-2])
print(L[3::3])

for elem in L:
    print(elem, end=" ")
print("\n")

for i in range(len(L)):
    print(L[i], end=" ")
print("\n")