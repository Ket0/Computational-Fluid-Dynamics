print('Importiere: Subklasse Eingabe')

class Eingabe(object):
	def __init__(self):
		self.machZahl = 0.1
		self.charL = 0.1
		self.vx = 0.00730365
		self.vy = 0
		self.dichte = 1.225
		self.dynamischZa = 1.7894e-05
		# Gitter
		self.dX = 2.5
		self.dY = 0.41 
		self.abstand = 0.015
		# Initialisierungsdaten
		self.initVX =0.00730365
		self.initVY = 0

"""
# Druck muss berechnet werden
cs_ = sqrt(u0x*u0y + u0y*u0y) / machZahl
initialisierungsDruck = cs*cs*rho
# Weiterhin berechnet wird
xi = 
Zeitschritt = 
omega = 
"""