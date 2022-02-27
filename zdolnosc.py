def zdolnosc(wiek, zdfinans):
    punkty = 0

    if wiek < 18:
        punkty += 0
    elif wiek >= 18:
        punkty += 1
    elif wiek > 80:
        punkty += 0
    if zdfinans == 0:
        punkty = 0
    elif zdfinans >= 1:
        punkty += 1
    if punkty >= 2:
        return True



