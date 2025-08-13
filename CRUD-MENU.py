import random
estudiantes = []
clases = []
asistencias = []

def generar_legajo():
    while True:
        legajo = random.randint(1000, 9999)
        existe = 0
        for fila in estudiantes:
            if fila[0] == legajo:
                existe = 1
        if existe == 0:
            return legajo

def agregar_estudiante():
    legajo = generar_legajo()
    dni = int(input("Ingrese DNI del estudiante: "))
    while len(str(dni)) != 7 and len(str(dni)) != 8:
        print("DNI incorrecto, ingrese DNI sin puntos ni espacios")
        dni = int(input("Ingrese DNI del estudiante: "))
    nombre = input("Ingrese nombre del estudiante: ").title()
    while len(str(nombre)) < 3:
        print("Nombre muy corto, intente nuevamente")
        nombre = input("Ingrese nombre del estudiante: ").title()
    fila = [legajo, dni, nombre]
    estudiantes.append(fila)
    print("Estudiante agregado correctamente. Legajo asignado:", legajo)

def listar_estudiantes():
    print("Legajo   DNI     Nombre")
    for fila in estudiantes:
        print(fila[0], " ", fila[1], " ", fila[2])

def ver_estudiante():
    id_buscar = int(input("Ingrese Legajo del estudiante: "))
    encontrado = 0
    for fila in estudiantes:
        if fila[0] == id_buscar:
            print("Legajo:", fila[0], "DNI:", fila[1], "Nombre:", fila[2])
            encontrado = 1
    if encontrado == 0:
        print("No se encontró ese estudiante.")

def actualizar_estudiante():
    id_buscar = int(input("Ingrese legajo del estudiante a actualizar: "))
    for fila in estudiantes:
        if fila[0] == id_buscar:
            nuevo_nombre = input("Nuevo nombre: ")
            fila[2] = nuevo_nombre
            print("Nombre actualizado.")

def eliminar_estudiante():
    id_buscar = int(input("Ingrese legajo del estudiante a eliminar: "))
    indice = -1
    contador = 0
    for fila in estudiantes:
        if fila[0] == id_buscar:
            indice = contador
        contador = contador + 1
    if indice != -1:
        estudiantes.pop(indice)
        print("Estudiante eliminado.")
    else:
        print("No se encontró ese estudiante.")

def menu_estudiantes():
    seguir = 1
    while seguir == 1:
        print("\n=== GESTIÓN DE ESTUDIANTES ===")
        print("1) Agregar estudiante")
        print("2) Listar estudiantes")
        print("3) Ver un estudiante")
        print("4) Actualizar estudiante")
        print("5) Eliminar estudiante")
        print("0) Salir")

        opcion = input("Elija una opción: ")

        if opcion == "1":
            agregar_estudiante()
        elif opcion == "2":
            listar_estudiantes()
        elif opcion == "3":
            ver_estudiante()
        elif opcion == "4":
            actualizar_estudiante()
        elif opcion == "5":
            eliminar_estudiante()
        elif opcion == "0":
            seguir = 0
        else:
            print("Opción inválida.")

def agregar_clase():
    codigo = int(input("Ingrese CÓDIGO de la clase: "))
    materia = input("Ingrese Materia: ").title
    fecha = input("Ingrese Fecha (ej: 2025-09-01): ")
    hora = input("Ingrese Hora (ej: 08:00): ")
    fila = [codigo, materia, fecha, hora]
    clases.append(fila)
    print("Clase agregada correctamente.")

def listar_clases():
    print("\nCódigo   Materia           Fecha        Hora")
    if len(clases) == 0:
        print("(no hay clases cargadas)")
    else:
        for fila in clases:
            print(fila[0], " ", fila[1], " ", fila[2], " ", fila[3])

def ver_clase():
    codigo_buscar = int(input("Ingrese CÓDIGO de la clase: "))
    encontrado = 0
    for fila in clases:
        if fila[0] == codigo_buscar:
            print("Código:", fila[0], "Materia:", fila[1], "Fecha:", fila[2], "Hora:", fila[3])
            encontrado = 1
    if encontrado == 0:
        print("No se encontró esa clase.")

