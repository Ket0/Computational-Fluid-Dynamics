## 
## 
## // Portierung eines Gitter-Boltzmann-Lösers von C++ nach Python \\
##
## Version: 1.0
##
## Author : Stefan Eickholz
## Datum:   11.06.2018
## Ort: 	Potsdam
## Sprache: Python
## Version: 3.6.1
##

## In den folgend gezeigten Programmanweisungen wird ein bestehender CFD Löser für ein zweidimensionales
## Stroemungsgebiet, geschrieben in der Sprache C++, auf Python portiert.
##  
## 

import time
import numpy as np
import node
import grid


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

print('main.py starten.')
print('\nProgrammstart\n') 

print('Pre-Processing')
# Pre-Processing

# Erzeuge Eingabe-Objekt
#
#
oE = Eingabe()

# Erzeuge Ausgabe-Objekt
# Erzeuge Zeit-Objekt
# Erzeuge Ausgabe-Objekt


abstand = 0.015
dX = 2.5
dY = 0.41 

# Erzeuge Gitter-Objekt
#
# (Eingabe, par_abstand, par_xK, par_yK):
# mN = grid.Gitter(Eingabe_obj, Eingabe_obj.abstand, Eingabe_obj.dX, Eingabe_obj.dY)
mN = grid.Gitter(par_abstand=abstand, par_xK=dX, par_yK=dY)
#  - grid.generiereGitter()
#  - grid.distanz()


#  - grid.punkte() -> Punkte in Sequenz einfuegen 
#    alle Punkte des Gitter sind hier gespeichert 
#    die Anzahl ist über len() bekannt.
print('Knotenliste erstellt.')
meineKnotenliste = []




# Calculation

# Hauptschleife

# Ausgabe 
# Schreibe in VTK Datei

# Oeffne Datei

# Zahlvariable
i=0

print('\nStarte Hauptschleife\n')
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
print('\nPost-Processing\n')
print('\nProgrammende')