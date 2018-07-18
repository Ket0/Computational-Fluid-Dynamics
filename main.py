## 
## 
## // Portierung eines Gitter-Boltzmann-Lösers von C++ nach Python \\
##
## Version: v0.1
##
## Author : Stefan Eickholz 
## Datum:   11.06.2018
## Ort:     01010000 01101111 01110100 01110011 01100100 01100001 01101101  

#   dBBBBBb     dBBBBP  dBBBBBBP  .dBBBBP     dBBBBb  dBBBBBb     dBBBBBBb
#       dB'    dBP.BP             BP             dBP       BB          dBP
#   dBBBP'    dBP.BP     dBP      `BBBBb    dBP dBP    dBP BB   dBPdBPdBP 
#  dBP       dBP.BP     dBP          dBP   dBP dBP    dBP  BB  dBPdBPdBP  
# dBP       dBBBBP     dBP      dBBBBP'   dBBBBBP    dBBBBBBB dBPdBPdBP   

## Sprache: Python
## Version: 3.6.1
#
# ~~~ πάντα ῥεῖ ~~~
#
## In den folgend gezeigten Programmanweisungen wird ein bestehender CFD Löser für ein zweidimensionales
## Stroemungsgebiet, geschrieben in der Sprache C++, auf Python portiert.
##  
## 
print('\nProgrammstart\n') 

import time
import numpy as np

# from node import *
import node as nd
# import grid
# from grid import *
import grid as gd

class Eingabe(object):
	def __init__(self):
		self.machZahl = 0.1
		self.charL = 0.1
		self.vx = 0.00730365
		self.vy = 0
		self.dichte = 1.225
		self.dynamischZa = 1.7894e-05
		# Gitter
		self.dX = 2.5
		self.dY = 0.41 
		self.abstand = 0.015
		# Initialisierungsdaten
		self.initVX =0.00730365
		self.initVY = 0

"""
# Druck muss berechnet werden
cs_ = sqrt(u0x*u0y + u0y*u0y) / machZahl
initialisierungsDruck = cs*cs*rho
# Weiterhin berechnet wird
xi = 
Zeitschritt = 
omega = 
"""

def main():
	print('# # # Pre-Processing / / / \n')
	# Erzeuge Eingabe-Objekt
	#
	#
	oE = Eingabe()

	# Erzeuge Ausgabe-Objekt
	# Erzeuge Zeit-Objekt
	# Erzeuge Ausgabe-Objekt

	# abstand = 0.015
	# dX = 2.5
	# dY = 0.41
	abstand = 1
	dX = 10
	dY= 5

	# Erzeuge Gitter-Objekt
	#
	# (Eingabe, par_abstand, par_xK, par_yK):
	# mN = grid.Gitter(Eingabe_obj, Eingabe_obj.abstand, Eingabe_obj.dX, Eingabe_obj.dY)
	mN = gd.UniformesGitter(par_xK=dX, par_yK=dY)

	#  - grid.generiereGitter()
	mN.erzeugeGitter_v1()
	# check_anzahl_knoten = mN.getKnotenZahl()
	# print(check_anzahl_knoten) # gibt 10 aus, check

	# for i in range(9):
		# print (mN.seq_Wand_0[i].get_koordinaten() )

	#  - grid.distanz()

	#  - grid.punkte() -> Punkte in Sequenz einfuegen 
	#    alle Punkte des Gitter sind hier gespeichert 
	#    die Anzahl ist über len() bekannt.
	print('Knotenliste erstellt.')
	meineKnotenliste = []

	# Zahlvariable
	i=0

	print('\n# # # Starte Hauptschleife # # #\n')
	while(i<1):
		
		print('Transportschritt')
		# Wende auf alle Knoten den Transportschritt an
		pass

		print('Kollisionsschritt')
		# Wende auf alle Knoten den Kollisionsschritt an
		pass

		print('Ergebnbis')
		# Berechne fuer jeden Knoten das Ergebnis
		pass

		# zaehl hoch
		i=i+1 

	#Post-Processing
	print('\n \ \ \ Post-Processing # # #\n')

if __name__ == '__main__':
	print('\nmain.py starten.\n')
	main()
	print('\nProgrammende')
