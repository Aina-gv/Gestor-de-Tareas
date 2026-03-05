misTareas = []
misTareasPendientes = []
misTareasCompletadas = []

ejemploTarea = {"descripción" : "Estudiar" , "prioridad" : "media" , "completada" : False}

def GestorDeTareas():
    while True:
        print("""
---[ Gestor de Tareas ]---
1. Agregar Tarea
2. Completar Tarea
3. Eliminar Tarea
4. Listar tareas pendientes
5. Listar tareas completadas
6. Listar todas las tareas
7. Mostrar estadísticas
8. Mostrar gráficos
9. Salir
        """)
        a = input("Elige una opción: ")
        # El usuario elige una opción para las diferentes funciones
        if a == "1":
            AgregarTarea(misTareas)
            Update()
        elif a == "2":
            CompletarTarea(misTareas)
            Update()
        elif a == "3":
            EliminarTarea(misTareas)
            Update()
        elif a == "4":
            ListarTareas(misTareas,"pendientes")
            input("Presiona intro para continuar: ")
        elif a == "5":
            ListarTareas(misTareas,"completadas")
            input("Presiona intro para continuar: ")
        elif a == "6":
            ListarTareas(misTareas,"todas")
            input("Presiona intro para continuar: ")
        elif a == "7":
            MostrarEstadisticas(misTareas)
            input("Presiona intro para continuar: ")
        elif a == "8":
            MostrarGraficos(misTareas)
            input("Presiona intro para continuar: ")
        elif a == "9":
            print("Saliendo del programa...")
            break
        else:
            print("Seleccione una opción válida")

def AgregarTarea(tareas):
    print("-> Agregar Tarea <-")

    # Comprobamos que la descripción es única
    while True:
        check = True
        desc = input("Describa la tarea: ")
        for tarea in tareas:
            if tarea["descripción"] == desc:
                print("No puedes tener múltiples tareas con el mismo nombre")
                check = False # si está duplicado, el bucle no se rompe
        if check:
            break

    # Comprobamos prioridad
    prior = input("Indique la prioridad de la tarea. [1] baja, [2] media, [3] alta: ")
    while prior not in ["1","2","3"]:
        print("Por favor, Escriba una de las opciones válidas")
        prior = input("Indique la prioridad de la tarea. [1] baja, [2] media, [3] alta: ")
    # Cambiamos de formato numérico a formato de texto para mejor uso de texto
    if prior == "1":
        prior = "baja"
    elif prior == "2":
        prior = "media"
    elif prior == "3":
        prior = "alta"

    # Comprobamos día de la semana
    dia_semana = input("Indique el día de la semana (lunes, martes, miércoles, jueves, viernes, sábado, domingo): ").lower()
    while dia_semana not in ["lunes","martes","miercoles","miércoles","jueves","viernes","sabado","sábado","domingo"]:
        print("Por favor, escriba un día válido.")
        if dia_semana == "miercoles":
            dia_semana = "miércoles"
        if dia_semana == "sabado":
            dia_semana = "sábado"

        dia_semana = input("Indique el día de la semana (lunes, martes, miércoles, jueves, viernes, sábado, domingo): ").lower()

    # Preguntamos el día del mes (1 a 31)
    dia_mes = input("Indique el día del mes (1-31): ")
    while not (dia_mes.isdigit() and 1 <= int(dia_mes) <= 31):
        print("Por favor, escriba un número de día válido (1-31).")
        dia_mes = input("Indique el día del mes (1-31): ")
    dia_mes = int(dia_mes)

    # Preguntamos el número de mes (1 a 12)
    mes_num = input("Indique el mes (1-12): ")
    while not (mes_num.isdigit() and 1 <= int(mes_num) <= 12):
        print("Por favor, escriba un número de mes válido (1-12).")
        mes_num = input("Indique el mes (1-12): ")
    mes_num = int(mes_num)

    # Añadimos tarea
    tareas.append({
        "descripción" : desc,
        "prioridad"   : prior,
        "completada"  : False,
        "día_semana"  : dia_semana,
        "día_mes"     : dia_mes,
        "mes"         : mes_num
    })
    print(f"-> Tarea {desc} de prioridad {prior} creada como incompleta ")

