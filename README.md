
Este proyecto implementa un **Gestor de Tareas interactivo por consola**, escrito en Python. Permite crear, organizar y completar tareas, ofrecer estadísticas automáticas y generar gráficos visuales por prioridad y por mes.

Es un proyecto pensado para practicar:

*   Validación de datos
*   Entrada interactiva del usuario
*   Organización de información
*   Estados de tareas
*   Uso de bibliotecas externas (matplotlib, numpy)
*   Generación de gráficos
*   Buenas prácticas y claridad al trabajar con estructuras de datos

***

# **¿Para qué sirve este proyecto?**

El Gestor de Tareas sirve como un pequeño asistente personal donde puedes:

*   Crear tareas con descripción, prioridad, día de la semana, día del mes y mes
*   Marcar tareas como completadas
*   Eliminar tareas
*   Consultar listas filtradas
*   Ver estadísticas de productividad
*   **Visualizar gráficos** sobre tu rendimiento

En esencia, **te ayuda a organizar tu tiempo y visualizar cómo avanzas**.

***

# **¿Qué problema estoy resolviendo?**

Este proyecto resuelve varias necesidades reales:

### Organizar tareas de manera estructurada

Con prioridad, fecha y estado.

### Evitar duplicados y errores

Incluye validaciones para que no existan tareas repetidas y para que los días/meses sean válidos.

### Ver el progreso de forma visual

Genera **dos gráficos importantes**:

*   Completadas vs. pendientes por prioridad
*   Completadas por día del mes seleccionado

### Tener estadísticas claras

El programa calcula:

*   Tareas totales
*   Cuántas están pendientes
*   Cuántas están completadas
*   Cuántas completas hay por prioridad

***

# **¿Qué hace cada parte del programa?**

El programa está dividido en funciones, cada una con una responsabilidad muy clara (esto mejora la organización y facilita el mantenimiento). [\[campusunie...epoint.com\]](https://campusunie-my.sharepoint.com/personal/agimenovaillo_student_universidadunie_com/Documents/Archivos%20de%20chat%20de%20Microsoft%C2%A0Copilot/Proyecto_1.2.py)

***

## **1. `AgregarTarea()`**

Permite añadir una tarea asegurando que:

*   No exista otra con la misma descripción
*   Prioridad sea válida (baja/media/alta)
*   Día de la semana sea correcto
*   Día del mes esté entre 1–31
*   El mes esté entre 1–12

Y luego crea un diccionario como:

```python
{
 "descripción": desc,
 "prioridad": prior,
 "completada": False,
 "día_semana": dia_semana,
 "día_mes": dia_mes,
 "mes": mes_num
}
```

***

## **2. `CompletarTarea()`**

Muestra solo tareas pendientes y permite marcarlas como completadas.

Actualiza el estado y reorganiza las listas internas.

***

## **3. `EliminarTarea()`**

Permite eliminar la tarea que elijas mediante su número.  
Incluye validaciones para evitar errores al introducir índices.

***

## **4. `ListarTareas()`**

Puede listar:

*   Solo pendientes
*   Solo completadas
*   Todas

Con formato:

    • [✓] Comprar pan – Prioridad: alta – Día miércoles 27 (Mes 10)

***

## **5. `Update()`**

Actualiza automáticamente:

*   `misTareasPendientes`
*   `misTareasCompletadas`

Es clave para que el gestor siempre esté sincronizado.

***

## **6. `MostrarEstadisticas()`**

Genera estadísticas como:

*   Total de tareas
*   Completadas
*   Pendientes
*   Cantas hay por prioridad (alta, media, baja)
*   Y cuántas de cada una se han completado

Ejemplo del cálculo interno: 

```python
if tarea["prioridad"] == "alta":
    if not tarea["completada"]:
        tareasPenPriorAlta += 1
    else:
        tareasComplPriorAlta += 1
```

***

## **7. `MostrarGraficos()`**

Genera **dos gráficos** con matplotlib:

### Gráfico 1 – Completadas vs. Pendientes (por prioridad)

*   Barras verdes → completadas
*   Barras azules → pendientes

### Gráfico 2 – Tareas completadas por día del mes

Pide un mes al usuario y genera un gráfico mensual.

***

# **Cómo ejecutar el programa**

1.  Abre una terminal en la carpeta del archivo.
2.  Ejecuta:

```bash
python Proyecto_1.2.py
```

3.  Usa el menú para navegar por todas las funciones.

***

# **Cómo trabajé este proyecto**

Decidí:

### Separar cada acción en una función

Para evitar confusiones y hacer el código más claro.

### Usar diccionarios para representar tareas

Porque permite guardar muchos atributos y acceder a ellos fácilmente.

### Crear tres listas sincronizadas mediante `Update()`

*   `misTareas` → todas
*   `misTareasPendientes` → solo las nuevas
*   `misTareasCompletadas` → las finalizadas

### Dividir el programa en fases

1.  Entrada y validación
2.  Gestión
3.  Estadísticas
4.  Gráficos

### Mantener la interacción simple

Todo se gestiona con teclado y mensajes claros.

***

#  **Dificultades que tuve**

### Validación de datos

Hubo que revisar:

*   Entradas numéricas
*   Días válidos
*   Meses
*   Descripciones duplicadas

### Gráficos

Integrar matplotlib con datos dinámicos fue un reto, sobre todo al calcular cuántas tareas se completaban por día.

### Sincronizar listas

Si no se actualizan correctamente, las tareas pueden “desaparecer” o duplicarse.

Esto lo resolví con la función `Update()`.

 **Conclusión**

Este proyecto me ayudó a mejorar en:

*   Organización del código
*   Manejo de estructuras de datos
*   Validación y control de errores
*   Lógica de estados
*   Estadísticas básicas
*   Generación de gráficos
*   Flujo interactivo por consola

Es uno de mis proyectos mejor estructurados y más completos dentro de la programación básica.
