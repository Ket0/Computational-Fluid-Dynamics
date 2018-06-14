
print('gitter.py importiert.')

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
		self.abstand = par_abstand

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
	def graupruefung():
		pass

	# Prototyp abstrahiert vom Gitterabstand
	# 
	# 
	def erzeugeGitter():
		
		# 
		# i=0
		# j=0
		# idx=0
		# imin=0
		# imax=0
		# ny=anzahl_y_knoten-1

		# Einlass
		# Grauknoten





	def punktImPolygon():
		pass

	def findeNachbarn():
		pass

	def distanz():
		pass

	# Zugriff Objekt-Attribute
	#
	# Liefert die Anzahl der Knoten in X-Richtung zurueck
	def getAnzahlXKnoten():
		return self.anzahl_x_knoten

	# Zugriff Objekt-Attribute
	#
	# Liefert die Anzahl der Knoten in Y-Richtung zurueck
	def getAnzahlYKnoten():
		return self.anzahl_y_knoten

	# Zugriff Objekt-Attribute
	# 
	# Liefert den Knotenabstand als Rueckgabewert
	def getAbstand():
		return self.abstand

	# 
	def punktHinzufuegen(mySequence, x_Node):
		mySequence.append(x_Node)
		return 