def actualizar_clase():
    codigo_buscar = int(input("Ingrese CÓDIGO de la clase a actualizar: "))
    actualizo = 0
    for fila in clases:
        if fila[0] == codigo_buscar:
            nueva_materia = input("Nueva Materia: ")
            nueva_fecha = input("Nueva Fecha (ej: 2025-09-01): ")
            nueva_hora = input("Nueva Hora (ej: 08:00): ")
            fila[1] = nueva_materia
            fila[2] = nueva_fecha
            fila[3] = nueva_hora
            actualizo = 1
            print("Clase actualizada.")
    if actualizo == 0:
        print("No se encontró esa clase.")

def eliminar_clase():
    codigo_buscar = int(input("Ingrese CÓDIGO de la clase a eliminar: "))
    indice = -1
    i = 0
    for fila in clases:
        if fila[0] == codigo_buscar:
            indice = i
        i = i + 1
    if indice != -1:
        clases.pop(indice)
        print("Clase eliminada.")
    else:
        print("No se encontró esa clase.")

def menu_clases():
    seguir = 1
    while seguir == 1:
        print("\n=== GESTIÓN DE CLASES ===")
        print("1) Agregar clase")
        print("2) Listar clases")
        print("3) Ver una clase")
        print("4) Actualizar clase")
        print("5) Eliminar clase")
        print("0) Salir")

        opcion = input("Elija una opción: ")

        if opcion == "1":
            agregar_clase()
        elif opcion == "2":
            listar_clases()
        elif opcion == "3":
            ver_clase()
        elif opcion == "4":
            actualizar_clase()
        elif opcion == "5":
            eliminar_clase()
        elif opcion == "0":
            seguir = 0
        else:
            print("Opción inválida.")

def buscar_estudiante_por_legajo(legajo):
    indice = -1
    i = 0
    for fila in estudiantes:
        if fila[0] == legajo:
            indice = i
        i = i + 1
    return indice  # -1 si no está

def buscar_clase_por_codigo(codigo):
    indice = -1
    i = 0
    for fila in clases:
        if fila[0] == codigo:
            indice = i
        i = i + 1
    return indice  # -1 si no está

def buscar_asistencia(legajo, codigo):
    indice = -1
    i = 0
    for fila in asistencias:
        if fila[0] == legajo and fila[2] == codigo:
            indice = i
        i = i + 1
    return indice  # -1 si no está

def agregar_asistencia():
    legajo = int(input("Ingrese LEGAJO del estudiante: "))
    idx_est = buscar_estudiante_por_legajo(legajo)
    if idx_est == -1:
        print("No se encontró ese estudiante.")
    else:
        codigo = int(input("Ingrese CÓDIGO de la clase: "))
        idx_cla = buscar_clase_por_codigo(codigo)
        if idx_cla == -1:
            print("No se encontró esa clase.")
        else:
            texto = input("¿Estuvo presente? (s/n): ")
            if texto == "s":
                estado = "Presente"
            else:
                estado = "Ausente"
            dni = estudiantes[idx_est][1]
            fila = [legajo, dni, codigo, estado]
            asistencias.append(fila)
            print("Asistencia registrada.")

def listar_asistencias():
    print("\nLegajo   DNI        Clase  Materia           Fecha        Estado")
    if len(asistencias) == 0:
        print("(no hay asistencias registradas)")
    else:
        for fila in asistencias:
            legajo = fila[0]
            dni = fila[1]
            codigo = fila[2]
            estado = fila[3]

            # buscar datos de la clase para mostrar materia/fecha
            idx_cla = buscar_clase_por_codigo(codigo)
            if idx_cla != -1:
                materia = clases[idx_cla][1]
                fecha = clases[idx_cla][2]
            else:
                materia = "-"
                fecha = "-"

            print(legajo, " ", dni, " ", codigo, " ", materia, " ", fecha, " ", estado)

