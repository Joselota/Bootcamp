# Calculadora exprés: rutina inteligente con variables

print("=== Calculadora exprés (rendimiento académico) ===")

# 1) Pedir datos (input SIEMPRE devuelve texto / str)
nombre = input("Nombre: ")

edad_str = input("Edad (en años): ")
edad = int(edad_str)  # Conversión 1: str -> int

nota1_str = input("Nota 1 (0 a 10): ")
nota2_str = input("Nota 2 (0 a 10): ")
nota3_str = input("Nota 3 (0 a 10): ")

nota1 = float(nota1_str)  # Conversión 2: str -> float
nota2 = float(nota2_str)
nota3 = float(nota3_str)

# 2) Calcular
promedio = (nota1 + nota2 + nota3) / 3
edad_meses = edad * 12

# 3) Comparación lógica (condición)
aprueba = promedio >= 6

# 4) Mensaje personalizado (incluye conversión extra con str() si quieres)
estado = "APROBADO ✅" if aprueba else "REPROBADO ❌"

print("\n--- Resultados ---")
print("Estudiante:", nombre)
print("Edad:", edad, "años (", edad_meses, "meses )")
print("Notas:", nota1, nota2, nota3)
print("Promedio:", round(promedio, 2))
print("Estado:", estado)
