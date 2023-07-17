#Crea un string que diga "Hola Mundo"
saludos: str = "Hola Mundo"
#Define una variable numerica n
n:int = 5
#Extrae en una variable los primeros n elementos
saludos_corta2 = saludos[:n]
#Convierte a mayusculas y minúsculas
print(saludos_corta2.upper())
print(saludos_corta2.lower())
# Divide la longitud entre 7
print(len(saludos_corta2)/7)