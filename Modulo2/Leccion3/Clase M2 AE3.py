# Ejemplo básico de condicional
edad = 18
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

# Ejemplo de uso de AND
edad = 20
tiene_identificacion = True

if edad >= 18 and tiene_identificacion:
    print("Puedes entrar al club.")
else:
    print("No puedes entrar al club.")

# Ejemplo de uso de OR
es_estudiante = True
es_docente = False

if es_estudiante or es_docente:
    print("Tienes acceso al descuento.")
else:
    print("No tienes acceso al descuento.")

# Ejemplo de uso de NOT
es_mayor = False
if not es_mayor:
    print("Eres menor de edad.")
else:
    print("Eres mayor de edad.")

# Operador Mayor Que y Mayor o Igual Que
edad = 21
if edad > 18:
    print("Puedes votar.")
if edad >= 21:
    print("Puedes beber alcohol legalmente en EE.UU.")  

# Operador Menor Que y Menor o Igual Que
nota = 7   
if nota < 5:
    print("Reprobaste el examen.")
elif nota <= 7:
    print("Aprobaste el examen con una nota regular.")
else:
    print("Aprobaste el examen con una buena nota.")

# Operador Igual Que
respuesta = "sí"

if respuesta == "sí":
    print("Has respondido afirmativamente.")
else:
    print("Has respondido negativamente.")

# Operador Distinto Que
usuario = "admin"

if usuario != "invitado":
    print("Acceso concedido.")
else:
    print("Acceso denegado.")

# Ejemplo de uso de paréntesis en una condición
edad = 25
es_miembro = True
codigo_descuento = "VIP"

if (edad > 18 and es_miembro) or codigo_descuento == "VIP":
    print("Tienes acceso al evento exclusivo.")
else:
    print("No tienes acceso al evento exclusivo.")

# Combinar Múltiples Condiciones con Paréntesis
salario = 3000
es_tiempo_completo = True
antiguedad = 2

if (salario > 2500 and es_tiempo_completo) or antiguedad >= 5:
    print("Eres elegible para el bono anual.")
else:
    print("No eres elegible para el bono anual.")

##########################################################################
############################## Parte 2 ###################################
##########################################################################

#Ejemplo básico de if
temperatura = 30
if temperatura > 25:
    print("Hace calor afuera.")
else:
    print("Hace frío afuera.")

# Condiciones Booleanas en if
edad = 20
tiene_permiso = True

if edad >= 18 and tiene_permiso:
    print("Puedes conducir un auto")
else:
    print("No puedes conducir un auto")


#Uso Práctico de if en Validaciones
# Validación de entrada de usuario
entrada = input("Ingrese un número: ")
if entrada.isdigit():    
    numero = int(entrada)    
    print(f"El cuadrado de {numero} es {numero**2}")


# Ejemplo de if-else
hor = 10
if hor < 12:
    print("Buenos días")
else:
    print("Buenas tardes")

# Comparaciones y Alternativas en if-else
# Comparación de dos números
a = 10
b = 20
if a > b:    
    print(f"{a} es mayor que {b}")
else:    
    print(f"{a} no es mayor que {b}")

# Ejemplo de Validación de Edad con if-else
edad = 17
if edad >= 18:
    print("Acceso permitido.")
else:
    print("Acceso denegado.")

# Ejemplo de if-elif-else
dia = "miércoles"

if dia == "lunes":
    print("Hoy es lunes.")
elif dia == "martes":
    print("Hoy es martes.")
elif dia == "miércoles":
    print("Hoy es miércoles.")
else:
    print("No es lunes, martes ni miércoles.")

# Verificación de Rangos de Valores
nota = 85
if nota >= 90:
    print("Excelente")
elif nota >= 75:
    print("Bueno")      
elif nota >= 60:
    print("Suficiente")
else:
    print("Insuficiente")

# Ejemplo Completo de if-elif-else
# Determinar el tipo de triángulo según sus lados
lado1 = 5
lado2 = 5
lado3 = 5
if lado1 == lado2 == lado3:    
    print("Triángulo equilátero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:    
    print("Triángulo isósceles")
else:    
    print("Triángulo escaleno")

# Ejemplo de expresión ternaria
edad = 20
mensaje = "Mayor de edad" if edad >= 18 else "Menor de edad"
print(mensaje)

# Forma tradicional
if edad >= 18:
    mensaje = "Acceso permitido"
else:
    mensaje = "Acceso denegado"

# Forma ternaria
mensaje = "Acceso permitido" if edad >= 18 else "Acceso denegado"


# Ejemplo de Condición de Aprobación con Ternaria
nota = 70 
resultado = "Aprobado" if nota >= 60 else "Reprobado"
print(f"El estudiante está: {resultado}")

# Ejemplo Práctico: Validación de Entrada
# Validación de entrada con expresión ternaria
edad_str = input("Ingrese su edad: ")
edad = int(edad_str) if edad_str.isdigit() else 0
print("Edad válida" if edad > 0 else "Edad inválida")

