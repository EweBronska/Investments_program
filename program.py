from przeliczaniePLN import przeliczWaluta
from zdolnosc import zdolnosc
from invest_in import podajInwestycje

x= int(input ("Podaj ile posiadacz pieniędzy w PLN: "))
y= 4.11

z = str(round(przeliczWaluta(x,y)))

print("Posiadasz " + z + " pieniędzy w USD")

wiek= int(input("Podaj wiek: "))
zdfinans = int(input("Podaj swoją zdolność finansową: "))

a= zdolnosc(wiek, zdfinans)

if a == True:
    podajInwestycje()
else:
    print("Nie inwestuj")
