def nww(x, y):  # * definiowanie algorytmu nww
    if x == y:  # jezeli x jest rowny y
        return y  # to zwroc y
    if x < y:  # jezeli x jest mniejszy niz y
        (x, y) = (y, x)  # to następuje zamiana miejsacami
    c = y  # * tworzymy nową zmienną, przypisujemy do niej y
    while True:
        y = y + c  # ! dodajemy do y drugą taką samą liczbę
        if y % x == 0:  # * jezeli reszta z dzielenia y i x to zero
            return y  # zwroc y


N = int(input(''))
for i in range(N):  # * ile razy program ma się wykonać
    data = (input('')).split(' ')  # kilka liczb w jednej linijce
    a = int(data[0])
    b = int(data[1])
    output = nww(a, b)
    print(output)