def ListarTareas(tareas,modo):
    if modo == "todas":
        print("Listando todas las tareas...")
    else:
        print(f"Listando tareas {modo}...")

    count = 1
    for tarea in tareas:
        if tarea["completada"]:
            completada = "✓"
        else:
            completada = " "

        if (tarea["completada"] and modo == "completadas") \
           or (not tarea["completada"] and modo == "pendientes") \
           or (modo == "todas"):
            print(f"• {count}: [{completada}] {tarea['descripción']} | "
                  f"Prioridad: {tarea['prioridad']} | "
                  f"Día: {tarea['día_semana']} {tarea['día_mes']} (Mes {tarea['mes']})")
            count += 1

    if count == 1:
        if modo == "todas":
            print("Lista de tareas vacía")
        else:
            print(f"Lista de tareas {modo} vacía")

def Update(tareas=misTareas,tareasPen=misTareasPendientes,tareasCompl=misTareasCompletadas):
    tareasPen.clear()
    tareasCompl.clear()
    for tarea in tareas:
        if tarea["completada"]:
            tareasCompl.append(tarea)
        else:
            tareasPen.append(tarea)

def CompletarTarea(tareas,tareasPen=misTareasPendientes):
    if len(tareasPen) == 0:
        print("No hay tareas pendientes")
    else:
        ListarTareas(tareasPen,"pendientes")
        print("-> Completar Tarea <-")

        while True:
            a = input("Elige la tarea para completar con su número indicado: ")
            if a.isdigit():
                if 0 < int(a) <= len(tareasPen):
                    a = int(a)
                    a -= 1
                    break
                else:
                    print("El número debe ser una de las opciones señaladas")
            else:
                print("Debes introducir un número")

        desc = tareasPen[a]["descripción"]
        for tarea in tareas:
            if tarea["descripción"] == desc:
                tarea["completada"] = True

        print(f"Tarea '{tareasPen[a]['descripción']}' completada")

def EliminarTarea(tareas):
    if len(tareas) == 0:
        print("No hay tareas")
        return False
    ListarTareas(tareas,"todas")
    print("-> Eliminar Tarea <-")

    while True:
        a = input("Elige la tarea para Eliminar con su número indicado: ")
        if a.isdigit():
            if 0 < int(a) <= len(tareas):
                a = int(a)
                a -= 1
                break
            else:
                print("El número debe ser una de las opciones señaladas")
        else:
            print("Debes introducir un número")

    print(f"Tarea '{tareas[a]['descripción']}' eliminada")
    tareas.pop(a)

