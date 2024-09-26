klass = {
    "Elev1": {"namn": "Anna", "ålder": 15, "betyg": [10, 8, 9]},
    "Elev2": {"namn": "Erik", "ålder": 16, "betyg": [7, 6, 8]},
    "Elev3": {"namn": "Maria", "ålder": 15, "betyg": [9, 10, 9]}
}
klass["Elev4"] = {"namn": "Einar", "ålder": 26, "betyg": [4, 5, 6]}
klass["Elev4"]['betyg'] = [7,8,2]
for elev in klass:
    avg_betyg = sum(klass[elev]["betyg"]) / len(klass[elev]["betyg"])
    print(f"{klass[elev]['namn']} har medelbetyg {avg_betyg:.1f}")

klass["Elev4"]['ålder'] = 83



print(klass["Elev4"])

print(klass.get('Elev4', 'eleven finns inte'))