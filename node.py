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
# Knoten
class node (object):
	def __init__(self):
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
	
	def transport():
		pass
	
	def kollidiere():
		pass
	
	def kalkuliereGleichverteilung():
		pass
	
	def kalkuliereErgebnis():
		pass

# Vererbe Interface Knoten an Subknotentypen
class Fluidknoten(node):
	def __init__():
		pass


class Wandknoten(node):
	def __init__(xKoord, yKoord, typ=Knotentyp(2) ):
		pass

# myWandknoten = Wandknoten(0, 50)
# x=0
# myList_kL=[]

# while(x<10):
# 	myList_kL.append(Wandknoten(0+x, 0))
# 	print('Knoten: ', myList_kL[x])
# 	x=x+1

# Einlass und Auslass vom Stroemungskanal
class Flussknoten(node):
	def __init__():
		pass

	
