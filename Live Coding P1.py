# Demo Bootcamp: Mini rutina interactiva en Python

print("=== Demo: Datos + Operaciones + Estructuras en Python 🐍 ===\n")

# 1) Crear variables: nombre, edad, altura, es_estudiante
nombre = input("¿Cómo te llamas? ")
edad = int(input("¿Cuántos años tienes? "))
altura = float(input("¿Cuánto mides en metros? (ej: 1.65) "))
es_estudiante_txt = input("¿Eres estudiante? (s/n): ").strip().lower()
es_estudiante = (es_estudiante_txt == "s")

print("\n✅ Variables creadas.\n")

# 2) Imprimir valores y tipos con print() y type()
print("---- 2) Valores y tipos ----")
print("nombre:", nombre, "| tipo:", type(nombre))
print("edad:", edad, "| tipo:", type(edad))
print("altura:", altura, "| tipo:", type(altura))
print("es_estudiante:", es_estudiante, "| tipo:", type(es_estudiante))
print()

# 3) Calcular promedio de edad entre tres personas
print("---- 3) Promedio de edad (3 personas) ----")
edad1 = int(input("Edad persona 1: "))
edad2 = int(input("Edad persona 2: "))
edad3 = int(input("Edad persona 3: "))

promedio = (edad1 + edad2 + edad3) / 3
print("Promedio de edad:", promedio, "| tipo:", type(promedio))
print()

# 4) Mostrar diferencia entre int y float al dividir
print("---- 4) División float vs división entera ----")
a = 10
b = 3
division_decimal = a / b      # devuelve float
division_entera = a // b      # devuelve int (parte entera)
residuo = a % b               # resto

print("a =", a, "b =", b)
print("a / b  =", division_decimal, "| tipo:", type(division_decimal))
print("a // b =", division_entera, "| tipo:", type(division_entera))
print("a % b  =", residuo, "(residuo)")
print()

# 5) Construir lista de productos y diccionario de precios
print("---- 5) Lista + Diccionario ----")
productos = ["pan", "leche", "cafe", "arroz"]
precios = {
    "pan": 1200,
    "leche": 1100,
    "cafe": 3500,
    "arroz": 1400
}

print("Productos:", productos)
print("Precios:", precios)
print()

# 6) Calcular precio total de un “carrito”
print("---- 6) Total carrito ----")
carrito = ["pan", "cafe", "pan"]  # repetido a propósito
total = 0

for item in carrito:
    total += precios[item]

print("Carrito:", carrito)
print("Total:", total)
print()

# 7) Usar set() para obtener elementos únicos
print("---- 7) Elementos únicos con set ----")
unicos = set(carrito)
print("Únicos:", unicos)
print()

# 8) Evaluar una condición booleana con == o !=
print("---- 8) Condición booleana (== / !=) ----")
usuario = input("Usuario: ").strip().lower()
activo_txt = input("¿Cuenta activa? (s/n): ").strip().lower()
activo = (activo_txt == "s")

if usuario == "admin" and activo:
    print("Acceso concedido ✅")
elif usuario != "admin":
    print("Acceso denegado ❌ (usuario no es admin)")
else:
    print("Acceso denegado ❌ (cuenta inactiva)")

print("\n=== Fin demo ===")
