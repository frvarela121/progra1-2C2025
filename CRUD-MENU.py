import random
estudiantes = []
clases = []
asistencias = []

# === REGISTRO DE ESTUDIANTES ===
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
    print("Legajo   DNI       Nombre")
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

# === REGISTRO DE CLASES ===

def agregar_clase():
    codigo = int(input("Ingrese CÓDIGO de la clase: "))
    materia = input("Ingrese Materia: ").title()
    fecha = input("Ingrese Fecha (ej: 2025-09-01): ")
    fila = [codigo, materia, fecha, ]
    clases.append(fila)
    print("Clase agregada correctamente.")

def listar_clases():
    print("\nCódigo   Materia           Fecha")
    if len(clases) == 0:
        print("(no hay clases cargadas)")
    else:
        for fila in clases:
            print(fila[0], " ", fila[1], " ", fila[2],)

def ver_clase():
    codigo_buscar = int(input("Ingrese CÓDIGO de la clase: "))
    encontrado = 0
    for fila in clases:
        if fila[0] == codigo_buscar:
            print("Código:", fila[0], "Materia:", fila[1], "Fecha:", fila[2])
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
            fila[1] = nueva_materia
            fila[2] = nueva_fecha
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

def buscar_clase_por_codigo(codigo):
    indice = -1
    i = 0
    for fila in clases:
        if fila[0] == codigo:
            indice = i
        i = i + 1
    return indice  # -1 si no está

# === REGISTRO DE ASISTENCIAS ===

def buscar_asistencia(legajo, codigo):
    indice = -1
    i = 0
    for fila in asistencias:
        if fila[0] == legajo and fila[2] == codigo:
            indice = i
        i = i + 1
    return indice  # -1 si no está

def agregar_asistencia():
    if len(estudiantes) == 0:
        print("No hay estudiantes cargados.")
        return

    codigo = int(input("Ingrese CÓDIGO de la clase: "))
    idx_cla = buscar_clase_por_codigo(codigo)
    if idx_cla == -1:
        print("No se encontró esa clase.")
        return

    for est in estudiantes:
        print(f"Estudiante: {est[2]} (Legajo: {est[0]}, DNI: {est[1]})")
        texto = input("¿Estuvo presente? (s/n): ")
        if texto.lower() == "s":
            estado = "Presente"
        else:
            estado = "Ausente"
        fila = [est[0], est[1], codigo, estado]
        asistencias.append(fila)
    
    print("Asistencias registradas para toda la clase.")

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

def consultar_estudiante_con_asistencias():
    print("\n=== Consultar ESTUDIANTE + asistencias ===")
    legajo = int(input("Ingrese LEGAJO del estudiante: "))

    # buscar estudiante
    idx_est = -1
    i = 0
    for fila in estudiantes:
        if fila[0] == legajo:
            idx_est = i
        i = i + 1

    if idx_est == -1:
        print("No se encontró ese estudiante.")
    else:
        dni = estudiantes[idx_est][1]
        nombre = estudiantes[idx_est][2]
        print("Estudiante => Legajo:", legajo, " DNI:", dni, " Nombre:", nombre)
        print("Asistencias (Clase / Materia / Fecha / Estado):")

        hay = 0
        for a in asistencias:
            if a[0] == legajo:
                codigo = a[2]
                estado = a[3]
                # datos de la clase
                idx_cla = -1
                j = 0
                for c in clases:
                    if c[0] == codigo:
                        idx_cla = j
                    j = j + 1
                if idx_cla != -1:
                    materia = clases[idx_cla][1]
                    fecha = clases[idx_cla][2]
                else:
                    materia = "-"
                    fecha = "-"
                print("  ", codigo, "/", materia, "/", fecha, "/", estado)
                hay = 1
        if hay == 0:
            print("  (sin registros)")

