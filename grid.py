
print('gitter.py importiert.')


# Uniformes Gitter 
# Bisher ist nur eine Art von Gitter
# realisiert
class Gitter (object):

	# Class Variables
	# List aller Knoten im Gitter
	seq_kL = []
	seq_kL.append(15)
	print(seq_kL)

	# Instance Variables
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



	def erzeugeGitter():
		pass

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



