# Ejercicio 1
print("¡Hola Mundo!")

# Ejercicio 2
Saludos = "¡Hola Mundo!"
print(Saludos)

# Ejercicio 3
Ask_name = input("Cual es tu nombre? ")
print(f"¡Hola {Ask_name}!")
print("¡Hola " + Ask_name + "!")

# Ejercicio 4
Operacion = ((3 + 2) / (2 * 5)) ** 2
print(Operacion)
print(((3 + 2) / (2 * 5)) ** 2)

# Ejercicio 5

Ask_num = float(input("Horas trabajadas: "))
Ask_hour = float(input("Coste por hora: "))
print(f"Tiene una paga correspondiente de {Ask_hour * Ask_num} €/Euros")
"""
horas = float(input("Introduce horas de trabajo: "))
coste = float(input("Introduce lo que cobras por hora: "))
paga = horas * coste
print("tu paga es", paga)
"""

# Ejercicio 6
num_positiu = int(input("Introduce un numero positivo: "))
suma = ((num_positiu * (num_positiu + 1)) / 2)
print("La suma de numeros enteros positivos es", suma)

# n = int(input("Introduce un número entero: "))
# suma = n * (n + 1) / 2
# print("La suma de los primeros números enteros desde 1 hasta " + str(n) + " es " + str(suma))

# Ejercicio 7
"""
peso = float(input("Introduce su peso: "))
estatura = float(input("Introduce su estatura: "))
imc = peso / (estatura * estatura)
print("Tu índice de masa corporal es ", imc.__round__(2))
"""
peso = input("¿Cuál es tu peso en kg? ")
estatura = input("¿Cuál es tu estatura en metros?")
imc = round(float(peso)/float(estatura)**2,2)
print("Tu índice de masa corporal es " + str(imc))

# Ejercicio 8
"""
n = int(input("Introduce un número entero: "))
m = int(input("Introduce un otro número entero: "))
c = round((float(n) / float(m)), 5)
r = n - (c * m)
print(str(n) + " entre " + str(m) + " da un cociente " + str(c) + " y un resto " + str(r))
"""
n = input("Introduce el dividendo (entero): ")
m = input("Introduce el divisor (entero): ")
print(n + " entre " +  m + " da un cociente " + str(int(n) // int(m)) + " y un resto " + str(int(n) % int(m)))

# Ejercicio 9
cantidad_invertida = float(input("¿En que cantidad quiere invertir? "))
tasa_interes = float(input("¿Cual es el su interes anual? "))
numero_anios = float(input("¿En que numero de años? "))
capital = cantidad_invertida * (1 + (tasa_interes / 100)) ** numero_anios
print("El capital obtenido al final del periodo de inversión es de " + "{:.2f}".format((capital)) + " €/Euros.")
"""
cantidad = float(input("¿Cantidad a invertir? "))
interes = float(input("¿Interés porcentual anual? "))
años = int(input("¿Años?"))
print("Capital final: " + str(round(cantidad * (interes / 100 + 1) ** años, 2)))
"""

# Ejercicio 10
"""
clown = int(input("Ingrese la Cantidad de Payasos Vendidos: "))
doll = int(input("Ingrese la Cantidad de Muñecas Vendidas: "))

clown *= 112
doll *= 75

print("El peso total del paquete es de", clown + doll, "gramos")
"""

peso_payaso = 112
peso_muneca = 75
payasos = int(input("Introduce el número de payasos a enviar: "))
munecas = int(input("Introduce el número de muñecas a enviar: "))
peso_total = peso_payaso * payasos + peso_muneca * munecas
print("El peso total del paquete es " + str(peso_total))

# Ejercicio 11

cantidad_dipositada = int(input("Introduce la cantidad de ahorros: "))
ahorros1 =
ahorros2 =
ahorros3 =

cantidad_final = print(f"El resultado de la operacion es {ahorros1}")