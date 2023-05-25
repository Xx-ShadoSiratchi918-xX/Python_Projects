import random
from random import choice
print ("vamos a jugar a piedra, papel a tijera.")
def mi_partida():
	puntuaciones = 0
	Opciones = ['Piedra','Papel','Tijera']
	Maquina = (choice((Opciones)))
	Eleccion = input("seleccione Piedra, Papel a Tijera:" )
	if Eleccion not in Opciones:
		print ("seleccione una opcion valida")
	if Eleccion == Maquina:
		puntuaciones = 0
		print ("Empate")
	if (Eleccion == 'Piedra'):
		if (Maquina == 'Papel'):
			puntuaciones = 2
			print("Perdiste")
		elif (Maquina == 'Tijera'):
			puntuaciones = 1
			print("ganaste")
	if (Eleccion == 'Papel'):
		if (Maquina == 'Tijera'):
			puntuaciones = 2
			print("Perdiste")
		elif (Maquina == 'Piedra'):
			puntuaciones = 1
			print("Ganaste")
	if (Eleccion == 'Tijera'):
		if (Maquina == 'Piedra'):
			puntuaciones = 2
			print( "perdiste")
		elif (Maquina == 'Papel'):
			puntuaciones = 1
			print("ganaste")
	return puntuaciones
def main():
	pJug = 0
	pMaq = 0
	n = False
	while n==False:
		puntuacione = mi_partida()
		if puntuacione == 1:
			pJug += 1
		elif puntuacione == 2:
			pMaq += 1
		print ("Puntuaciones: Ordenador ->", pMaq, "jugador ->", pJug)
		respuesta=input("Quieres seguir jugando?: y/n:" )
		if(respuesta =="n"):
			print("Juego finalizado")
			n = True
main()
