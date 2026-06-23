# 📑 Python Piscine - Module 00: Basics & Garden Basics

Este módulo introduce los conceptos fundamentales de Python enfocado en la sintaxis básica, tipos de datos, estructuras de control, funciones e introducción a las anotaciones de tipo (Type Annotations). Toda la temática gira en torno a la gestión y automatización de un huerto o jardín virtual.

---

## 🛠️ Requisitos Generales
* **Lenguaje:** Python 3.10 o superior.
* **Norma:** El código debe seguir las pautas de estilo de la comunidad (PEP 8).
* **Restricciones:** No se permite el uso de librerías externas a menos que se especifique lo contrario.

---

## 🚀 Ejercicios del Módulo

### 📇 Exercise 0: Hello Garden
* **Objetivo:** Primer contacto con la salida estándar en Python.
* **Conceptos:** Función `print()`, strings y sintaxis inicial.
* **Ficheros:** `hello_garden.py`
* **Descripción:** Escribe un script que muestre por pantalla un mensaje de bienvenida personalizado al jardín de 42.

### 📇 Exercise 1: Garden Name
* **Objetivo:** Manejo de variables y entrada de datos por consola.
* **Conceptos:** Función `input()`, variables de texto y formateo de strings (f-strings).
* **Ficheros:** `garden_name.py`
* **Descripción:** Solicita al usuario el nombre de su jardín y devuelve un saludo dinámico utilizando el nombre introducido.

### 📇 Exercise 2: Garden Plot Area
* **Objetivo:** Operaciones aritméticas y tipos de datos numéricos.
* **Conceptos:** Operadores matemáticos (`+`, `-`, `*`, `/`), tipos `int` y `float`.
* **Ficheros:** `garden_area.py`
* **Descripción:** Calcula el área de una parcela rectangular del jardín pidiendo al usuario el ancho y el largo en metros.

### 📇 Exercise 3: Harvest Total
* **Objetivo:** Manipulación de listas y acumuladores.
* **Conceptos:** Listas (`list`), bucles `for`, indexación y funciones integradas como `sum()`.
* **Ficheros:** `harvest_total.py`
* **Descripción:** Dado un listado con los kilogramos recolectados por planta, calcula y muestra el total de la cosecha acumulada.

### 📇 Exercise 4: Plant Age Check
* **Objetivo:** Estructuras condicionales.
* **Conceptos:** Sentencias `if`, `elif` y `else`.
* **Ficheros:** `plant_check.py`
* **Descripción:** Determina si una planta está lista para ser cosechada basándose en su edad en días introducida por el usuario.

### 📇 Exercise 5: Water Reminder
* **Objetivo:** Control de flujos con bucles condicionales.
* **Conceptos:** Bucle `while`, operadores lógicos y decrementos.
* **Ficheros:** `water_reminder.py`
* **Descripción:** Crea una cuenta atrás de días que faltan para el próximo riego. El script avisa con una alerta en pantalla cuando el contador llega a cero.

### 📇 Exercise 6: Count to Harvest
* **Objetivo:** Generación de secuencias numéricas y rangos.
* **Conceptos:** Función `range()`, bucles aninados y control de iteraciones.
* **Ficheros:** `count_to_harvest.py`
* **Descripción:** Genera un contador visual paso a paso de los días que restan hasta el día exacto de la cosecha masiva.

### 📇 Exercise 7: Seed Inventory with Type Annotations
* **Objetivo:** Uso estricto de tipado y estructuras de datos complejas.
* **Conceptos:** Diccionarios (`dict`), Type Annotations (tipado estático simulado) y la librería estándar `typing`.
* **Ficheros:** `seed_inventory.py`
* **Descripción:** Diseña una función con anotaciones de tipo explícitas que reciba un inventario de semillas (con stock y tipo) y valide que los datos introducidos coinciden con los tipos esperados.

---

## 💻 Cómo ejecutar los scripts

Puedes probar cada uno de los ejercicios ejecutando el intérprete de Python desde la terminal:

```bash
python3 hello_garden.py
python3 garden_name.py
python3 seed_inventory.py
```

---

## ⚖️ Descargo de Responsabilidad (Disclaimer)

Este repositorio ha sido creado con fines puramente académicos y como parte de mi proceso de aprendizaje en el plan de estudios de **42**.

* **Uso bajo tu propio riesgo:** No me hago responsable del uso que se le dé al código de este repositorio, ni de las consecuencias derivadas de su copia, modificación o reutilización en tus propias entregas.
* **Política de copia de 42 (Plagio):** Se recuerda a los estudiantes de 42 que el plagio o la copia directa de código sin comprender su funcionamiento infringe las normas de la escuela y puede ser penalizado de forma severa por los sistemas de evaluación automática o manual (*Moulinette* / Evaluadores).
* **Propósito:** El código se comparte con el único objetivo de servir como referencia, consulta técnica o inspiración para resolver arquitecturas de Makefiles complejos y automatización de tests interactivos.
