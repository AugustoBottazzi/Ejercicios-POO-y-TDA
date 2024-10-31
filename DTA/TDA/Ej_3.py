set_a_2024 = {"Lolo", "Daniela", "Miguel", "Pablo", "Juana", "Rakela" }
set_b_2023 = {"Uriel", "Hernan", "Daniela", "Rakela", "Pablo"}

#print(set_a)

set_unido = set_a_2024.union(set_b_2023)

print(set_unido)
print(f"Los preceptores que se encuentran en el Año 2024 y no estuvieron en el anterior: {set_a_2024 - set_b_2023}")
print(f"Los preceptores que estuvieron durante los 2 años de cursada (2023 y 2024): {set_a_2024 & set_b_2023}")