def consultar_clase_con_asistencias():
    print("\n=== Consultar CLASE + asistencias ===")
    codigo = int(input("Ingrese CÓDIGO de la clase: "))

    # buscar clase
    idx_cla = -1
    i = 0
    for c in clases:
        if c[0] == codigo:
            idx_cla = i
        i = i + 1

    if idx_cla == -1:
        print("No se encontró esa clase.")
    else:
        materia = clases[idx_cla][1]
        fecha = clases[idx_cla][2]
        hora = clases[idx_cla][3]
        print("Clase => Código:", codigo, " Materia:", materia, " Fecha:", fecha, " Hora:", hora)
        print("Asistentes (Legajo / DNI / Estado):")

        hay = 0
        for a in asistencias:
            if a[2] == codigo:
                print("  ", a[0], "/", a[1], "/", a[3])
                hay = 1
        if hay == 0:
            print("  (sin registros)")

# === ESTADÍSTICAS BÁSICAS ===

def promedio_asistencia_general():
    total = 0
    presentes = 0
    for a in asistencias:
        total = total + 1
        if a[3] == "Presente":
            presentes = presentes + 1
    if total == 0:
        print("Promedio general de asistencia: 0.00% (no hay registros)")
    else:
        porc = presentes * 100.0 / total
        print("Promedio general de asistencia:", f"{porc:.2f}%", " (", presentes, "/", total, ")")

def promedio_asistencia_por_clase():
    print("\n=== Promedio de asistencia por CLASE ===")
    if len(clases) == 0:
        print("(no hay clases)")
    else:
        # por cada clase, contar presentes/total
        for c in clases:
            codigo = c[0]
            presentes = 0
            total = 0
            for a in asistencias:
                if a[2] == codigo:
                    total = total + 1
                    if a[3] == "Presente":
                        presentes = presentes + 1
            if total == 0:
                print("Clase", codigo, "=> 0.00% (0/0)")
            else:
                porc = presentes * 100.0 / total
                print("Clase", codigo, "=>", f"{porc:.2f}%", " (", presentes, "/", total, ")")

def promedio_asistencia_por_estudiante():
    print("\n=== Promedio de asistencia por ESTUDIANTE ===")
    if len(estudiantes) == 0:
        print("(no hay estudiantes)")
    else:
        for e in estudiantes:
            legajo = e[0]
            presentes = 0
            total = 0
            for a in asistencias:
                if a[0] == legajo:
                    total = total + 1
                    if a[3] == "Presente":
                        presentes = presentes + 1
            if total == 0:
                print("Legajo", legajo, "=> 0.00% (0/0)")
            else:
                porc = presentes * 100.0 / total
                print("Legajo", legajo, "=>", f"{porc:.2f}%", " (", presentes, "/", total, ")")

def conteos_totales_y_por_estado():
    print("\n=== Conteos totales y por estado ===")
    print("Total estudiantes:", len(estudiantes))
    print("Total clases:", len(clases))
    print("Total registros de asistencia:", len(asistencias))

    presentes = 0
    ausentes = 0
    for a in asistencias:
        if a[3] == "Presente":
            presentes = presentes + 1
        else:
            ausentes = ausentes + 1
    print("Presentes:", presentes, " | Ausentes:", ausentes)

def porcentaje_asistencias_por_materia():
    print("\n=== Porcentaje de registros por MATERIA (sobre total de asistencias) ===")
    total = len(asistencias)
    if total == 0:
        print("(no hay asistencias)")
    else:
        # contar asistencias por materia
        # (sin diccionarios: recorremos materias únicas y contamos)
        materias_unicas = []
        for c in clases:
            materia = c[1]
            repetida = 0
            for m in materias_unicas:
                if m == materia:
                    repetida = 1
            if repetida == 0:
                materias_unicas.append(materia)

        for materia in materias_unicas:
            cuenta = 0
            # contar asistencias cuyo codigo de clase tenga esta materia
            for a in asistencias:
                codigo = a[2]
                # buscar clase
                i = 0
                idx = -1
                for c in clases:
                    if c[0] == codigo:
                        idx = i
                    i = i + 1
                if idx != -1:
                    if clases[idx][1] == materia:
                        cuenta = cuenta + 1
            porc = cuenta * 100.0 / total
            print(materia, "=>", f"{porc:.2f}%", " (", cuenta, "/", total, ")")

