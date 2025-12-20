edad = 25
#print("La edad es:", edad)

nombre_completo = "Juan Solís"
telefono = "123-456-7890"
mail_personal = "juan@example.com"
#direccion = "Calle Uno 123"

"""print("Nombre:", nombre_completo)
print("Teléfono:", telefono)
print("Correo electrónico:", mail_personal)
print("Dirección:", direccion)
print("Hola, Python funciona correctamente 🐍")"""

edad = " - 30"
#print("La nueva edad es:", edad)


""" Variable Global y Variable Local"""

mensaje = "Hola, soy GLOBAL"  

def saludar():
    nombre = "Ingrid"        
    print(mensaje)             
    print("Hola", nombre)      

#saludar()

#print(mensaje)                 
# print(nombre)                

""" Declarqacion de multiples variables"""
x, y, z = 1, 2, 3

#print(x)
#print(y)
#print(z)

""" Tipos de datos en Python"""

entero = 10
flotante = 10.5
cadena = "Hola Mundo"
booleano = True
complejo = 2 + 3j
lista = [1, 2, 3, 4, 5]
tupla = (1, 2, 3, 4, 5)
conjunto = {1, 2, 3, 4, 5}
diccionario = {"clave1": "valor1", "clave2": "valor2"}
rango = range(5)
#print(type(entero))
#print(type(flotante))
#print(type(cadena))        
#print(type(booleano))
#print(type(complejo))
#print(type(lista))
#print(type(tupla))
#print(type(conjunto))
#print(type(diccionario))
#print(type(rango))

### Operaciones con diferentes tipos de datos
# Cadena original
texto = "  Hola, mundo de Python!  "

# 1. Eliminar espacios al inicio y final
limpio = texto.strip()

# 2. Convertir a minúsculas y mayúsculas
minusculas = limpio.lower()
mayusculas = limpio.upper()

# 3. Reemplazar palabras
reemplazo = limpio.replace("Python", "la programación")

# 4. Verificar si contiene una palabra
contiene = "Python" in limpio

# 5. División de la cadena en palabras
palabras = limpio.split()

# Resultados
"""print("Original:", texto)
print("Limpio:", limpio)
print("Minúsculas:", minusculas)
print("Mayúsculas:", mayusculas)
print("Reemplazo:", reemplazo)
print("¿Contiene 'Python'?", contiene)
print("Palabras:", palabras)"""

### Ejemplos de operaciones con booleanos

# Comparaciones simples
edad = 18

es_mayor = edad >= 18

#print("¿Es mayor de edad?", es_mayor)  # True


# Comparaciones combinadas
nota = 7

aprobado = nota >= 6 and nota <= 10

#print("¿La nota es aprobatoria?", aprobado)  # True


# Uso de booleanos en condicionales
usuario = "admin"
activo = True

"""if usuario == "admin" and activo:
    print("Acceso concedido")
else:
    print("Acceso denegado")"""

""" Expresiones aritméticas"""
# Operaciones básicas
a = 10
b = 3

suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b          # División con decimales
division_entera = a // b  # División entera
modulo = a % b            # Resto
potencia = a ** b         # Exponente

# Mostrar resultados
"""print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)
print("División entera:", division_entera)
print("Módulo:", modulo)
print("Potencia:", potencia)"""


""" Ejemplos de operaciones aritméticas"""

a = 10
b = 3

suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b

print("Suma:", suma, "Resta:", resta, "Multiplicación:", multiplicacion)

"""Uso de Módulo y División Entera"""
dividendo = 10
divisor = 3

residuo = dividendo % divisor
division_entera = dividendo // divisor

print("Residuo:", residuo)  # Salida: Residuo: 1
print("División entera:", division_entera)  # Salida: División entera: 3


"""Operador de Exponenciación"""
base = 2
exponente = 3

potencia = base ** exponente

print("Potencia:", potencia)  # Salida: Potencia: 8


#
#  Parte 2: 
#

"""Uso de Paréntesis para Prioridad"""

resultado = 2 + 3 * 4  # Sin paréntesis, multiplica primero
print("Resultado sin paréntesis:", resultado)  # Salida: 14

resultado = (2 + 3) * 4  # Con paréntesis, suma primero
print("Resultado con paréntesis:", resultado)  # Salida: 20


"""Conversión de Entero a Flotante"""

entero = 10
decimal = float(entero)
print("Convertido a decimal:", decimal)  # Salida: 10.0

"""Flotantes a Enteros"""
flotante = 10.7
entero = int(flotante)
print("Convertido a entero:", entero)  # Salida: 10


"""Conversión de Números a Cadenas y Viceversa"""
numero = 123
cadena = str(numero)
print("Convertido a cadena:", cadena)  # Salida: "123"

cadena = "456"
numero = int(cadena)
print("Convertido a número:", numero)  # Salida: 456

"""Conversión de Cadenas a Booleanos"""
cadena = "True"
booleano = bool(cadena)
print("Convertido a booleano:", booleano)  # Salida: True

"""Conversión Implícita en Operaciones"""
entero = 5
decimal = 2.5
resultado = entero + decimal  # entero se convierte a float
print("Resultado de la suma:", resultado)  # Salida: 7.5

"""Impresión de Variables y Textos Combinados"""
nombre = "Ana"
edad = 28
print(f"Nombre: {nombre}, Edad: {edad}")  # Usando f-strings
print("Nombre:", nombre, "| Edad:", edad)  # Usando comas   
print("Nombre: " + nombre + ", Edad: " + str(edad))  # Usando concatenación


"""Control de la Separación y el Final de la Impresión"""
#1️⃣ Separador (sep)
print("Hola", "Mundo")
print("Hola", "Mundo", sep="-")
print(1, 2, 3, sep=", ")
# 1, 2, 3

print("2025", "12", "18", sep="/")
# 2025/12/18

#2️⃣ Carácter final (end)
print("Hola")
print("Mundo")
print("Hola", end="!")
print(" Mundo")

print("Cargando", end="...")
print(" listo")

#3️⃣ sep y end juntos
print("Python", "es", "genial", sep=" 💙 ", end="!!!")

"""Impresión de Formato Avanzado"""
precio = 49.99
print(f"El precio es: ${precio:.2f}")  # Dos decimales


"""Usos Prácticos de print() en Depuración"""
contador = 0
for i in range(5):
    contador += i
    print(f"Iteración {i}: contador = {contador}")  # Depuración paso a paso


"""Entrada de Datos en Consola"""
nombre = input("¿Cómo te llamas? ")
edad = input("¿Cuántos años tienes? ")
print(f"Hola, {nombre}. Tienes {edad} años.")

"""Conversión de Entradas de Texto a Otros Tipos de Datos"""
edad = int(input("¿Cuántos años tienes? "))
altura = float(input("¿Cuánto mides en metros? (ej: 1.75) "))
print(f"Tienes {edad} años y mides {altura} metros.")

"""Manejo de Errores en Entradas de Datos"""
try:
    edad = int(input("¿Cuántos años tienes? "))
    print(f"Tienes {edad} años.")
except ValueError:
    print("Por favor, ingresa un número válido para la edad.")
    


    