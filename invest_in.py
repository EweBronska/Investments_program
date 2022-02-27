from przeliczaniePLN import przeliczWaluta

def podajInwestycje():
    if przeliczWaluta() < 200:
        print("Inwestuj w akcje")
    elif przeliczWaluta() < 1000:
        print ("Inwestuj w nieruchomości")
    elif przeliczWaluta() <5000:
        print ("Inwestuj w surowce")
