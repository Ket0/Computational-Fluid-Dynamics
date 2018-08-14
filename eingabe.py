print('Importiere: Subklasse Eingabe')
import math as m
from node import *
from linie import *
import sys

class Eingabe(object):
	def __init__(self):

		# Speicher physikalische Parameter in einer 
		# Datenstruktur, um sie einfacher ausgeben
		# zu koennen
		self.seq_dict = dict()

		# Datenstruktur Listensequenz
		# fuer Knotenpaare von Polygonzug
		self.seq_list = []

		# Stroemungsparameter
		#
		# Oeffne Datei
		f = open('parameter.txt', 'r')
		
		# Lies die Werte Zeile fuer Zeile ein
		# und konvertiere die Strings in 
		# Floatwerte
		self.machZahl=float(f.readline())
		self.charL=float(f.readline())
		self.vx=float(f.readline())
		self.vy=float(f.readline())
		self.rho=float(f.readline())
		self.eta=float(f.readline())
		self.dX=float(f.readline())
		self.dY=float(f.readline())
		self.abstand=float(f.readline())
		self.initVX=float(f.readline())
		self.initVY=float(f.readline())

		# Datei schliessen
		f.close()
		self.seq_dict['machZahl: '] = float(self.machZahl)
		self.seq_dict['Charakteristische Laenge: '] = float(self.charL)
		self.seq_dict['Stroemungsgeschwindigkeit in X-Richtung: '] = self.vx
		self.seq_dict['Stroemungsgeschwindigkeit in Y-Richtung: '] = self.vy
		self.seq_dict['Dichte: '] = self.rho
		self.seq_dict['Dynamische Zaehigkeit: '] = self.eta

		# Gitter
		self.seq_dict['Gitterknoten X-Richtung: '] = self.dX
		self.seq_dict['Gitterknoten Y-Richtung: '] = self.dY
		self.seq_dict['Gitterabstand: '] = self.abstand

		# Initialisierungsdaten
		self.seq_dict['Initialisierungsgeschwindigkeit X-Richtung: '] = self.initVX
		self.seq_dict['Initialisierungsgeschwindigkeit Y-Richtung: '] = self.initVY

		self.maxX=0.0
		self.maxY=0.0
		self.minX=0.0
		self.minY=0.0

		self.cs=1
		float(self.cs)
		self.xi=1
		float(self.xi)
		self.timeStep=1
		float(self.timeStep)
		self.omega=1
		float(self.omega)

		# Fuehre weitere Berechnungen durch
		self.cs=m.sqrt(float(self.vx)**2 + float(self.vy)**2)/float(self.machZahl)
		self.seq_dict['Isotherme Schallgeschwindigkeit: '] = self.cs
		self.xi=m.sqrt(3)*self.cs
		self.seq_dict['Molekulare Einheitsgeschwindigkeit: '] = self.xi
		self.Zeitschritt=float(self.abstand)/float(self.xi)
		self.seq_dict['Zeitschritt: '] = self.Zeitschritt		
		cs_q = self.cs**2
		self.omega=(float(cs_q)*float(self.Zeitschritt)) / ((float(self.eta)/float(self.rho))+float(cs_q)*float(self.Zeitschritt)*0.5)
		self.seq_dict['Molekulare Kollisionsfrequenz: '] = self.xi

	def berechneWP(self):
		self.cs=m.sqrt(self.vx**2 + self.vy**2)/self.machZahl
		self.seq_dict['Isotherme Schallgeschwindigkeit: '] = self.cs
		self.xi=m.sqrt(3)*self.cs
		self.seq_dict['Molekulare Einheitsgeschwindigkeit: '] = self.xi
		self.Zeitschritt=self.abstand/self.xi
		self.seq_dict['Zeitschritt: '] = self.Zeitschritt		
		cs_q = self.cs**2
		self.omega=(cs_q*self.Zeitschritt) / ((self.eta/self.rho)+cs_q*self.Zeitschritt*0.5)
		self.seq_dict['Molekulare Kollisionsfrequenz: '] = self.xi

	def schreibeWerte(self):
		print("Physikalische Parameter")
		for parameter, wert in self.seq_dict.items():
			print(parameter, wert)

	def get_dX(self):
		dxTemp=self.dX
		return int(dxTemp)

	def get_dY(self):
		dyTemp=self.dY
		return int(dyTemp)

	def get_anzahlKnoten(self):
		x=self.get_dX()
		y=self.get_dY()
		res=x*y
		return int(res)

	def get_abstand(self):
		return self.abstand

	def get_charL(self):
		return self.charL

	# Zaehlt Zeilen einer Datei
	def file_len(self, dateiname):
		with open(dateiname) as f:
			for i, l in enumerate(f):
				pass
		return i + 1

	# Vergleicht zwei Konten auf Identitaet
	# Liefert True, wenn identisch
	# Sonst False
	def teste_Knotengleichheit_func1(self, k1, k2):		
		# Teste X-Koordinate
		if( k1.get_x_koordinate() == k2.get_x_koordinate() ):
			if( k1.get_y_koordinate() == k2.get_y_koordinate() ):
				#print("True")
				return True
			else: 
				#print("False")
				return False

	def teste_Knotengleichheit_func2(self):
		print(" Teste Geometrie auf Geschlossenheit")

		# Alle Knoten in einer Liste speichern
		f = open('geometrie.txt', 'r')
		alleKnoten = f.readlines()
		#print(alleKnoten)
		f.close()

		# Laenge der Liste bestimmen
		leaenge=len(alleKnoten)

		# Koordinaten fuer paarweisen Vergleich
		# extrahieren
		kx1=alleKnoten[0]
		ky1=alleKnoten[1]

		kxn=alleKnoten[leaenge-2]
		kyn=alleKnoten[leaenge-1]

		if float(kx1)!=float(kxn): 
			print("False")
			print("kx1: %d, kxn: %d", kx1, kxn)
			return False
		elif float(ky1)!=float(kyn):
			print("False")
			print("{}{}".format(ky1, kyn))
			return False
		else:
			print("  Testergebnis: ok")
			return True


	def get_poly(self):
		print("\nHindernisgeometrie einlesen")

		self.seq_list = []

		# 1
		# Diese Tests sollte eigentlich in eine
		# eigene Funktion...

		# In der Datei liegen die Koordinaten
		# des Knoten in der Form x,y,x,y,x,y...
		f = open('geometrie.txt', 'r')

		# Speicher alle Werte der Datei
		# einer Datenstruktur
		alleKnoten = f.readlines()
		f.close()

		# Pruefe, ob die Geometrie in Ordnung ist...
		dateiname="geometrie.txt"
		zz=self.file_len(dateiname) #ZeilenZahl	
		
		# Zeilenzahl muss ohne Rest teilbar sein!
		# Sonst wuerde eine Koordinate fehlen
		print(" Teste Koordinaten auf Vollstaendigkeit")
		if (zz%2)!=0:
			print("  Fehler: Stroemungshindernis hat ungerade Koordinatenzahl!")
			sys.exit()
		else:
			#print(zz%2)
			print("  Testergebnis: ok")
		
		# Mininum sind drei Knoten, daher muessen mindestens 
		# sechs Koordinaten vorhanden sein.
		print(" Teste Koordinaten auf Knotenminimum drei")
		if zz<=6:
			print("  Fehler: Zu wenig Knoten um Stroemungshindernis aufzubauen!")
			sys.exit()
		else:
			#print(zz)
			print("  Testergebnis: ok")

		# Teste auf Ueberschneidungsfreiheit!
		# fehlt hier noch

		# Ist die Geometrie geschlossen
		self.teste_Knotengleichheit_func2()


		# 2
		# Lies begrenzendes Viereck ein
		# alle X-Werte in Datenstruktur
		#
		# minX, maxX bestimmen
		#
		tmp_list1 = []
		for iterator in range(0, zz-1, 2):
			i = alleKnoten[iterator]
			tmp_list1.append(float(i))
			self.minX=min(tmp_list1)
			self.maxX=max(tmp_list1)

		# minY, minX bestimmen
		#
		# setze Startwert auf '1', dann
		# jeden 2. Wert
		tmp_list2 = []
		for iterator in range(1, zz-1, 2):
			i = alleKnoten[iterator]
			tmp_list2.append(float(i))
			self.minY=min(tmp_list2)
			self.maxY=max(tmp_list2)

		# print("{} {} {} {}".format(self.minX, self.maxX, self.minY, self.maxY))

		# 3
		# Speichere Linien (=Knotenpaare) in
		# Datenstruktur
		f = open('geometrie.txt', 'r')
		
		# Anzahl an Knoten ist ZeilenZahl zz halbe
		paarZahl = int(zz/2)
		# Anzahl an Linien ist paarZahl-1
		linienZahl = paarZahl-1

		zaehler=0
		while(zaehler<linienZahl):
			# Die ersten vier Koordinaten
			if zaehler==0:
				x1 = f.readline() 
				y1 = f.readline()
				x2 = f.readline()
				y2 = f.readline()
			else:
				# Vorgaenger zuweisen
				x1=x2
				y1=y2
				# Lese die naechsten zwei Koordinaten
				x2 = f.readline()
				y2 = f.readline()

			# Erzeuge Knoten
			k1 = node(x1,y1, 2)
			#print(k1.print_koordinaten())
			k2 = node(x2,y2, 2) 
			#print(k2.print_koordinaten())

			# Wenn Knoten nicht gleich, erzeuge Linie und 
			# speichere Linie in Datenstruktur
			# Andernfalls stop
			if self.teste_Knotengleichheit_func1(k1, k2) != True:
				# Erzeuge Linie
				l1 = Linie(k1, k2)
				# Fuege Linie in Datenstruktur ein
				self.seq_list.append(l1)
			else:
				print("Knoten sind identisch, letzte Linie hinzugefuegt!")
				break

			# Naechste Linie
			zaehler += 1

		f.close()

		#print(self.seq_list)
		#print(self.seq_list[0].get_punkte())
		#print("Schliesse Datei")
		print("Hindernisgeometrie einlesen abgeschlossen")


	def get_minX(self):
		return self.minX

	def get_minY(self):
		return self.minY

	def get_maxX(self):
		return self.maxX

	def get_maxY(self):
		return self.maxY

	def get_u0x(self):
		return self.u0x

	def get_u0y(self):
		return self.u0y

	def get_machZahl(self):
		return self.machZahl

	def get_xi(self):
		return self.xi

	def get_cs(self):
		return self.cs

	def get_timeStep(self):
		return self.timeStep

	def get_omega(self):
		return self.omega

	def get_rho(self):
		return self.rho

	def get_eta(self):
		return self.eta

	def get_initDruck(self):
		return self.initDruck

	def get_initVX(self):
		return self.initVX

	def get_initVY(self):
		return self.initVY

	def get_geometrie(self):
		return self.seq_list