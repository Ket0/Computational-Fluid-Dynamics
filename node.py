#print('node.py importiert.')
#print('Importiere: node.py')
print('\nImportiere: Wurzelklasse Knoten')

import enum

# Diese Knotentypen sind vorhanden
class Knotentyp(enum.Enum):
	Nonee = 0
	Fluid = 1
	Wand = 2
	Solid = 3
	Periodisch = 4
	Einlass = 5
	Auslass = 6

# Wurzel der Vererbungshierachie
# 
# Vererbe Interface Knoten an Subknotentypen
# Wurzelknoten/Basisklasse

class node (object):
	# def __init__(self):
	def __init__(self, par_x=0.0, par_y=0.0, par_typ=Knotentyp(0) ):
		self.xKoord = par_x
		self.yKoord = par_y

	def set_x_koordinate(self, x):
		self.xKoord=x
		return None

	def set_y_koordinate(self, y):
		self.yKoord=y
		return None

	def get_x_koordinate(self):
		return self.xKoord
	
	def get_y_koordinate(self):
		return self.yKoord

	def get_koordinaten(self):
		#print( '{} {}'.format(self.xKoord, self.yKoord) )
		return self.xKoord, self.yKoord

	def print_koordinaten(self):
		print("X-Koordinate: ", self.xKoord)
		print("Y-Koordinate: ", self.yKoord)

	def get_attributes(self):
		return self.xKoord, self.yKoord, self.typ

	def transport(self):
		pass
	
	def kollidiere(self):
		pass
	
	def kalkuliereGleichverteilung(self):
		pass
	
	def kalkuliereErgebnis(self):
		pass

	def set_ZWW(wert, i):
		pass

	def set_VTL(wert, i):
		pass 

	def set_vx(self):
		pass

	def set_vy(self):
		pass

	def set_druck(self):
		pass

	def initialisiereKnoten(self):
		# druck, vx, vy, rho, cs2, xi, omega, u0x, u0y, 
		# eta, abstand, L
		pass

	