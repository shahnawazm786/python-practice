temps = [23, 25, 22, 26, 24]

temps_copy=temps
print(temps)
print(temps_copy)
temps[-2]=30
print(temps)
print(temps_copy)
temps_copy.append(28)
print(temps)
print(temps_copy)
if 26 in temps:
    temps_copy.remove(26)
print(temps[temps.index(25)-2])