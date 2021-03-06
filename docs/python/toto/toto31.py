#! /usr/bin/env python
# -*- coding: utf-8 -*-

from totomodul import ustawienia, losujliczby, pobierztypy, czytaj, zapisz

# program główny

# ustalamy trudność gry
ileliczb, maksliczba, ilerazy = ustawienia()

# losujemy liczby
liczby = losujliczby(ileliczb, maksliczba)

# pobieramy typy użytkownika i sprawdzamy, ile liczb trafił
for i in range(ilerazy):
    typy = pobierztypy(ileliczb, maksliczba)
    trafione = set(liczby) & typy
    if trafione:
        print "\nIlość trafień: ",len(trafione)
        print "Trafione liczby: ",trafione
    else:
        print "Brak trafień. Spróbuj jeszcze raz!"

    print "\n"+"x"*40+"\n" # wydrukuj 40 znaków x

print "Wylosowane liczby:",liczby

import time

nick = raw_input("\nPodaj swój nick: ")
nazwapliku = nick + ".json"

losowania = czytaj(nazwapliku)

losowania.append({
    "czas": time.time(),
    "dane": (ileliczb, maksliczba),
    "wylosowane": liczby,
    "ile": len(trafione)
})

zapisz(nazwapliku, losowania)

print "\n",losowania