def ver_asistencias_por_estudiante():
    legajo = int(input("Ingrese LEGAJO del estudiante: "))
    print("\nLegajo   DNI        Clase  Materia           Fecha        Estado")
    encontrado = 0
    for fila in asistencias:
        if fila[0] == legajo:
            codigo = fila[2]
            estado = fila[3]
            dni = fila[1]
            idx_cla = buscar_clase_por_codigo(codigo)
            if idx_cla != -1:
                materia = clases[idx_cla][1]
                fecha = clases[idx_cla][2]
            else:
                materia = "-"
                fecha = "-"
            print(legajo, " ", dni, " ", codigo, " ", materia, " ", fecha, " ", estado)
            encontrado = 1
    if encontrado == 0:
        print("(no hay registros para ese estudiante)")

def ver_asistencias_por_clase():
    codigo = int(input("Ingrese CÓDIGO de la clase: "))
    print("\nLegajo   DNI        Clase  Materia           Fecha        Estado")
    encontrado = 0
    for fila in asistencias:
        if fila[2] == codigo:
            legajo = fila[0]
            dni = fila[1]
            estado = fila[3]
            idx_cla = buscar_clase_por_codigo(codigo)
            if idx_cla != -1:
                materia = clases[idx_cla][1]
                fecha = clases[idx_cla][2]
            else:
                materia = "-"
                fecha = "-"
            print(legajo, " ", dni, " ", codigo, " ", materia, " ", fecha, " ", estado)
            encontrado = 1
    if encontrado == 0:
        print("(no hay registros para esa clase)")

def actualizar_asistencia():
    legajo = int(input("Ingrese LEGAJO del estudiante: "))
    codigo = int(input("Ingrese CÓDIGO de la clase: "))
    idx = buscar_asistencia(legajo, codigo)
    if idx == -1:
        print("No existe ese registro de asistencia.")
    else:
        texto = input("Nuevo estado ¿Presente? (s/n): ")
        if texto == "s":
            estado = "Presente"
        else:
            estado = "Ausente"
        asistencias[idx][3] = estado
        print("Asistencia actualizada.")

def eliminar_asistencia():
    legajo = int(input("Ingrese LEGAJO del estudiante: "))
    codigo = int(input("Ingrese CÓDIGO de la clase: "))
    idx = buscar_asistencia(legajo, codigo)
    if idx == -1:
        print("No existe ese registro de asistencia.")
    else:
        asistencias.pop(idx)
        print("Asistencia eliminada.")

def menu_asistencias():
    seguir = 1
    while seguir == 1:
        print("\n=== REGISTRO DE ASISTENCIAS ===")
        print("1) Agregar asistencia")
        print("2) Listar asistencias")
        print("3) Ver por estudiante")
        print("4) Ver por clase")
        print("5) Actualizar asistencia")
        print("6) Eliminar asistencia")
        print("0) Salir")
        opcion = input("Elija una opción: ")

        if opcion == "1":
            agregar_asistencia()
        elif opcion == "2":
            listar_asistencias()
        elif opcion == "3":
            ver_asistencias_por_estudiante()
        elif opcion == "4":
            ver_asistencias_por_clase()
        elif opcion == "5":
            actualizar_asistencia()
        elif opcion == "6":
            eliminar_asistencia()
        elif opcion == "0":
            seguir = 0
        else:
            print("Opción inválida.")

def menu_principal():
    seguir = 1
    while seguir == 1:
        print("\n=== SISTEMA DE ASISTENCIAS ===")
        print("1) Gestión de estudiantes")
        print("2) Gestión de clases")
        print("3) Registro de asistencias")
        print("0) Salir")
        opcion = input("Elija una opción: ")

        if opcion == "1":
            menu_estudiantes()
        elif opcion == "2":
            menu_clases()
        elif opcion == "3":
            menu_asistencias()
        elif opcion == "0":
            seguir = 0
        else:
            print("Opción inválida.")

menu_principal()