def przeliczWaluta():
    podajWaluta = input("Podaj waluta do przeliczenia:\n")
    ilosc = input("Podaj ilość " + podajWaluta + "do przeliczenia na PLN \n")


    waluta1 = "usd"


    if podajWaluta() == waluta1:
        wynik = int(ilosc) * 4.11
        print(wynik)
    else:
        print("Error: Wybrano zla walute. Sproboj jeszcze raz.")
        przeliczWaluta()


przeliczWaluta()