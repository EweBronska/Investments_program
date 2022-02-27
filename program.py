import przeliczaniePLN
import zdolnosc
import invest_in

przeliczWaluta()

wiek= int(input("Podaj wiek: "))
zdfinans = int(input("Podaj swoją zdolność finansową: "))

zdolnosc()

if zdolność()== True:
    invest_in()
elif zdolnosc == False:
    print("Nie inwestuj")
