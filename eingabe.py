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

	def teste_Knotengleichheit_func1(self, k1, k2):
		print("Teste Geometrie auf Geschlossenheit")
		
		# Teste X-Koordinate
		if( k1.get_x_koordinate() != k2.get_x_koordinate() ):
			return False
		else: 
			return True
		
		# Teste Y-Koordinate
		if ( k1.get_y_koordinate() != k2.get_y_koordinate() ):
			return False
		else:
			return True

	def teste_Knotengleichheit_func2(self):
		print("Teste Geometrie auf Geschlossenheit")

		# Alle Knoten in einer Liste speichern
		f = open('geometrie.txt', 'r')
		alleKnoten = f.readlines()
		print(alleKnoten)
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
			return True


	def get_poly(self):

		self.seq_list = []

		# In der Datei liegen die Koordinaten
		# des Knoten in der Form x,y,x,y,x,y...
		f = open('geometrie.txt', 'r')
		
		# Pruefe, ob die Geometrie in Ordnung ist...
		dateiname="geometrie.txt"
		zz=self.file_len(dateiname) #ZeilenZahl	
		
		# Zeilenzahl muss ohne Rest teilbar sein!
		# Sonst wuerde eine Koordinate fehlen
		print("Teste Koordinaten auf Vollstaendigkeit")
		if (zz%2)!=0:
			print("Fehler: Stroemungshindernis hat ungerade Koordinatenzahl!")
			sys.exit()
		else:
			print(zz%2)
		
		# Mininum sind drei Knoten, daher muessen mindestens 
		# sechs Koordinaten vorhanden sein.
		print("Teste Koordinaten auf Knotenminimum drei")
		if zz<=6:
			print("Fehler: Zu wenig Knoten um Stroemungshindernis aufzubauen!")
			sys.exit()
		else:
			print(zz)

		print("Schliesse Datei")
		f.close()

		self.teste_Knotengleichheit_func2()




		# Letzer Knoten ('n) muss wieder dem ersten Knoten ('0') entsprechen
		# Koordinaten Knoten Null
		#koordinate_1_x=f.readline()
		#koordinate_1_y=f.readline()

		# Koordinaten Knoten 'n'
		#koordinate_n_x=f.readline()
		#koordinate_n_y=f.readline()




		# Erzeuge Testknoten
		#print("Erzeuge Testknoten")
		#k_test_1=node(koordinate_1_x, koordinate_1_y)
		#k_test_n=node(koordinate_n_x, koordinate_n_y)

		#if self.teste_Knotengleichheit(k_test_1, k_test_n) != True:
	#		print("Fehler: Hindernisgeometrie nicht geschlossen!")
	#		print("Knoten 1: ")
	#		k_test_1.print_koordinaten()
	#		print("Knoten n: ")
	#		k_test_n.print_koordinaten()
	#		sys.exit()
	#	else:
	#		pass

		# lese knoten 1
		#  x, y
		# lese knoten 2
		#  x, y
		# erzeuge neue Linie 
		# und speichere die Linie
		# in der Liste 
				
		# for iterator in range(0, int(zeilenZahl)):
		# 	x1=f.readline()
		# 	y1=f.readline()
		# 	k1=node(x1,y1)

		# 	x2=f.readline()
		# 	y2=f.readline()
		# 	k2=node(x2,y2)

		# 	linie=linie(k1,k2)
		# 	self.seq_list.append(linie)



		#self.node.set_x_koordinate(f.readline)
		#self.node_one.set_x_koordinate(f.readline)


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








"""
# Druck muss berechnet werden
cs_ = sqrt(u0x*u0y + u0y*u0y) / machZahl
initialisierungsDruck = cs*cs*rho
# Weiterhin berechnet wird
xi = 
Zeitschritt = 
omega = 
"""