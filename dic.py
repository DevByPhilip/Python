projektdata = {
    "Projekt A": {"Erik": 25, "Lina": 30, "Tomas": 20},
    "Projekt B": {"Lina": 35, "Erik": 40},
    "Projekt C": {"Tomas": 45, "Erik": 50}
}

max_tid = 0
projekt_erik = ""

for projekt, timmar in projektdata.items():
    if "Erik" in timmar and timmar["Erik"] > max_tid:
        max_tid = timmar["Erik"]
        projekt_erik = projekt

print(f"Erik har arbetat mest på {projekt_erik} med {max_tid} timmar.")