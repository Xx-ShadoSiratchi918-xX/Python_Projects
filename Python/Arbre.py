#Programa_Arbre

alc = input("digas la alçada del arbre")
estrelles = 1
punts = int(alc) - 2
nivell = 1

while nivell <= int(alc)-2:
	print ('.'*punts + '*'* estrelles + '.'* punts)

	nivell = nivell + 1
	estrelles = estrelles + 2
	punts = punts - 1

print ("." * (int(alc) -1) + "|||" + "." * (int(alc) -1))
