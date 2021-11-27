import random


zahl = 100
randomnumberlist = random.sample(range(1, 1000000000), 1000)
print(randomnumberlist)

result = "randomnumberlist" < "zahl"

if result:
    #undo = del print(
    #del (
    print("Es wurden zu viele Zufallszahlen erstellt")
else:
    print("Die Zufallszahlenliste ist erfolgreich erstellt worden!")
