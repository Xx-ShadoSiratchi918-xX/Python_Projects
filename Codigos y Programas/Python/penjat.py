#Programa_Joc-del-penjat

#! /usr/bin/python3 -*- coding: utf-8-*- Joc del penjat, tot i que noff
# Limita els intents
paraula = input("Escriu la paraula a endevinar: ")
print ("la paraula és " + paraula)
input("prem enter per netejar la pantalla i que vingui l'‘altra persona")

#Netegem la pantalla:
for i in range (1, 50):
        print ("\n")

descoberta = "_"*len(paraula)
intents = 0
while descoberta != paraula:
        print ("Fins ara has descobert:", descoberta)
        print ("Intents: ", intents)
        lletra = input ("Introdueix la Lletra: ")
        #siempre suma, da igual
        intents += 1

        trobolletra = "S"
        x = 0
        trobada = False
        while trobolletra == "S":
                posicioTrobada = paraula.find(lletra, x)
                if posicioTrobada < 0:
                        trobolletra = "N"
                        if trobada == False:
                                print ("Lletra no trobada")
                else:
                        descoberta = descoberta[:posicioTrobada] + lletra + descoberta[posicioTrobada + 1 :]
                        x = posicioTrobada+1
                        trobada = True

print ("Felicitats! has trobat la paraula", paraula, "en", intents, "intents!")
