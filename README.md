# 🏨 Sistema de Gestión de Habitaciones - Hotel Estelar

Programa en Python con menú interactivo que gestiona la disponibilidad de habitaciones de un hotel, permitiendo realizar check-in, check-out, y consultar el estado de ocupación en tiempo real.

## 🧩 Situación inicial

El Hotel Estelar necesita una herramienta de consola para que su personal de recepción pueda gestionar la disponibilidad de sus 50 habitaciones durante el día: registrar el ingreso de huéspedes (check-in), liberar habitaciones al finalizar una estadía (check-out), y consultar en cualquier momento cuántas habitaciones están disponibles u ocupadas.

## 🚀 Funcionalidades implementadas

- **Menú interactivo persistente**: permite realizar múltiples operaciones en la misma sesión, volviendo al menú principal después de cada acción hasta que el usuario elige salir.
- **Consulta de disponibilidad**: muestra en cualquier momento cuántas habitaciones están disponibles.
- **Check-in validado**: permite reservar una cantidad de habitaciones, validando que no se exceda la disponibilidad actual.
- **Check-out validado**: permite liberar habitaciones, validando que no se libere una cantidad mayor a la que efectivamente está ocupada.
- **Historial de ocupaciones**: muestra el total de habitaciones actualmente ocupadas.

## 🛠️ Tecnologías utilizadas

- Python 3 (módulos `os` y `time`)

## 📂 Estructura del proyecto

Sistema-de-gestion-de-habitaciones/
└── hotel_estelar.py # Lógica completa: menú interactivo, validación de check-in/check-out

## ▶️ Cómo ejecutarlo

1. Clona este repositorio o descarga el archivo.
2. Ejecuta el script:
```bash
   python hotel_estelar.py
```
3. Elige una opción del menú (1 a 5) para consultar disponibilidad, hacer check-in, check-out, ver el historial de ocupaciones, o salir.

## 🧠 Decisiones de diseño

- **Validación de check-out contra habitaciones realmente ocupadas**: se corrigió la validación para que el límite de habitaciones a liberar sea la cantidad efectivamente ocupada (`historial`), y no la capacidad máxima del hotel, evitando que el sistema termine con más habitaciones disponibles que las que existen en total.
- **Menú dentro de un ciclo `while True`**: se estructuró todo el procesamiento de opciones dentro del mismo ciclo que muestra el menú, permitiendo realizar múltiples operaciones (check-in, check-out, consultas) en una sola ejecución del programa.
- **Patrón de validación con bandera booleana (`dato_valido`)**: tanto el check-in como el check-out utilizan este patrón para asegurar que el dato ingresado sea numérico y esté dentro del rango permitido antes de continuar, volviendo a solicitarlo en caso contrario.
- **Pausas con `time.sleep()`**: se agregaron pausas antes de limpiar la pantalla, para que el usuario pueda leer el resultado de cada operación antes de volver al menú.

## 👤 Autora

Abigail Betsabé Arriagada Aravena — Proyecto realizado durante la formación en Python de la asignatura Fundamentos de la programación (Duoc UC).
