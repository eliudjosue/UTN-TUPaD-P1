# 1. Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.

#Funciones
def imprimir_hola_mundo(mensaje):
    print(f"Hola {mensaje}!")

# Programa principal

imprimir_hola_mundo("Mundo")

print("\n" + "-"*40 + "\n")
# 2. Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.

def saludar_usuario(nombre):
    return imprimir_hola_mundo(nombre)

# Programa prinsipal
saludar_usuario("Marcos")

print("\n" + "-"*40 + "\n")
# 3. Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

#Función para imprimir información personal
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

def pedir_datos():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    edad = input("Ingrese su edad: ")
    residencia = input("Ingrese su lugar de residencia: ")
    return nombre, apellido, edad, residencia

# Programa principal
datos = pedir_datos()
informacion_personal(*datos)

print("\n" + "-"*40 + "\n")
# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

# Funciones
import math

def calcular_area_circulo(radio):
    return math.pi * (radio ** 2)

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

def pedir_numero(mensaje):
    while True:
        try:
            numero = float(input(mensaje))
            if numero < 0:
                raise ValueError("El número no puede ser negativo.")
            return numero
        except ValueError as e:
            print(f"Entrada inválida: {e}. Intente nuevamente.")

# Programa principal
radio = pedir_numero("Ingrese el radio del círculo: ")
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)
print(f"El área del círculo es: {area:.2f}")
print(f"El perímetro del círculo es: {perimetro:.2f}")

print("\n" + "-"*40 + "\n")
# 5. Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

# Función
def segundos_a_horas(segundos):
    horas = segundos // 3600
    return horas

# Programa principal
segundos = pedir_numero("Ingrese la cantidad de segundos: ")
horas = segundos_a_horas(int(segundos))
print(f"La cantidad de horas correspondientes es: {horas} horas")

print("\n" + "-"*40 + "\n")
# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.

def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
# Programa principal
numero = pedir_numero("Ingrese un número para ver su tabla de multiplicar: ")
tabla_multiplicar(int(numero))

print("\n" + "-"*40 + "\n")
# 7. Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = None
    if b != 0:
        division = a / b
    else:
        division = "Error: División por cero"
    
    return (suma, resta, multiplicacion, division)
# Programa principal
a = pedir_numero("Ingrese el primer número: ")
b = pedir_numero("Ingrese el segundo número: ")
resultados = operaciones_basicas(int(a), int(b))
print(f"Resultados:\nSuma: {resultados[0]}\nResta: {resultados[1]}\nMultiplicación: {resultados[2]}\nDivisión: {resultados[3]}")


print("\n" + "-"*40 + "\n")
# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

def calcular_imc(peso, altura):
    if altura <= 0:
        return "Error: La altura debe ser mayor que cero."
    imc = peso / (altura ** 2)
    return round(imc, 2)
# Programa principal
peso = pedir_numero("Ingrese su peso en kilogramos: ")
altura = pedir_numero("Ingrese su altura en metros: ")
imc = calcular_imc(peso, altura)

if isinstance(imc, str):
    print(imc)
else:
    print(f"Su índice de masa corporal (IMC) es: {imc:.2f}")
    
print("\n" + "-"*40 + "\n")
# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.

def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return round(fahrenheit, 2)
# Programa principal
celsius = pedir_numero("Ingrese la temperatura en grados Celsius: ")
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"La temperatura en grados Fahrenheit es: {fahrenheit:.2f}°F")

print("\n" + "-"*40 + "\n")
# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

# Programa principal
a = pedir_numero("Ingrese el primer número: ")
b = pedir_numero("Ingrese el segundo número: ")
c = pedir_numero("Ingrese el tercer número: ")
promedio = calcular_promedio(a, b, c)
print(f"El promedio de los números es: {promedio:.2f}")
