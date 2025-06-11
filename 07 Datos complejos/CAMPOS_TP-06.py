# 1) Dado el diccionario precios_frutas precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450} Añadir las siguientes frutas con sus respectivos precios:
# ● Naranja = 1200
# ● Manzana = 1500
# ● Pera = 2300

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print("\n" + "-"*40 + "\n")

# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# ● Banana = 1330
# ● Manzana = 1700

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700

print("\n" + "-"*40 + "\n")


# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios.

frutas = list(precios_frutas.keys())
print("Lista de frutas:", frutas)

print("\n" + "-"*40 + "\n")

# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe. Ejemplo:

# contactos = {"Juan": "123456", "Ana": "987654"}
# #Consultar: "Juan" -> muestra "123456" 

contactos = {}
def cargar_contactos():
    for _ in range(5):
        nombre = input("Ingrese el nombre del contacto: ")
        numero = input("Ingrese el número de teléfono: ")
        contactos[nombre] = numero

def consultar_contacto(nombre):
    return contactos.get(nombre, "Contacto no encontrado")

# Programa principal
cargar_contactos()
nombre_consulta = input("Ingrese el nombre del contacto a consultar: ")
print(consultar_contacto(nombre_consulta))


print("\n" + "-"*40 + "\n")

# 5) Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra. Ejemplo:

#Entrada: "Hola mundo Hola"

## Salida:
# Palabras únicas: {'Hola', 'mundo'}
# Recuento: { "hola": 2, "mundo": 1 }

def procesar_frase(frase):
    palabras = frase.lower().split()
    palabras_unicas = set(palabras)
    recuento_palabras = {palabra: palabras.count(palabra) for palabra in palabras_unicas}
    
    return palabras_unicas, recuento_palabras

# Programa principal

frase = input("Ingrese una frase: ")

palabras_unicas, recuento_palabras = procesar_frase(frase)

print("Palabras únicas:", palabras_unicas)
print("Recuento:", recuento_palabras)

print("\n" + "-"*40 + "\n")

# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. Luego, mostrá el promedio de cada alumno. Ejemplo:

# alumnos = {
#     "Sofia": (10, 9, 8),
#     "Luis": (6, 7, 7)
# }

alumnos = {}
def cargar_alumnos():
    for _ in range(3):
        nombre = input("Ingrese el nombre del alumno: ")
        notas = tuple(float(input(f"Ingrese la nota {i+1} de {nombre}: ")) for i in range(3))
        alumnos[nombre] = notas
def calcular_promedio(notas):
    return sum(notas) / len(notas)

# Programa principal
cargar_alumnos()
for nombre, notas in alumnos.items():
    promedio = calcular_promedio(notas)
    print(f"El promedio de {nombre} es: {promedio:.2f}")

print("\n" + "-"*40 + "\n")

# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

parcial_1 = {"Sofia", "Luis"}
parcial_2 = {"Sofia", "Juan"}

# Aprobaron ambos parciales
aprobados_ambos = parcial_1.intersection(parcial_2)
print("Aprobados ambos parciales:", aprobados_ambos)

# Aprobaron solo uno de los dos
aprobados_solo_uno = parcial_1.symmetric_difference(parcial_2)
print("Aprobados solo uno de los dos:", aprobados_solo_uno)

# Total de estudiantes que aprobaron al menos un parcial
aprobados_totales = parcial_1.union(parcial_2)
print("Total aprobados:", aprobados_totales)

print("\n" + "-"*40 + "\n")

# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.

stock_productos = {}

def consultar_stock(producto):
    return stock_productos.get(producto, 0)

def agregar_stock(producto, cantidad):
    if producto in stock_productos:
        stock_productos[producto] += cantidad
    else:
        stock_productos[producto] = cantidad

# Programa principal
while True:
    print("\nOpciones:")
    print("1. Consultar stock")
    print("2. Agregar stock")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        producto = input("Ingrese el nombre del producto: ")
        print(f"Stock de {producto}: {consultar_stock(producto)} unidades")

    elif opcion == "2":
        producto = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad a agregar: "))
        agregar_stock(producto, cantidad)
        print(f"Stock de {producto} actualizado: {consultar_stock(producto)} unidades")

    elif opcion == "3":
        break

    else:
        print("Opción inválida. Intente nuevamente.")


print("\n" + "-"*40 + "\n")

# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos. Ejemplo:

# agenda = {
#     ("lunes", "10:00"): "Reunión", ("martes", "15:00"): "Clase de ingles"
# }

# Permití consultar qué actividad hay en cierto día y hora.

def consultar_evento(dia, hora):
    return agenda.get((dia, hora), "No hay evento programado")

agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "15:00"): "Clase de ingles"
}
# Programa principal
dia = input("Ingrese el día: ")
hora = input("Ingrese la hora (HH:MM): ")
evento = consultar_evento(dia, hora)
print(f"Evento programado para {dia} a las {hora}: {evento}")

print("\n" + "-"*40 + "\n")

# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores. Ejemplo:

# original  = {
#     "Argentina": "Buenos Aires",
#     "Chile": "Santiago"
# }

# invertido = {"Buenos Aires": "Argentina", "Santiago": "Chile"}

original = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago"
}
invertido = {capital: pais for pais, capital in original.items()}
print("Diccionario original:", original)
print("Diccionario invertido:", invertido)
print("\n" + "-"*40 + "\n")