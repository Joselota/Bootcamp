# Acceso permitido: demo de condicionales y booleanos

nombre = input("Ingrese su nombre: ").strip()

edad_txt = input("Ingrese su edad: ").strip()
if not edad_txt.isdigit():
    print("❌ Edad inválida. Debes ingresar un número entero (ej: 19).")
    raise SystemExit

edad = int(edad_txt)

rol = input("Ingrese su rol (estudiante/docente/otro): ").strip().lower()

# Validar rol
roles_validos = ("estudiante", "docente", "otro")
if rol not in roles_validos:
    print(f"⚠️ Rol '{rol}' no es válido. Por favor, revíselo e intente nuevamente.")
    raise SystemExit

# Evaluar condiciones
if edad > 18 and (rol == "estudiante" or rol == "docente"):
    print(f"✅ Acceso permitido, {nombre}. (Edad: {edad}, Rol: {rol})")

elif edad < 18:
    print(f"⛔ Acceso denegado, {nombre}. Debes ser mayor de 18 años. (Edad: {edad})")

else:
    # Aquí cae, por ejemplo: edad == 18, o rol == "otro" aunque sea mayor de 18
    if edad == 18:
        print(f"⛔ Acceso denegado, {nombre}. La condición es 'mayor de 18' (no incluye 18).")
    elif rol == "otro":
        print(f"⛔ Acceso denegado, {nombre}. Solo 'estudiante' o 'docente' pueden acceder.")
    else:
        print(f"⛔ Acceso denegado, {nombre}. No cumples las condiciones de acceso.")
