
print('gitter.py importiert.')

from node import *

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
# 3. 2D Gitter morphologisch/adaptiv
# 4. 3D Gitter morphologisch/adaptiv

# Klasse Gitter
#
# Definiert, wie das Gitter im Detail erzeugt wird.

class Gitter (object):

	# Klassenvariablen
	#
	# List aller Knoten im Gitter

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

	# Instanzvariablen
	def __init__(self, par_abstand, par_xK, par_yK):
		
		# Abstand der Knoten 
		# Im Prototyp v0.1 entspricht der Abstand
		# dem Betrag 1
		#
		self.abstand = par_abstand
		
		# xk = X-Knoten
		self.xk = par_xK
		
		# yk = Y-Knoten
		self.yk = par_yK

		# Berechne gerade Anzahl an Knoten
		# self.anzahl_x_knoten = Eingabe.dX/self.abstand

		# Aktualisiere Abstand
		# self.abstand = Eingabe.dx/self.anzahl_x_knoten

		#
		# self.anzahl_x_knoten = self.anzahl_x_knoten+1

		#
		# self.anzahl_y_knoten = Eingabe.dy/self.abstand

		#
		# self.anzahl_y_knoten = self.anzahl_y_knoten+1


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

	# Fuer Knoten, die sich im Graubereich befinden 
	# Prueft Knotentyp
	# 
	def graupruefung(self):
		pass

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
			print(seq_Einlass)
			b=b+1

		# Einlass
		# oben links = Knoten ky = Wandknoten
		# Knotennummer 49
		seq_Wand_1.append( Wandknoten(0, ky_) )

		# Grauknoten
		# hier wird es haarig
		# Prototyp v0.1 kennt kein Hindernis!

	def erzeugeGitter_v1(self):
		
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
			self.seq_Wand_0.append( Wandknoten(0, a) )
			a=a+1
			# print(self.seq_Wand_0)

	def printGitter(self):
		myNodes = len(self.seq_Wand_0)
		zaehler = 0
		while(zaehler<myNodes):
			print('Knoten: ', self.seq_Wand_0[zaehler])
			zaehler = zaehler+1

	def getKnotenZahl(self):
		zahl = len(self.seq_Wand_0)
		return zahl	


	def punktImPolygon(self):
		pass

	def findeNachbarn(self):
		pass

	def distanz(self):
		pass

	# Zugriff Objekt-Attribute
	#
	# Liefert die Anzahl der Knoten in X-Richtung zurueck
	def getAnzahlXKnoten(self):
		return self.anzahl_x_knoten

	# Zugriff Objekt-Attribute
	#
	# Liefert die Anzahl der Knoten in Y-Richtung zurueck
	def getAnzahlYKnoten(self):
		return self.anzahl_y_knoten

	# Zugriff Objekt-Attribute
	# 
	# Liefert den Knotenabstand als Rueckgabewert
	def getAbstand(self):
		return self.abstand

	# 
	def punktHinzufuegen(self, mySequence, x_Node):
		mySequence.append(x_Node)
		return 



