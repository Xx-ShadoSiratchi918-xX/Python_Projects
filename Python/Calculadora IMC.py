"""
Este programa calcula el indice de masa corporal del usuario y despues lo muestra en pantalla
"""
def calcularIMC(peso, alturaEnMetros):
    imc = round(peso / (alturaEnMetros * alturaEnMetros), 2)
    return imc

def pedirElIMC():
    try:

        peso = float(input("¿Cual es su peso en kg? "))
        alturaEnCM = int(input("¿Cual es su altura en cm? "))

        alturaEnMetros = alturaEnCM / 100
        imc = calcularIMC(peso, alturaEnMetros)

        # print("Su indice de masa corporal es de" + str(imc) + "IMC")
        print(f"Su indice de masa corporal es de {str(imc)} IMC")

        if imc < 20:
            print("Usted se encuentra en un estado de Delgadez")
        if imc >= 20 and imc < 26:
            print("Usted se encuentra en un estado Normal")
        if imc >= 26 and imc < 30:
            print("Usted se encuentra en un estado de Sobrepeso")
        if imc >= 30:
            print("Usted se encuentra en un estado de Obesidad")

    except:
        print("Ha introducido un valor o lo ha escrito erroneamente, porfavor intenaló de nuevo")

print("Porfavor, Introduce los valores de tres personas para calcular sus IMCs")
print("Ingrese el valor de la primera persona")
pedirElIMC()
print("Ingrese el valor de la segunda persona")
pedirElIMC()
print("Ingrese el valor de la tercera persona")
pedirElIMC()