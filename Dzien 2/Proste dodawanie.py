testy = int(input()) #* zmienna przechowująca ile testów program musi wykonać
koniec = [] #* tablica przechowująca wyniki
for i in range(testy): #* pętla wykonująca się n razy
    ile_liczb = int(input()) #* ile liczb program ma dodać
    ar = list(map(int, input().strip().split(' '))) #* stworzenie tablicy 
    #* przy pomocy mapy, która będzie przechowywała n liczb
    #* tablica przechowująca
    #* wczytane liczby
    suma = 0 #* suma liczb tablicy
    for x in range(len(ar)):
        suma += ar[x] #* program dodaje do sumy liczbę pod danym indexem
    if len(ar) != ile_liczb: #* test, jeżeli użytkownik podał więcej lub mniej liczb
        #* niż wcześniej zaznaczył to przerwij program
        break
    koniec.append(suma) #* na końcu pętli do tablicy przechowującej wyniki
    #* dodaj sumę liczb podanych wcześniej
for element in koniec: #* dla każdego wyniku w tabeli 
    print(element) #* wypisz wynik
