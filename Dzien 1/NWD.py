# zdefiniowanie funkcji obliczającej nwd
def nwd(a, b): return nwd(b, a % b) if b else a


wykonane = []
testy = int(input())

for i in range(testy):
    # wczytanie więcej niż jednego argumentu
    x = list(map(int, input().split()))
    # dodanie do listy 'wykonane' wyniku funkcji
    wykonane.append(nwd(x[0], x[1]))

for i in wykonane:  # wypisanie zawartosci funkcji wykonane
    print(i)
