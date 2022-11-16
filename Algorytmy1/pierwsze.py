# 1. Algorytm sprawdzający czy liczba jest pierwsza
# liczba pierwsza dzieli sie tylko przez 1 i samą siebie
# 2, 3, 5, 7, 11, 13, 17, 19 itd...
# liczba x ma swój dzielnik (o ile go ma) w przedziale [2, sqrt(x)]
# dzielnik właściwy - dzielnik liczby oprócz 1 i niej samej

n = int(input())
for i in range(2,int(n**0.5)+1):
    if n % i == 0:
        print("Liczba nie jest pierwsza")
        exit()
print("Liczba jest pierwsza")

# 2. Generator liczb pierwszych - liczby pierwsze w przedziale [p, q]

# [10;15] -> 11 i 13
# [20;22] -> brak liczb pierwszych

# 3. Generator liczb pierwszych - początkowe k liczb pierwszych