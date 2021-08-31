def palindrom(number):  # funkcja sprawdzająca czy liczba jest palindromem
    if str(number) == str(number)[::-1]:  # jezeli jest, zwroc true
        return True
    return False  # w przeciwnym wypadku zwroc false


def reverse(number):
    return int(str(number)[::-1])


testy = int(input())
for i in range(testy):
    licznik = 0
    n = int(input())
    while not palindrom(n):
        temp = reverse(n)
        n = n + temp
        licznik = licznik + 1
    print(n, licznik)
