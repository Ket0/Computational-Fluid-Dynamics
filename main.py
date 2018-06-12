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
import node
import grid



print('main.py starten.')
print('\nProgrammstart\n') 


# Pre-Processing

# Erzeuge Eingabe-Objekt
# Erzeuge Ausgabe-Objekt
# Erzeuge Zeit-Objekt
# Erzeuge Ausgabe-Objekt

# Erzeuge Gitter-Objekt
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

print('Starte Hauptschleife')
while(i<2):
	
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

print('\nProgrammende')