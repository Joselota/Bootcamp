# Clasificación por edad y evaluación de beneficio

# 1) Solicitar datos
edad_txt = input("Ingrese su edad: ").strip()
categoria = input("Ingrese su categoría (estudiante/docente/visitante): ").strip().lower()

# 6) Validar entradas
if not edad_txt.isdigit():
    print("❌ Error: la edad debe ser un número entero.")
    raise SystemExit

edad = int(edad_txt)

if edad < 0 or edad > 120:
    print("❌ Error: edad fuera de rango.")
    raise SystemExit

if categoria not in ("estudiante", "docente", "visitante"):
    print("❌ Error: categoría no válida.")
    raise SystemExit

# 2) Clasificar edad
if edad < 13:
    clasificacion = "Infancia"
elif edad <= 17:
    clasificacion = "Adolescencia"
elif edad <= 64:
    clasificacion = "Adultez"
else:
    clasificacion = "Persona mayor"

# 3) Evaluar acceso al beneficio
accede = (edad >= 18) and (categoria == "estudiante" or categoria == "docente")

# 4) Ternaria para mostrar acceso
mensaje_acceso = "✅ Accede al beneficio" if accede else "⛔ No accede al beneficio"

# 5) Resumen final
print("\n--- Resumen ---")
print(f"Edad: {edad}")
print(f"Categoría: {categoria}")
print(f"Etapa de vida: {clasificacion}")
print(mensaje_acceso)
