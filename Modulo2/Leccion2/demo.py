EDAD_JUBILACION = 60
NOTA_MINIMA = 4.0

# 1) Solicitar nombre y edad (input)
nombre = "Ingrid" #input("Ingresa tu nombre: ")
edad_texto = "30" #input("Ingresa tu edad (en años): ")
edad = int(edad_texto)  # 6) conversión a int

#print(f"Hola, {nombre}. Tienes {edad} años.")

# 2) Años faltantes para jubilarse
faltan = EDAD_JUBILACION - edad
ya_jubilado = (faltan <= 0)
#print("Años faltantes para jubilarse:", faltan, "| Ya jubilado:", ya_jubilado)
"""
# 3) Leer tres calificaciones numéricas
nota1 = float(input("Ingresa nota 1 (1.0 a 7.0): "))
nota2 = float(input("Ingresa nota 2 (1.0 a 7.0): "))
nota3 = float(input("Ingresa nota 3 (1.0 a 7.0): "))

# 4) Calcular promedio y determinar si aprueba
promedio = (nota1 + nota2 + nota3) / 3
aprueba = (promedio >= NOTA_MINIMA)
#print("\n=== Resultados ===")
#print("promedio:", round(promedio, 2))
#print("aprueba:", aprueba)

# 7) Mensaje condicional de aprobación
if aprueba:
    print("Estado:", "Aprueba ✅")
else:
    print("Estado:", "Reprueba ❌")
"""
# 8) Variable booleana: estado del usuario
respuesta = input("¿Eres estudiante? (s/n): ").strip().lower()
es_estudiante = (respuesta == "s")  # 7) comparación que produce True/False
print("Estudiante:", es_estudiante)