def max_min_clase_por_asistencia():
    print("\n=== Clase con MAYOR y MENOR % asistencia ===")
    # calcular % por clase y guardar mejor/peor
    mejor_codigo = -1
    mejor_porc = -1.0
    peor_codigo = -1
    peor_porc = 101.0

    for c in clases:
        codigo = c[0]
        presentes = 0
        total = 0
        for a in asistencias:
            if a[2] == codigo:
                total = total + 1
                if a[3] == "Presente":
                    presentes = presentes + 1
        if total > 0:
            porc = presentes * 100.0 / total
            if porc > mejor_porc:
                mejor_porc = porc
                mejor_codigo = codigo
            if porc < peor_porc:
                peor_porc = porc
                peor_codigo = codigo

    if mejor_codigo == -1:
        print("(no hay clases con asistencias registradas)")
    else:
        print("Mejor clase:", mejor_codigo, "=>", f"{mejor_porc:.2f}%")
        print("Peor clase:", peor_codigo, "=>", f"{peor_porc:.2f}%")

def max_min_estudiante_por_presentes():
    print("\n=== Estudiante con MÁS y MENOS presentes ===")
    if len(estudiantes) == 0:
        print("(no hay estudiantes)")
    else:
        mejor_legajo = -1
        mejor_count = -1
        peor_legajo = -1
        peor_count = 999999

        # solo consideramos estudiantes con al menos 1 registro para el mínimo real
        # si ninguno tiene registros, mostramos 0
        hay_registros = 0

        for e in estudiantes:
            legajo = e[0]
            presentes = 0
            registros = 0
            for a in asistencias:
                if a[0] == legajo:
                    registros = registros + 1
                    if a[3] == "Presente":
                        presentes = presentes + 1
            if registros > 0:
                hay_registros = 1
                if presentes > mejor_count:
                    mejor_count = presentes
                    mejor_legajo = legajo
                if presentes < peor_count:
                    peor_count = presentes
                    peor_legajo = legajo

        if hay_registros == 0:
            print("(no hay asistencias registradas)")
        else:
            print("Más presentes => Legajo", mejor_legajo, ":", mejor_count)
            print("Menos presentes => Legajo", peor_legajo, ":", peor_count)

# === MENUS ===

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

def menu_estadisticas():
    seguir = 1
    while seguir == 1:
        print("\n=== ESTADÍSTICAS ===")
        print("1) Promedio general de asistencia")
        print("2) Promedio por clase")
        print("3) Promedio por estudiante")
        print("4) Conteos totales y por estado")
        print("5) % de asistencias por materia (sobre el total)")
        print("6) Clase con mayor y menor % asistencia")
        print("7) Estudiante con más y menos presentes")
        print("0) Volver")
        opcion = input("Elija una opción: ")

        if opcion == "1":
            promedio_asistencia_general()
        elif opcion == "2":
            promedio_asistencia_por_clase()
        elif opcion == "3":
            promedio_asistencia_por_estudiante()
        elif opcion == "4":
            conteos_totales_y_por_estado()
        elif opcion == "5":
            porcentaje_asistencias_por_materia()
        elif opcion == "6":
            max_min_clase_por_asistencia()
        elif opcion == "7":
            max_min_estudiante_por_presentes()
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
        print("4) Consultas con relacionados")
        print("5) Estadísticas")
        print("0) Salir")
        opcion = input("Elija una opción: ")

        if opcion == "1":
            menu_estudiantes()
        elif opcion == "2":
            menu_clases()
        elif opcion == "3":
            menu_asistencias()
        elif opcion == "4":
            # mini menú de consultas
            print("\n1) Estudiante + asistencias")
            print("2) Clase + asistencias")
            print("0) Volver")
            sub = input("Opción: ")
            if sub == "1":
                consultar_estudiante_con_asistencias()
            elif sub == "2":
                consultar_clase_con_asistencias()
        elif opcion == "5":
            menu_estadisticas()
        elif opcion == "0":
            seguir = 0
        else:
            print("Opción inválida.")

menu_principal()