import sys

try: 
    n = '' #koncowy wyraz
    toUp = False # czy trzeba podwyzszczyc, na starcie programu false
    for line in sys.stdin: # dla każdej lini w tym co wpisze użytkownik
        for w in line: # dla każdego znaku w wyrazie 
            if w != ' ': # jezeli znak jest równy spacji
                if(toUp): # jezeli toUp jest true:
                    n += w.upper() # do wyrazuje dodajemy wielki znak 
                    toUp = False # zwracamy toUp na false
                else: # wprzeciwnym wypadku jezeli toUp jest false
                    n += w # wyraz dodaje zwykly znak
            elif w == ' ': # jezeli znak jest rowny spacji
                toUp = True # to toUp ustawia na True

    print(n)
except:
    sys.exit(0)
