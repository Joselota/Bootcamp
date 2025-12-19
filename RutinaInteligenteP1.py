# Mi primera rutina inteligente 🧠🏃‍♀️

# 1) Crear variables
nombre = "Ingrid"                 # str
edad = 30                         # int
altura_m = 1.62                   # float
rutina_completada = True          # bool
calorias_por_dia = [1800, 1950, 1720, 2100, 1850]  # lista de 5 valores

# (opcional) mirar tipos
print("Tipos:", type(nombre), type(edad), type(altura_m), type(rutina_completada), type(calorias_por_dia))

# 2) Calcular e imprimir

# promedio de calorías
promedio_calorias = sum(calorias_por_dia) / len(calorias_por_dia)

# diferencia entre el valor más alto y más bajo
diferencia_max_min = max(calorias_por_dia) - min(calorias_por_dia)

# multiplicar altura por edad (ejercicio simple de tipos)
altura_x_edad = altura_m * edad

# mensaje personalizado según si completó la rutina
if rutina_completada:
    mensaje = f"¡Bien, {nombre}! Rutina completada ✅"
else:
    mensaje = f"Ánimo, {nombre}. Mañana lo intentas de nuevo 💪"

# Mostrar resultados
print("\n--- Resultados ---")
print("Calorías por día:", calorias_por_dia)
print("Promedio calorías:", promedio_calorias)
print("Diferencia (máx - mín):", diferencia_max_min)
print("Altura x edad:", altura_x_edad)
print("Estado:", mensaje)
