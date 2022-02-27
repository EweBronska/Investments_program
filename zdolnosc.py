def zdolnosc(wiek: int, zdfinans: int):
    punkty = 0

    if wiek < 18:
        punkty += 0
    if wiek > 70:
        punkty += 1
    else:
        punkty += 2
    if zdfinans == 0:
        punkty = 0
    if zdfins > 1:
        punkty += 1
    if punkty >= 2:
        return True
