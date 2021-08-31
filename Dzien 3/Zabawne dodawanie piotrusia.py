def palindrom(number):  # funkcja sprawdzająca czy liczba jest palindromem
    if str(number) == str(number)[::-1]:  # jezeli jest, zwroc true
        return True
    return False  # w przeciwnym wypadku zwroc false


def reverse(number):  # odwroc liczbe
    return int(str(number)[::-1])  # zwraca odwróconą liczbę (int)


testy = int(input())  # ile liczb
for i in range(testy):
    licznik = 0  # licznik ile dodawań zostało dokonanych
    n = int(input())  # liczba
    while not palindrom(n):  # * dopuki liczba nie jest palindromem
        temp = reverse(n)  # pomocnicza zmienna przechowująca odwroconą liczbę
        n = n + temp  # do n przypisujemy jej wartość plus wartość odwróconą
        licznik = licznik + 1  # zwiekszamy licznik o jeden
    print(n, licznik)  # wypisujemy liczbę jako palindrom oraz ilosc dodawań
