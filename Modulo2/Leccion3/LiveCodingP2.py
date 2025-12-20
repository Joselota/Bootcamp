# Demo: Clasificar por edad y validar acceso a un beneficio

# 1) Solicitar edad y categoría
edad_txt = input("Ingrese su edad: ").strip()
categoria = input("Ingrese su categoría (estudiante/docente/visitante): ").strip().lower()

# 4) Validaciones adicionales (entrada inválida)
if not edad_txt.isdigit():
    print("❌ Edad inválida. Debes ingresar un número entero (ej: 20).")
    raise SystemExit

edad = int(edad_txt)

if edad < 0 or edad > 120:
    print("❌ Edad fuera de rango. Ingresa un valor entre 0 y 120.")
    raise SystemExit

categorias_validas = ("estudiante", "docente", "visitante")
if categoria not in categorias_validas:
    print("⚠️ Categoría no válida. Usa: estudiante, docente o visitante.")
    raise SystemExit

# 2) Evaluar múltiples condiciones usando if-elif-else (clasificación por edad)
if edad <= 12:
    grupo = "niño/a"
elif edad <= 17:
    grupo = "adolescente"
elif edad <= 59:
    grupo = "adulto/a"
else:
    grupo = "adulto/a mayor"

# Reglas del beneficio (puedes ajustarlas si tu profe definió otras)
if categoria == "estudiante":
    acceso_beneficio = edad >= 18
elif categoria == "docente":
    acceso_beneficio = edad >= 21
else:  # visitante
    acceso_beneficio = False

# 3) Expresión ternaria para mensaje resumen
resumen = "✅ Accede al beneficio" if acceso_beneficio else "⛔ No accede al beneficio"

# 6) Mostrar resultados personalizados
print("\n--- Resultado ---")
print(f"Edad: {edad}")
print(f"Categoría: {categoria}")
print(f"Clasificación: {grupo}")
print(resumen)

# 7) Comparación: sintaxis tradicional vs ternaria (solo para mostrar en la demo)
# Tradicional:
# if acceso_beneficio:
#     resumen2 = "✅ Accede al beneficio"
# else:
#     resumen2 = "⛔ No accede al beneficio"
#
# Ternaria:
# resumen2 = "✅ Accede al beneficio" if acceso_beneficio else "⛔ No accede al beneficio"
