voltage = float(input("Battery voltage (V): "))
temperature = float(input("Battery temperature (C): "))
charge = float(input("Battery charge (%): "))

if voltage <= 0 or not 0 <= charge <= 100:
    print("Invalid readings")
elif temperature >= 60 or temperature < 0:
    print("Temperature warning!")
elif charge < 20:
    print("Low battery!")
else:
    print("Battery readings within configured limits")

print("Voltage:", voltage, "V")
print("Charge:", charge, "%")
