# napisy jako prawie listy

# s = input()
# print(s)

# for x in s:
#     print(x)
    
# for i in range(len(s)):
#     print(s[i])

# napis a lista

# L = [5,2,8,4]
# print(s, L)
# L.sort()
# print(s, L)
# s.sort() <- błąd, nie ma takiego czegoś
# print(s, L)

# konwersja napis <-> lista (list(), join())

# s = input()
# L = list(s)
# print(s, L)
# L.sort()
# print(s, L)
# s = "".join(L)
# print(s, L)

# sprawdz czy dane słowo jest palindromem

# s = input()
# L = list(s)
# R = list(s)  # R = L.copy()
# R.reverse()
# if L == R:
#     print("TAK")
# else:
#     print("NIE")
    
# palindrom za pomocą tablicy

s = input()

for i in range(len(s)//2):
    if s[i] != s[len(s)-1-i]:
        exit("NIE")
exit("TAK")
