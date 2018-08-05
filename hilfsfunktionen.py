print('Importiere: Modul hilfsfunktionen als hlf')

	# def printGitter1(self):
	# print('Methode Gitter.printGitter aufgerufen')
	# myNodes = len(self.seq_Wand_0)
	# zaehler = 0
	# while(zaehler<myNodes):
	# 	# Druckt Koordinaten des Knoten aus
	# 	print('{} {} {}'.format(self.seq_Wand_0[zaehler], Wandknoten.xk, Wandknoten.yk) )
	# 	zaehler = zaehler+1

def printGitter2(Gitter):
	anzahlElemente = len(Gitter.seq_Wand_0)
	for iterator in range(0, anzahlElemente):
		print( Gitter.seq_Wand_0[iterator].get_koordinaten() )