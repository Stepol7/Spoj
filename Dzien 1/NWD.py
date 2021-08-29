# zdefiniowanie funkcji obliczającej nwd
def nwd(a, b):
    if b > 0:  # jezeli b jest wieksze niz 0
        return nwd(b, a % b)  # zwroc funkcję nwd z
        # parametrami b oraz wynikiem reszty z dzielenia a i b
    else:  # w przeciwnym wypadku
        return a  # wzroc a


wykonane = []  # pusta lista, która będzie przechowywała wyniki
testy = int(input())  # ilosc testow

for i in range(testy):
    # wczytanie więcej niż jednego argumentu
    x = list(map(int, input().split()))
    # x jes traktowany jako lista, dwuelementowa
    # poniewaz ogranicza nas program
    wykonane.append(nwd(x[0], x[1]))  # wykonanie funkcji z użyciem pierwszego
    # oraz drugiego elementu tablicy x,
    # wpisanie wyniku tej funkcji do listy wykonanych

for i in wykonane:  # wypisanie zawartosci funkcji wykonane
    print(i)
