print('node.py importiert.')

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
print('\nImportiere: Wurzelklasse Knoten')
class node (object):
	# def __init__(self):
	def __init__(self, par_x, par_y, par_typ=Knotentyp(0) ):
		self.xKoord = par_x
		self.yKoord = par_y

		# def __init__(par_druck, par_init_vx, par_init_vy, par_rho, par_cs, par_xi, par_omega, par_u0x, par_u0y, par_eta, par_abstand, par_charL):
		# par_ = Parameter
		# self.druck   = par_druck
		# self.init_vx = par_init_vx
		# self.init_vy = par_init_vy
		# self.rho     = par_rho
		# self.cs      = par_cs
		# self.xi      = par_xi
		# self.omega   = par_omega
		# self.u0x     = par_u0x
		# self.u0y     = par_u0y
		# self.eta     = par_eta
		# self.abstand = par_abstand
		# self.charL   = par_charL



		"""
		def __init__(self):
        	self.attribute = {
            	'druck':     ,
            	'init_vx':  ,
            	'init_vy':
        }

    	def __getitem__(self,i):
        	return self.info[i]
		"""
	
	def get_x_koordinate(self):
		return self.xKoord
	
	def get_y_koordinate(self):
		return self.yKoord

	def get_koordinaten(self):
		print('{} {}'.format(self.xKoord, self.yKoord))

	def transport():
		pass
	
	def kollidiere():
		pass
	
	def kalkuliereGleichverteilung():
		pass
	
	def kalkuliereErgebnis():
		pass

print('Importiere: Subklasse Fluidknoten')
# Subknoten
class Fluidknoten(node):
	def __init__(self, xKoord, yKoord, typ=Knotentyp(1) ):
		self.xKoord = xKoord
		self.yKoord = yKoord


print('Importiere: Subklasse Wandknoten')
# Wandknoten
# class Wandknoten(node):
# 	def __init__(par_x, par_y, par_typ=Knotentyp(2) ):
# 		self.xKoord = par_x
# 		self.yKoord = par_y
# 		self.typ = par_typ

class Wandknoten(node):
	def __init__(self, par_typ=Knotentyp(2)):
		self.typ = par_typ

	def get_attributes(self):
		print('{} {} {}'.format(self.xKoord, self.yKoord, self.typ))
		
print('Importiere: Subklasse Flussknoten_Einlass')
# Einlass und Auslass vom Stroemungskanal
class Flussknoten_Einlass(node):
	def __init__(self, xKoord, yKoord, typ=Knotentyp(5) ):
		self.xKoord = xKoord
		self.yKoord = yKoord

print('Importiere: Subklasse Flussknoten_Auslass\n')
# Einlass und Auslass vom Stroemungskanal
class Flussknoten_Auslass(node):
	def __init__(self, xKoord, yKoord, typ=Knotentyp(6) ):
		self.xKoord = xKoord
		self.yKoord = yKoord