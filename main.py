## 
## 
## // Portierung eines Gitter-Boltzmann-Lösers von C++ nach Python \\
##
## Version: v0.1
##
## Author : Dipl. Wirtsch.-Ing. Stefan Eickholz (Fachbereich Maschinenbau)
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
import einlassknoten as elk
import fluidknoten as flk
import wandknoten as wdk
import auslassknoten as ask
from linie import *
# import grid
# from grid import *
import grid as gd
import eingabe as eg
import ausgabe as ag
import hilfsfunktionen as hlf
import math as ma


# Parameter einlesen
# Objekte erzeugen
def vorbereitungen():
	print('# # # Vorverarbeitung / / / \n')
	pass

def nachverarbeitung():
	# Post-Processing
	print('\n \ \ \ Nachverarbeitung # # #\n')
	pass

def main():
	# Erzeuge Ausgabe Objektreferenz
	ausgabe = ag.Ausgabe()

	# Erzeuge Eingabe Objektreferenz
	eingabe = eg.Eingabe()
	#eingabe.schreibeWerte()

	# Erzeuge Zeit-Objekt
	#

	# # # 
	# Nonee = 0
	# Fluid = 1
	# Wand = 2
	# Solid = 3
	# Periodisch = 4
	# Einlass = 5
	# Auslass = 6
	# # # 

	# Gitter
	#
	# Gitter Parameter waehlen
	print("# # # Gitteraufbau")
	dY = eingabe.get_dY()
	print("Anzahl Knoten in Y-Richtung (Breite Stroemungskanal): ", dY)
	dX = eingabe.get_dX()
	print("Anzahl Knoten in X-Richtung (Laenge Stroemungskanal): ", dX)
	abst = eingabe.get_abstand()
	print("Knotenabstand: ", abst)

	# Gitter Objekt erzeugen
	meinGitter = gd.Gitter(par_xK=dX, par_yK=dY, par_abstand=abst)

	# Knoten des Gitters erzeugen
	meinGitter.erzeugeGitter_v2()
	#meinGitter.print_All()

	# Erstelle Feld mit Typangabe
	hlf.erstelleTypfeld(meinGitter, eingabe)
	#hlf.printTypfeld(meinGitter, eingabe)
	#hlf.laengeTypfeld(meinGitter, eingabe)

	# Geometrie Stroemungshindernis aufbauen
	eingabe.get_poly()
	
	# Schreibe die erste VTK Datei heraus ("T0.vtk")
	# Beachte auch den Dateikopf
	ausgabe.schreibeVTK(meinGitter)


	# check_anzahl_knoten = mN.getKnotenZahl()
	# print(check_anzahl_knoten) # gibt 10 aus, check

	#  - grid.distanz()

	#  - grid.punkte() -> Punkte in Sequenz einfuegen 
	#    alle Punkte des Gitter sind hier gespeichert 
	#    die Anzahl ist über len() bekannt.
	#print('Knotenliste erstellt.')

	# Datenstruktur?
	meineKnotenliste = []

	# Stoffdaten
	kw_rho = 1/eingabe.get_rho()

	# Gewichtungen der Gleichverteiung
	tp0 = 4.0/9.0
	tp1 = 1.0/9.0
	tp2 = 1.0/36.0

	# Hilfsvariablen
	cs2=eingabe.get_cs()**2
	EQ_t0_h = (tp1/cs2)*eingabe.get_rho()
	EQ_t45_h = (tp2/cs2)*eingabe.get_rho()
	EQ_t0_h = (tp0/cs2)*eingabe.get_rho()
	EQ_HV1_h = ((eingabe.get_xi()**2)/cs2)
	EQ_HV2_h = (eingabe.get_xi()*kw_rho)

	# Felder fuer Verteilungen
	# D2Q9-
	dq_count = 9
	#VL = np.random.randn(knotenMax)
	VL = np.ones(dX*dY*dq_count)
	#VL = np.full ( (dY*dq_skalierung, dX*dq_skalierung), 1, dtype=float)
	ZW = np.ones(dX*dY*dq_count)
	EQ = np.ones(dX*dY*dq_count)

	# Feldgroesse entsprich Knotenzahl
	# jeder Knoten hat nur einen Wert fuer 
	# Druck, vx, vy
	Druck = np.ones(dX*dY)
	VX = np.ones(dX*dY)
	VY = np.ones(dX*dY)

	# Feldinitialisierung
	#
	#



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

if __name__ == '__main__':
	print('\n__main__ starten.\n')

	# 1.
	vorbereitungen()

	# 2.
	main()
	
	# 3.
	nachverarbeitung()

	print('\nProgrammende')
