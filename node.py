
print('node.py importiert.')

# Wurzel der Vererbungshierachie
# 
# Knoten
class node (object):
	def __init__(par_druck, par_init_vx, par_init_vy, par_rho, par_cs, par_xi, 
		par_omega, par_u0x, par_u0y, par_eta, par_abstand, par_charL):
		# par_ = Parameter
		self.druck   = par_druck
		self.init_vx = par_init_vx
		self.init_vy = par_init_vy
		self.rho     = par_rho
		self.cs      = par_cs
		self.xi      = par_xi
		self.omega   = par_omega
		self.u0x     = par_u0x
		self.u0y     = par_u0y
		self.eta     = par_eta
		self.abstand = par_abstand
		self.charL   = par_charL
	
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
	def __init__ (self, par_druck, par_init_vx, par_init_vy, par_rho, par_cs, par_xi, 
		par_omega, par_u0x, par_u0y, par_eta, par_abstand, par_charL, 
		parameter_fuer_Fluidknoten):
		Fluidknoten.__init__(self, par_druck, par_init_vx, par_init_vy, par_rho, par_cs, par_xi, 
		par_omega, par_u0x, par_u0y, par_eta, par_abstand, par_charL)
		pass

class Randknoten(node):
	def __init__():
		pass

# Einlass und Auslass vom Stroemungskanal
class Flussknoten(node):
	def __init__():
		pass

	
