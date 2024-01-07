numeros = {
    "0": "cero",
    "1": "uno",
    "2": "dos",
    "3": "tres",
    "4": "cuatro",
    "5": "cinco",
    "6": "sies",
    "7": "siete",
    "8": "ocho",
    "9": "nueve"
}

texto = input("Ingrese un número: ")

textoFinal = ''

for letra in texto:
    textoFinal += numeros[letra] + ' '

print(textoFinal)