def MostrarEstadisticas(tareas,tareasPen=misTareasPendientes,tareasCompl=misTareasCompletadas):
    print("Calculando estadísticas...")
    # Variables tareas pendientes
    tareasPenPriorAlta = 0
    tareasPenPriorMedia = 0
    tareasPenPriorBaja = 0
    # Variables tareas completadas
    tareasComplPriorAlta = 0
    tareasComplPriorMedia = 0
    tareasComplPriorBaja = 0

    # Cálculo de variables
    for tarea in tareas:
        if tarea["prioridad"] == "alta":
            if not tarea["completada"]:
                tareasPenPriorAlta += 1
            else:
                tareasComplPriorAlta += 1
        elif tarea["prioridad"] == "media":
            if not tarea["completada"]:
                tareasPenPriorMedia += 1
            else:
                tareasComplPriorMedia += 1
        elif tarea["prioridad"] == "baja":
            if not tarea["completada"]:
                tareasPenPriorBaja += 1
            else:
                tareasComplPriorBaja += 1

    print("Mostrando estadísticas...")
    print(f'''
Tareas: {len(tareas)}
Tareas completas: {len(tareasCompl)}
Tareas pendientes: {len(tareasPen)}

Tareas de prioridad Alta: {tareasComplPriorAlta} de {tareasComplPriorAlta + tareasPenPriorAlta} completada(s)
Tareas de prioridad Media: {tareasComplPriorMedia} de {tareasComplPriorMedia + tareasPenPriorMedia} completada(s)
Tareas de prioridad Baja: {tareasComplPriorBaja} de {tareasComplPriorBaja + tareasPenPriorBaja} completada(s)
''')

    
def MostrarGraficos(tareas):
    import numpy as np
    import matplotlib.pyplot as plt



    # Variables tareas pendientes
    tareasPenPriorAlta = 0
    tareasPenPriorMedia = 0
    tareasPenPriorBaja = 0
    # Variables tareas completadas
    tareasComplPriorAlta = 0
    tareasComplPriorMedia = 0
    tareasComplPriorBaja = 0

    # Cálculo de variables
    for tarea in tareas:
        if tarea["prioridad"] == "alta":
            if not tarea["completada"]:
                tareasPenPriorAlta += 1
            else:
                tareasComplPriorAlta += 1
        elif tarea["prioridad"] == "media":
            if not tarea["completada"]:
                tareasPenPriorMedia += 1
            else:
                tareasComplPriorMedia += 1
        elif tarea["prioridad"] == "baja":
            if not tarea["completada"]:
                tareasPenPriorBaja += 1
            else:
                tareasComplPriorBaja += 1

    # Gráfico principal (completadas vs. pendientes por prioridad)
    labels = ['Alta', 'Media', 'Baja']
    completadas = [tareasComplPriorAlta, tareasComplPriorMedia, tareasComplPriorBaja]
    pendientes = [tareasPenPriorAlta, tareasPenPriorMedia, tareasPenPriorBaja]

    x = np.arange(len(labels))  # Posiciones para cada barra
    width = 0.35                # Ancho de cada barra

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, completadas, width, label='Completadas', color='green')
    rects2 = ax.bar(x + width/2, pendientes, width, label='Pendientes', color='blue')

    ax.set_ylabel('Cantidad de tareas')
    ax.set_title('Estadísticas de tareas por prioridad')
    ax.set_xticks(x, labels)
    ax.legend()

    for rect in rects1 + rects2:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width()/2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom')

    print("Mostrando gráfico principal")
    plt.tight_layout()
    plt.show()

    input("Presiona intro para continuar...")

    # Gráfico mensual (completadas vs pendientes. por día de mes según el mes )

    import matplotlib.pyplot as plt
    import numpy as np

    mes_elegido = input("¿Para qué mes (1-12) deseas ver las tareas completadas por día? ")
    while not (mes_elegido.isdigit() and 1 <= int(mes_elegido) <= 12):
        print("Por favor, escribe un número de mes válido (1-12).")
        mes_elegido = input("¿Para qué mes (1-12) deseas ver las tareas completadas por día? ")
    mes_elegido = int(mes_elegido)

    completadas_por_dia = {}
    for dia in range(1, 32):
        completadas_por_dia[dia] = 0

    for tarea in tareas:
        if tarea["completada"] and "mes" in tarea and "día_mes" in tarea:
            if tarea["mes"] == mes_elegido:
                dia_tarea = tarea["día_mes"]
                completadas_por_dia[dia_tarea] += 1

    dias_ordenados = sorted(completadas_por_dia.keys())
    cantidades = [completadas_por_dia[d] for d in dias_ordenados]

    fig2, ax2 = plt.subplots()
    ax2.bar(dias_ordenados, cantidades, color='purple')
    ax2.set_xlabel('Día del Mes')
    ax2.set_ylabel('Tareas Completadas')
    ax2.set_title(f"Tareas Completadas en el Mes {mes_elegido}")

    print("Mostrando gráfico mensual")
    plt.tight_layout()
    plt.show()

# Iniciamos el programa
GestorDeTareas()