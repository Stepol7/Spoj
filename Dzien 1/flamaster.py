n = int(input())
for x in range(n):  # * pętla wykonuje się x razy
    word = input()  # * wprowadzamy słowo
    # * ustalamy zmienną równą długości słowa wprowadzonego
    word_len = len(word)
    # * tworzymy listę, która będzie służyła do późniejszego wyświetlenia wyniku
    short_version = []
    counter = 0  # * tworzymy licznik występowania słów, na początku ustalamy jego wartość na 0
    # * dla i oraz _ w enumarate - umożliwia iterację po obiektach
    for i, x in enumerate(word):
        # * przy jednoczesnej informacji, którą iterację wykonujemy
        # ? https://analityk.edu.pl/python-enumerate/
        counter += 1  # * na samym starcie licznik zwiększamy o 1
        # * jezeli i jest równe dlugosci słowa - 1
        if i == word_len-1 or word[i] != word[i+1]:
            # * lub iterator słowa ( na samym początku będzie to 0), jest różne od iteratora o 1 większego to
            if counter <= 2:  # * jezeli licznik jest mniejszy bądź równy 2 to
                # * do listy dodajemy literę oraz mnożymy ją przez ilość wystąpień
                short_version += [word[i] * counter]
            else:  # ! w przeciwnym wypadku jezeli licznik jest większy niż 2
                # * do listy dodajemy literę oraz liczbę jej wystapień
                short_version += [word[i], str(counter)]
            counter = 0  # * na samym końcu pętli zerujemy licznik
    print(''.join(short_version))  # * wypisujemy końcową wersję napisu
