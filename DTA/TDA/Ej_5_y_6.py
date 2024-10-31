set_a_2024 = {"Lolo", "Daniela", "Miguel", "Pablo", "Juana", "Rakela" }
set_b_2023 = {"Uriel", "Hernan", "Daniela", "Rakela", "Pablo", "Pipi"}
set_c_2022 = {"Rakela", "Daniela", "Ismael", "Fermin", "Xavier", "Pipi"}

#print(set_a)

set_unido = set_a_2024.union(set_b_2023 and set_c_2022)

print("Los preceptores que estuvieron durante los años 2022, 2023 y 2024, son:")
print(set_unido)

print(f"Los preceptores que se encuentran en el Año 2024 y no estuvieron en el anterior: {set_a_2024 - set_b_2023}")
print(f"Los preceptores que se encuentran en el Año 2023 y no estuvieron en el anterior: {set_b_2023 - set_c_2022}")
print(f"Los preceptores que estuvieron durante los años de cursada 2022 y 2023: {set_c_2022 & set_b_2023}")
print(f"Los preceptores que estuvieron durante los 3 años de cursada (2022, 2023 y 2024): {set_a_2024 & set_b_2023 & set_c_2022}")