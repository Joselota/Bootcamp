# Calculadora exprés: rutina inteligente con variables
print("=== Calculadora express (rendimiento académico) ===")

# 1) Pedir datos (input SIEMPRE devuelve texto / str)
nombre = input("Nombre: ")
edad = int(input("Edad (en años): "))
nota1 = float(input("Nota 1 (0 a 10): "))
nota2 = float(input("Nota 2 (0 a 10): "))
nota3 = float(input("Nota 3 (0 a 10): "))

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
