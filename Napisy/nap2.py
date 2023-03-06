# anagramy np adam dama
# burza arbuz

# a, b = input(), input()
# X, Y = list(a), list(b)
# X.sort()
# Y.sort()
# a = "".join(X)
# b = "".join(Y)
# if a == b:
#     print("TAK")
# else: print("NIE")

# anagram przez tablice

a, b = input(), input()
X, Y = [0] * 150, [0] * 150
for i in range(len(a)):
    X[ord(a[i])] += 1
for i in range(len(b)):
    Y[ord(b[i])] += 1
if X == Y:        print("TAK")
else:             print("NIE")