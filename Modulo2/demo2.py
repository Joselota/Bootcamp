EDAD_JUBILACION = 60
NOTA_MINIMA = 4.0
# 1) Solicitar nombre y edad (input)In
nombre = input("Ingresa tu nombre: ")
edad_texto = input("Ingresa tu edad (en años): ")
edad = int(edad_texto)  
respuesta = input("¿Eres estudiante? (s/n): ").strip().lower()
es_estudiante = (respuesta == "s")  # 7) comparación que produce True/False

#print(f"Hola, {nombre}. Tienes {edad} años.")
# 2) Años faltantes para jubilarse
año_faltantes = EDAD_JUBILACION - edad
ya_jubilado = (año_faltantes <= 0)
#print("Te faltan", año_faltantes, "años para jubilarte.")

# 3) Leer tres calificaciones numéricas
"""nota1 = float(input("Ingresa nota 1 (1.0 a 7.0): "))
nota2 = float(input("Ingresa nota 2 (1.0 a 7.0): "))
nota3 = float(input("Ingresa nota 3 (1.0 a 7.0): "))

# 4) Calcular promedio y determinar si aprueba
promedio = (nota1 + nota2 + nota3) / 3
aprueba = (promedio >= NOTA_MINIMA)
print("Promedio:", round(promedio, 2))
print("Aprueba:", aprueba)"""

# 7) Mensaje sobre jubilación (relacionales)
if ya_jubilado:
    print("Jubilación:", "Ya estás en edad de jubilación (o la superaste).")
else:
    print("Jubilación:", "Te faltan", año_faltantes, "años para jubilarte.")