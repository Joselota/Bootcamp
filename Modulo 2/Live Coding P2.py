# Live Coding 2: rutina interactiva (inputs + tipos + operadores)

EDAD_JUBILACION = 65
NOTA_MINIMA = 4.0

print("=== Rutina interactiva ===")

# 1) Solicitar nombre y edad (input)
nombre = input("Ingresa tu nombre: ")

edad_texto = input("Ingresa tu edad (en años): ")
edad = int(edad_texto)  # 6) conversión a int

# 8) Variable booleana: estado del usuario
respuesta = input("¿Eres estudiante? (s/n): ").strip().lower()
es_estudiante = (respuesta == "s")  # 7) comparación que produce True/False

# 2) Años faltantes para jubilarse
faltan = EDAD_JUBILACION - edad
ya_jubilado = (faltan <= 0)

# 3) Leer tres calificaciones numéricas
nota1 = float(input("Ingresa nota 1 (1.0 a 7.0): "))
nota2 = float(input("Ingresa nota 2 (1.0 a 7.0): "))
nota3 = float(input("Ingresa nota 3 (1.0 a 7.0): "))

# 4) Calcular promedio y determinar si aprueba
promedio = (nota1 + nota2 + nota3) / 3
aprueba = (promedio >= NOTA_MINIMA)

print("\n=== Resultados ===")

# 5) Mostrar resultados con print() y expresiones combinadas
print("Nombre:", nombre)
print("Edad:", edad, "| Estudiante:", es_estudiante)

# 7) Mensaje sobre jubilación (relacionales)
if ya_jubilado:
    print("Jubilación:", "Ya estás en edad de jubilación (o la superaste).")
else:
    print("Jubilación:", "Te faltan", faltan, "años para jubilarte.")

print("Notas:", nota1, nota2, nota3)
print("Promedio:", round(promedio, 2))

# 7) Mensaje condicional de aprobación
if aprueba:
    print("Estado:", "Aprueba ✅")
else:
    print("Estado:", "Reprueba ❌")

# Extra mini-demostración de str() (6)
mensaje_final = "Gracias, " + str(nombre) + ". Fin de la rutina."
print(mensaje_final)
