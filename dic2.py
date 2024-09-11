# Dictionary med projekt och arbetade timmar
projektdata = {
    "Projekt A": {"Erik": 25, "Lina": 30, "Tomas": 20},
    "Projekt B": {"Lina": 35, "Erik": 40},
    "Projekt C": {"Tomas": 45, "Erik": 50}
}

lina_projekt = {}

for projekt, timmar in projektdata.items():
    if "Lina" in timmar and timmar["Lina"] > 30:
        lina_projekt[projekt] = timmar

print("Projekt där Lina har arbetat mer än 30 timmar:", lina_projekt)