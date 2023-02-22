N = [100,50,20,10,5,2,1]
# N.sort(reverse=True)
x = int(input("Podaj kwotę: "))
for i in N:
    ilosc = x // i
    if ilosc > 0:
        x = x - ilosc * i
        print(f"{i}zł razy {ilosc}")