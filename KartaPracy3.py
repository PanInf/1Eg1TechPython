# Zad 1
# n = int(input("Podaj ile chcesz liczb: "))
# for i in range(n):
#     print(i**3 + 3, end=" ")

# Zad 2
# for i in range(105,1000,15):
#     print(i, end=" ")

# Zad 3 
n = int(input("Podaj liczbę n:\n"))
for i in range(1, n+1):
    if n%i == 0:
        print(i, end=" ")
