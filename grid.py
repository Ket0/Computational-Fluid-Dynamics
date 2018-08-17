
#print('gitter.py importiert.\n')
print('Importiere: Wurzelklasse Gitter')
#from node import *
import node as nd
import wandknoten as wdk
import einlassknoten as elk
import fluidknoten as flk
import math as math

# Uniformes Gitter 
# Bisher ist nur eine Art von Gitter
# realisiert

"""

2D

Aufbau des Gitters bzw. des Kanals ohne Hinderniss

E=Einlass
A=Auslass
W=Wand
F=Fluid

	Stroemungsrichtung ->

			'oben' hier

WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
EFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFA
EFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFA
EFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFA
EFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFA
EFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFA
EFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFA
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW

			'unten' hier

"""

# 2. 3D Gitter 

""" 

	3D Struktur (9 Elemente pro Ebene; 3 Ebenen = 9x3 Elemente)

= 3 Ebenen (aufgefaltet); S=Eingebetteter Solidknoten

   fff fff fff
   fff fSf fff
   fff fff fff

   ^   ^   ^
Oben Mitte Unten
 
"""

# 3. 2D Gitter morphologisch/adaptiv
# 4. 3D Gitter morphologisch/adaptiv

#print('Importiere: Subklasse UniformesGitter')
# Uniformes Gitter
class Gitter (object):
	def __init__(self, par_xK=128, par_yK=32, par_abstand=1):
		self.abstand = par_abstand
		self.xk = par_xK
		self.yk = par_yK
		#print('Konstruktor Klasse Gitter aufgerufen')

		# 0
		# hier sollte eine Art Knotenbegrenzung 
		# eingebaut werden, damit nicht zu 
		# viel Speicher belegt wird!
		# zb nicht mehr als 1.000k Knoten

		# 1 
		# korrigiere die Gitterparameter
		# caste auf jedenfall auf Ganzzahl
		# floor rundet immer ab, hier sollte 
		# ein vielfaches der nvidia warp size 
		# von 32 einzustellen!
		# 
		# print(self.abstand) # 1.0
		# print(par_xK) # 128
		# print(par_yK) # 32
		x=math.floor(par_xK/par_abstand)
		print("x:", x)
		# x=round(par_xK/par_abstand)
		# print("x:", x)

		# test auf Vielfache
		if self.xk % 32 == 0:
			self.xk = int(x)
		else:
			while (self.xk%32)!= 0:
				self.xk += 1
		# Bestimme Abstand
		self.abstand = par_xK/self.xk
		print("Abstand: ", self.abstand)
		# jeder Kanals vier mal so 
		# lang, wie breit
		y=int(0.25*self.xk)
		print("y: ", y)
		self.yk=y

		self.anzahlKnoten = self.xk*self.yk

	# Fluid (~99% aller Knoten)
	seq_Fluid = []

	# Wand 'unten' 
	seq_Wand_0 = []

	# Wand 'oben'
	seq_Wand_1 = []

	# Einlass
	seq_Einlass = []

	# Auslass
	seq_Auslass = []

	# Solid (sind von Wandknoten umgeben, siehe Zeile 101, UniformGrid.cpp)
	seq_Solid = []

	# Typ enthaelt einen Ganzzahlwert, der als Indikator  fuer den Typ steht
	# Laenge entspricht der Knotenanzahl im Gitter
	seq_Type = []

	# Datenstruktur als eigener Typ?
	seq_all = []

	# Fuer Knoten, die sich im Graubereich befinden 
	# Prueft Knotentyp
	# 
	def graupruefung(self):
		pass

	"""
	Problemstellung (fuer beliebig gewaehlten Abstand)
	Graubereich ist die Fläche bzw. das Volumen (3D) in 
	direkter Nähe um den Polygonzug

	Polygonzug = /
	Fluid = F
	Solid = S
	Wand = W

			F F F F / S
			F F F / S S
			F F / S S
		  F	F / S S S
	      F F F / / /

	"""

	# Zugriff Objekt-Attribute
	#
	# Liefert die Anzahl der Knoten in X-Richtung zurueck
	def getLaenge(self):
		return self.xk

	# Zugriff Objekt-Attribute
	#
	# Liefert die Anzahl der Knoten in Y-Richtung zurueck
	def getBreite(self):
		return self.yk

	# Zugriff Objekt-Attribute
	# 
	# Liefert den Knotenabstand als Rueckgabewert
	def getAbstand(self):
		return self.abstand

	def punktImPolygon(self):
		pass

	def findeNachbarn(self):
		pass

	def distanz(self):
		pass

	def erzeugeGitter_v1(self):
		print('Methode Gitter.erzeugeGitter_v1 aufgerufen')
		# Zaehler
		a=0
		b=0

		# Knoten in x-Richtung
		kx_ = self.xk

		# Flussknoten_Einlass in y-Richtung
		ky_ = self.yk-1
		
		# Wand unten (=Wand_0)
		# unten links = Knoten Null
		while(a<kx_):
			self.seq_Wand_0.append( nd.Wandknoten(0, a) )
			a=a+1
			# print(self.seq_Wand_0)

		# Wand oben (=Wand_1)
		# 
		while(b<ky_):
			self.seq_Wand_1.append( nd.Wandknoten(self.yk, b) )
			b=b+1
			# print(self.seq_Wand_0)		

		# Ränder
		# πάντα ῥεῖ

	# Typpruefung im Bereich der Umschlingungskurve
	def umschlingungskurve(self):
		pass

	def erzeugeGitter_v2(self):
		print('\nMethode Gitter.erzeugeGitter_v1 aufgerufen')
		# Zaehler
		a=0
		b=0
		index=0
		imin=0
		imax=0

		# Knoten in x-Richtung
		kx_ = self.xk

		# Flussknoten_Einlass in y-Richtung
		ky_ = self.yk-1
		
		# # # 
		# Nonee = 0
		# Fluid = 1
		# Wand = 2
		# Solid = 3
		# Periodisch = 4
		# Einlass = 5
		# Auslass = 6
		# # # 

		# 1 Einlass
		# 
		print(" Einlassknoten")
		self.seq_all.append(wdk.Wandknoten(0 ,0.0 ,2))
		b=1
		while b<(self.yk-1):
			self.seq_all.append(elk.Flussknoten_Einlass(0, b*self.abstand,5))
			#index += 1
			b += 1
		self.seq_all.append(wdk.Wandknoten(0, (self.yk-1)*self.abstand, 2))

		# 2 Kanal
		#
		print(" Kanal")
		a=1
		#b=0
		#c=1
		while (a*self.abstand)<(self.xk-1):
			self.seq_all.append(wdk.Wandknoten(a*self.abstand, 0, 2 ))
			
			# In der Mitte des Kanals befinden sich nur 
			# Fluidknoten
			c=1
			b=1
			while c<(self.yk-1):
				self.seq_all.append(flk.Fluidknoten(a*self.abstand, b*self.abstand, 1))
				#index += 1
				c += 1
				b += 1
				# if len(self.seq_all) == (self.anzahlKnoten/2):
				# 	print("Haelfte aller Knoten generiert")
			self.seq_all.append(wdk.Wandknoten(a*self.abstand, (self.yk-1)*self.abstand, 2 ) )
			a += 1

		# # 3
		# # Bereich Stroemungshindernis
		# # hier wird es haarig
		# # self.umschlingungskurve()

		# 4 Auslass
		#
		print(" Auslass")
		a=self.xk-1 # Letzte Reihe
		self.seq_all.append(wdk.Wandknoten(a*self.abstand, 0, 2 ) )
		b=1
		while b<(self.yk-1):
			self.seq_all.append(wdk.Wandknoten( a*self.abstand, b*self.abstand, 6) )
			b += 1
		self.seq_all.append(wdk.Wandknoten( a*self.abstand, (self.yk-1)*self.abstand, 2 ))
		print("# # # Knotenliste erstellt!")
		# πάντα ῥεῖ

	def print_All(self):
		sMax=len(self.seq_all)
		for iterator in range(0, sMax):
			#print(self.seq_all[iterator].get_koordinaten())
			print("{} {}".format(self.seq_all[iterator].get_koordinaten(), self.seq_all[iterator].get_type()))

	def getKnotenZahl(self):
		return self.anzahlKnoten 

	def getAnzahlSolidknoten(self):
		zahl = len(self.seq_Wand_0)
		return zahl	

	# 
	def punktHinzufuegen(self, mySequence, x_Node):
		mySequence.append(x_Node)
		return 

	def punktInPolygon(self):
		pass

	def findeNachbarn(self):
		pass

	def wandAbstand(self):
		pass





"""
	# Prototyp abstrahiert vom Gitterabstand
	# 
	# 
	def erzeugeGitter_v0(self):
		
		# 
		# i=0
		# j=0
		# idx=0
		# imin=0
		# imax=0	
		# ny=anzahl_y_knoten-1

		a=0 
		b=0

		# Knoten in x-Richtung
		kx_ = self.xk

		# Flussknoten_Einlass in y-Richtung
		ky_ = self.yk-1

		# Einlass
		# unten links = Knoten Null = Wandknoten
		b=0
		seq_Wand_0.append( Wandknoten(0, b) )

		# Einlass
		b=1
		while(b<ky):
			seq_Einlass.append( Flussknoten(0, b+1) )
			# print(seq_Einlass)
			b=b+1

		# Einlass
		# oben links = Knoten ky = Wandknoten
		# Knotennummer 49
		seq_Wand_1.append( Wandknoten(0, ky_) )

		# Grauknoten
		# hier wird es haarig
		# Prototyp v0.1 kennt kein Hindernis!
"""