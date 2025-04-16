# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range(101):
    print(i)

print("\n" + "-"*40 + "\n")
# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

# Para este ejercicio, se utilizará la función input() para solicitar un número al usuario y luego se
# convertirá a entero. Luego, se utilizará un bucle while para contar la cantidad de dígitos.
# Finalmente, se imprimirá el resultado en pantalla.

numero = int(input("Ingrese un número entero: "))
contador = 0

while numero > 0:
    numero //= 10
    contador += 1

print(f"El número tiene {contador} dígitos.")

print("\n" + "-"*40 + "\n")

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

# Para este ejercicio, se utilizará la función input() para solicitar dos números al usuario y luego
# se utilizará un bucle for para sumar todos los números entre esos dos valores. Finalmente, se
# imprimirá el resultado en pantalla.

valor1 = int(input("Ingrese el primer valor: "))
valor2 = int(input("Ingrese el segundo valor: "))

suma = 0

if valor1 < valor2:
    for i in range(valor1 + 1, valor2):
        suma += i
else:
    for i in range(valor2 + 1, valor1):
        suma += i

print(f"La suma de los números entre {valor1} y {valor2} es: {suma}")


print("\n" + "-"*40 + "\n")

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

# Para este ejercicio, se utilizará la función input() para solicitar números al usuario y luego se
# utilizará un bucle while para sumar los números ingresados. El programa se detendrá cuando el
# usuario ingrese un 0. Finalmente, se imprimirá el total acumulado en pantalla.

suma = 0
numero = int(input("Ingrese un número entero (0 para salir): "))

while numero != 0:
    suma += numero
    numero = int(input("Ingrese otro número entero (0 para salir): "))

print(f"El total acumulado es: {suma}")

print("\n" + "-"*40 + "\n")

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

# Para este ejercicio, se utilizará la función random para generar un número aleatorio y luego se
# utilizará un bucle while para permitir al usuario adivinar el número. Se contará la cantidad de
# intentos y se imprimirá el resultado al final.

import random

numero_aleatorio = random.randint(0, 9)
intentos = 0
numero_adivinado = -1

while numero_adivinado != numero_aleatorio:
    numero_adivinado = int(input("Adivina el número entre 0 y 9: "))
    intentos += 1

print(f"¡Felicidades! Adivinaste el número {numero_aleatorio} en {intentos} intentos.")

print("\n" + "-"*40 + "\n")

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.
# # (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

# # Para este ejercicio, se utilizará un bucle for para iterar sobre los números pares entre 0 y 100
# # en orden decreciente. Se utilizará la función range() con un paso de -2 para lograr esto.
# # Finalmente, se imprimirá cada número en pantalla.


for i in range(100, -1, -2):
    print(i)

print("\n" + "-"*40 + "\n")

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

# # Para este ejercicio, se utilizará la función input() para solicitar un número al usuario y luego
# # se utilizará un bucle for para sumar todos los números entre 0 y ese número. Finalmente, se
# # imprimirá el resultado en pantalla.

numero = int(input("Ingrese un número entero positivo: "))
suma = 0
for i in range(numero + 1):
    suma += i

print(f"La suma de los números entre 0 y {numero} es: {suma}")

print("\n" + "-"*40 + "\n")

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

# # Para este ejercicio, se utilizará un bucle for para permitir al usuario ingresar 100 números
# # enteros. Se utilizarán contadores para llevar un registro de la cantidad de números pares,
# # impares, negativos y positivos. Finalmente, se imprimirán los resultados en pantalla.

numeros = 100  # Cambia este valor para probar con menos números

pares = 0
impares = 0
negativos = 0
positivos = 0

for i in range(numeros):
    numero = int(input(f"Ingrese el número {i + 1}: "))

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    if numero < 0:
        negativos += 1
    elif numero > 0:
        positivos += 1

print(f"\nCantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")
print(f"Cantidad de números negativos: {negativos}")
print(f"Cantidad de números positivos: {positivos}")

print("\n" + "-"*40 + "\n")

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

# # Para este ejercicio, se utilizará un bucle for para permitir al usuario ingresar 100 números
# # enteros. Se utilizará una variable acumuladora para sumar los números y luego se calculará la
# media dividiendo la suma entre la cantidad de números ingresados. Finalmente, se imprimirá el
# resultado en pantalla.

numeros = 100  # Cambia este valor para probar con menos números
suma = 0

for i in range(numeros):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    suma += numero

media = suma / numeros
print(f"La media de los números ingresados es: {media}")

print("\n" + "-"*40 + "\n")

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

# # Para este ejercicio, se utilizará la función input() para solicitar un número al usuario y luego
# se convertirá a cadena para invertir el orden de los dígitos. Finalmente, se imprimirá el
# resultado en pantalla.


numero = input("Ingrese un número: ")
numero_invertido = numero[::-1]  # Invertir la cadena

print(f"El número invertido es: {numero_invertido}")

print("\n" + "-"*40 + "\n")
