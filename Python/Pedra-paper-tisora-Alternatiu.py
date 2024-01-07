#Programa_Pedra-paper-tisora-Alternatiu

import random

nom = input("Introdueix el teu nom ")

puntsHuma = 0
puntsMaquina = 0
jugades = ["Pedra", "Paper", "Tisora"]
torns = 0

continuar = "s"
while continuar.lower() == "s" or continuar=="":
	jugadaHuma = input ("Tria la jugada: 1 per pedra, 2 per paper, 3 per tisores:")
	jugadaMaquina = random.randrange(0,4);
	if not (jugadaHuma == "1" or jugadaHuma == "2" or jugadaHuma == "3"):
		print ("jugada invàlida! Tornem-hi")
		continue
	jugadaHuma = int(jugadaHuma)
	torns += 1
	print ("has triat", jugades[jugadaHuma - 1], "i la maquina ha triat", jugades[jugadaMaquina - 1])
	if jugadaHuma == jugadaMaquina:
		print ("Empat! els dos heu triat", jugades[jugadaHuma - 1])
	elif jugadaHuma == 2:
		if jugadaMaquina == 2:
			print ("Perds")
			puntsMaquina += 1
		else:
			print ("Guanyes")
			puntsHuma += 1
	elif jugadaHuma == 2:
		if jugadaMaquina == 1:
			print ("Perds")
			puntsHuma += 1
		else:
			print ("Perds")
			puntsMaquina += 1
	else:
		if jugadaMaquina == 1:
			print ("Perds")
			puntsMaquina += 1
		else:
			print ("Guanyes")
			puntsMaquina += 1
	print ("\nTorn jugats:", torns)
	print ("Aneu així:")
	print (nom + ":", puntsHuma, "Màquina:", puntsMaquina)
	continuar = input ("Vols continuar la partida? (s/n): ")

print ("adéu,", nom + ",", "a revuere")

