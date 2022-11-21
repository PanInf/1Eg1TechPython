# 1. Algorytm sprawdzający czy liczba jest pierwsza
# liczba pierwsza dzieli sie tylko przez 1 i samą siebie
# 2, 3, 5, 7, 11, 13, 17, 19 itd...
# liczba x ma swój dzielnik (o ile go ma) w przedziale [2, sqrt(x)]
# dzielnik właściwy - dzielnik liczby oprócz 1 i niej samej

# n = int(input())
# for i in range(2,int(n**0.5)+1):
#     if n % i == 0:
#         print("Liczba nie jest pierwsza")
#         exit()
# print("Liczba jest pierwsza")

# 2. Generator liczb pierwszych - liczby pierwsze w przedziale [p, q]

# p, q = map(int, input().split())
# for i in range(p, q+1):
#     flaga = True
#     for j in range(2, int(i**0.5)+1):
#         if i % j == 0:
#             flaga = False
#             break
#     if flaga:
#         print(i, end=" ")



# 3. Generator liczb pierwszych - początkowe k liczb pierwszych

# n = int(input("Podaj ile chcesz liczb pierwszych: "))

# x = 2
# while n > 0:
#     flaga = True
#     for i in range(2, x):
#         if x % i == 0:
#             flaga = False
#             break
#     if flaga:
#         print(x, end=" ")
#         n = n - 1
#     x = x + 1
