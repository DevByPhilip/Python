projects = {
    "Projekt A": {"Erik": 25, "Lina": 30, "Tomas": 20},
    "Projekt B": {"Lina": 35, "Erik": 40},
    "Projekt C": {"Tomas": 45, "Erik": 50}}

# Sortera efter summan av projektpunkter

sorted_projects = dict(sorted(projects.items(), key=lambda item: sum(item[1].values()), reverse=True))

print(sorted_projects)  # Skriv ut sorterade projekter med summan av projektpunkter

