## 
## 
## // Portierung eines Gitter-Boltzmann-Lösers von C++ nach Python \\
##
## Version: v0.1
##
## Author:  Dipl. Wirtsch.-Ing. Stefan Eickholz (Fachbereich Maschinenbau)
## Datum:   01.08.2018
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

print('Importiere: Modul time')
import time

print('Importiere: Modul numpy')
import numpy as np

# from node import *
import node as nd
# import grid
# from grid import *
import grid as gd
import eingabe as eg
import ausgabe as ag

def main():
	print('# # # Pre-Processing / / / \n')

	# Erzeuge Ausgabe Objektreferenz
	ausgabe = ag.Ausgabe()
	# Erzeuge Eingabe Objektreferenz
	eingabe = eg.Eingabe()
	# Erzeuge Zeit-Objekt
	
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
	meinGitter = gd.UniformesGitter(par_xK=dX, par_yK=dY)
	#mN.erzeugeGitter_v1()

	# Schreibe die erste VTK Datei heraus ("T0.vtk")
	# Beachte auch den Dateikopf
	ausgabe.erzeugeVTK(meinGitter)


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
