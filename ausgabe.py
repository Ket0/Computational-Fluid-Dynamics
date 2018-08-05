print('Importiere: Subklasse Ausgabe')
import time as tm
import math as mt

class Ausgabe(object):
	def __init__(self):
		pass

	def schreibeVTK(self, Gitter):
		# Der Dateiname wird durch einen
		# Zaehler variiert
		filename = ""
		#filename = tm.ctime() #Wed Aug  1 00:12:19 2018
		
		# Erstelle Stopuhr
		filename = tm.clock() # 7.551344422482617e-07
		
		# Berechnung
		# VTK schreiben
		#tm.sleep(1)
		filename = tm.clock()
		#print("name: %s", filename)

		firstClock = filename
		firstClock = str(firstClock)

		# Datei oeffnen und schreiben
		#myInt = int(filename)
		#print("handle: ", myInt)

		# Runden
		#filename = round(filename, 0)
		filename = mt.ceil(filename)

		# f == float
		# i == integer
		#sv1 = "T%1.3f" % filename
		#------>---<--genaue Formatangabe
		sv1 = "T%1i" % filename
		#print("handle: ", sv1)
		f = open(sv1+".vtk", 'w')
		#f.write(firstClock+"\n")

		# Konvertiere benoetigte Daten
		x = str(Gitter.getLaenge())
		y = str(Gitter.getBreite())
		a = str(Gitter.getAbstand())

		# Schreibe Dateikopf
		f.write("# vtk DataFile Version 2.0\n")
		Zeitmarke=tm.ctime()
		Zeitmarke=str(Zeitmarke)
		f.write(Zeitmarke+"\n")
		f.write("ASCII\n")
		f.write("DATASET STRUCTURED_POINTS\n")
		f.write("DIMENSIONS " + x + " " + y + " 1\n")
		f.write("ORIGIN 0 0 0\n")
		f.write("SPACING " + a + " " + a + " 1\n")

		# grid.all.size() 
		# gibt Anzahl Solidknoten
		# zurueck

		f.write("POINT_DATA " + "\n")
		f.write("SCALARS " + "Druck " + "FLOAT\n")
		# Fuer alle SOLID Knoten, gib '0' aus
		# sonst den druck()
		f.write("LOOKUP_TABLE default\n")
		# Iteriere über das gesamte Gitter
		#
		# Iteriere über die Datenstruktur Solid und 
		# gebe schreibe fuer jeden Solid Null
		
		knotenzahl = len(Gitter.seq_Type)
		for iterator in range(0, knotenzahl):
			if (Gitter.seq_Type[] == 3):
				f.write('0\n')
			else
				#schreibe Druck


		#anzahlElemente = len(Gitter.seq_Solid)

		# Schreibe mehrere Werte in Datei
		i = 0
		while(i<5):
			counter=tm.clock()
			# build in Funktion 'write'
			# kann String als Argument
			# aufnehmen!
			counter = str(counter)
			# +\n schreibt jeden Wert
			# in eine neue Zeile
			f.write(counter+"\n")
			i += 1
		f.close()

		# Öffne *.vtk und drucke 
		# den Inhalt aus
		# Beachte, dass drucken 
		# nur im 'Read Modus'
		# möglich ist
		f = open("T1.vtk", 'r')
		# Zeilenweise Iteration ueber das 
		# Referenzobjekt
		for line in f:
			print(line)
		f.close()

		




