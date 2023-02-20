# w przedzialne <2;200> wypisz te liczby, w których suma dzielników właściwych liczby n jest większa od liczby n

for i in range(2,201):
    suma = 0
    for j in range(1,i):
        if i % j == 0:
            suma += j
    if suma > i:
        print(i, end=" ")
    # x = i - suma
    # licznik = 0
    # for k in range(1,x):
    #     if x % k == 0:
    #         licznik += 1
    # if licznik > 1:
    #     print(x, end=" ")