#Programa_"OSO" o "SOS"

n1 = input("Nom del jugador 1: ")
n2 = input("Nom del jugador 2: ")
taulell = [[".",".",".","."],[".",".",".","."],[".",".",".","."],[".",".",".","."]]

def DibuixTaulell():
	print ("\n")
	for l in taulell:
		print(l[0] + " " + l[1]+ " " + l[2]+ " " + l[3])
	print ("\n")

def main():
	jugador = 1
	intents = 0
	fitxa = ""
	while intents < 16 and not fitxa == "X":
		DibuixTaulell()
		if jugador == 1:
			print("Li toca jugar a " + n1)
		else:
			print("Li toca jugar a " + n2)
		h = input ("Alçada, horitzontal i lletra (x per abandonar)")
		fitxa = h[0]
		fitxa = fitxa.upper()
		if fitxa == "X":
			break
		x = h[1]
		y = h[2]

		x2 = int(x)-1
		y2 = int(y)-1
		if (x2 < 0 or x2 > 3 or y2 < 0 or y2 > 3):
			print("Posició errònia")
		else:
			if not taulell[x2][y2] == ".":
				print ("Casella ocupada")
			else:
				taulell[x2][y2] = fitxa
			if jugador == 1:
				jugador = 2
			else:
				jugador = 1
			intents = intents + 1

main()
