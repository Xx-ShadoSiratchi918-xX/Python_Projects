"""
Este es un programa que simula un chat con emojis en la consola y lo muestra en la pantalla
"""

seguirChateando = True

while seguirChateando:
    texto = input("> ")
    if texto == "Adios":
        print("¡¡Nos vemos pronto!! ☺️")
        seguirChateando = False
    texto = texto.replace(":)", "🙂")
    texto = texto.replace(":(", "😟")
    texto = texto.replace(":P", "😛")
    texto = texto.replace("XP", "😝")
    texto = texto.replace("9P", "😜")
    texto = texto.replace("B)", "😎")
    texto = texto.replace("<(", "😞")
    texto = texto.replace("0u< ", "😉")
    texto = texto.replace("=D", "😃")
    texto = texto.replace(":D", "😀")
    texto = texto.replace("X'D", "😂")
    texto = texto.replace(":C", "☹️")
    texto = texto.replace("XD", "😆")
    texto = texto.replace("<//)", "☺️")
    texto = texto.replace("(:", "🙃")
    texto = texto.replace("·3·", "😗")
    texto = texto.replace("^3^", "😙")
    texto = texto.replace("X(", "😣")
    texto = texto.replace("XE", "😖")
    texto = texto.replace("DX", "😫")
    texto = texto.replace("D>", "😩")
    texto = texto.replace("<:'(", "😢")
    texto = texto.replace("<''o", "😭")
    texto = texto.replace("=o", "😮")
    texto = texto.replace(">:(", "😠")
    texto = texto.replace(">:#(", "😡")
    texto = texto.replace("'-_-", "😓")
    texto = texto.replace(": ", "😶")
    texto = texto.replace(":|", "😐")
    texto = texto.replace("-_-", "😑")
    texto = texto.replace("<:o", "😯")
    texto = texto.replace("8O", "😲")
    texto = texto.replace("<:S", "🥴")
    print(texto)