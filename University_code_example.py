temperature = [85, 95, 78, 110, 102, 120]
rpm = [2000, 2200, 1700, 3000, 4500, 3100]
fuel = [8, 9.5, 7.2, 11, 16, 12]
countefficient = 0
countoverload = 0
countnormal = 0
for i in range(0, 5):
    if temperature[i] > 80 and temperature[i] < 110:
        if rpm[i] > 1500 and rpm[i] < 3000:
            if fuel[i] < 10:
                print("Efficient")
                countefficient = countefficient + 1
    elif temperature[i] > 110 or temperature[i] < 80 or rpm[i] > 4000 or fuel[i] > 15:
        print("Overloaded")
        countoverload = countoverload + 1
    else:
        print("Normal")
        countnormal = countnormal + 1

tempaverage = int(85 + 95 + 78 + 110 + 102 + 120)/6
print("Average temperature is", int(tempaverage))
rpmaverage = int(2000 + 2200 + 1700 + 3000 + 4500 + 3100)/6
print("Average rpm is", int(rpmaverage))
fuelaverage = float(8 + 9.5 + 7.2 + 11 + 16 + 12)/6
print("Average fuel is", int(fuelaverage))

print("Count of efficient", countefficient)
print("Count of Overload", countoverload)
print("Count of Normal", countnormal)
