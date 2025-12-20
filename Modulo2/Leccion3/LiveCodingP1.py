# Demo: sistema simple de validación de acceso según edad, rol y estado

# 1) Solicitar nombre, edad y rol
nombre = input("Ingresa tu nombre: ").strip()

# Validación básica de edad (para evitar que reviente si escriben letras)
edad_txt = input("Ingresa tu edad: ").strip()
if not edad_txt.isdigit():
    print("❌ Edad inválida. Debes ingresar un número entero (ej: 18).")
    raise SystemExit

edad = int(edad_txt)

rol = input("Ingresa tu rol (estudiante/docente/otro): ").strip().lower()

# Estado (activo/inactivo) para introducir condición negativa con 'not'
estado = input("Estado de la cuenta (activo/inactivo): ").strip().lower()

# Normalizamos rol para evitar variantes raras
if rol not in ("estudiante", "docente", "otro"):
    rol = "otro"

# 2) Evaluar si puede acceder a una función especial según edad y rol
# Regla ejemplo:
# - Si la cuenta está inactiva -> NO puede acceder (prioridad alta)
# - Docente activo -> accede siempre
# - Estudiante activo -> accede si edad >= 18
# - Otro activo -> accede si edad >= 21

# 3) Aplicar if, elif, else con and, or, not + paréntesis para claridad
if not (estado == "activo"):
    puede_acceder = False
    motivo = "tu cuenta está inactiva"
elif (rol == "docente") and (estado == "activo"):
    puede_acceder = True
    motivo = "eres docente con cuenta activa"
elif (rol == "estudiante") and (estado == "activo") and (edad >= 18):
    puede_acceder = True
    motivo = "eres estudiante y tienes edad suficiente"
else:
    # Aquí cae: estudiante menor de 18, u 'otro' menor de 21, etc.
    if rol == "estudiante":
        puede_acceder = False
        motivo = "eres estudiante pero no cumples la edad mínima (18)"
    elif rol == "otro":
        puede_acceder = (estado == "activo") and (edad >= 21)
        motivo = "para 'otro' la edad mínima es 21" if not puede_acceder else "cumples la condición para 'otro'"
    else:
        # por si acaso
        puede_acceder = False
        motivo = "rol no reconocido"

# 4) Mostrar mensaje personalizado
print("\n--- Resultado ---")
print(f"Nombre: {nombre}")
print(f"Edad: {edad}")
print(f"Rol: {rol}")
print(f"Estado: {estado}")

# 8) Mostrar todos los resultados con print()
if puede_acceder:
    print(f"✅ Acceso concedido, {nombre}. Motivo: {motivo}.")
else:
    print(f"⛔ Acceso denegado, {nombre}. Motivo: {motivo}.")
