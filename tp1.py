import math
# Ejercicio 1
print("Hola, mundo!")
# Ejercicio 2
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")
# Ejercicio 3
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre}, tengo {edad} años y vivo en {residencia}")
# Ejercicio 4
radio = float(input("¿Cuánto mide el radio del círculo? "))
area = math.pi * radio ** 2
perimetro = 2 * math.pi * radio
print(f"El área del círculo mide {area} y su perímetro mide {perimetro}")
# Ejercicio 5
segundos = int(input("Ingrese una cantidad de segundos: "))
hora = segundos / 3600
print(f"{segundos} segundos equivalen a {hora} horas")
# Ejercicio 6
numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
# Ejercicio 7
num1 = int(input("Ingrese el primer número, distinto de cero: "))
num2 = int(input("Ingrese un segundo número, distitnto de cero: "))
print(f"Suma: {num1 + num2}")
print(f"Resta: {num1 - num2}")
print(f"Multiplicación: {num1 * num2}")
print(f"División: {num1 / num2}")
# Ejercicio 8
altura = float(input("Ingrese su altura (en metros): "))
peso = float(input("Ingrese su peso (en kg.): "))
imc = peso / (altura ** 2)
print(f"Su índice de masa corporal es {imc}")
# Ejercicio 9
celsius = int(input("Ingrese temperatura en grados Celsius: "))
fahrenheit = (9 / 5) * celsius + 32
print(f"{celsius}° equivalen a {fahrenheit}°F")
# Ejercicio 10
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese un segundo número: "))
num3 = float(input("Ingrese un tercer número: "))
prom = (num1 + num2 + num3) / 3
print(f"El promedio de los números es {prom}")