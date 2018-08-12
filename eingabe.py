print('Importiere: Subklasse Eingabe')
import math as m

class Eingabe(object):
	def __init__(self):

		self.seq_dict = dict()
		# Stroemungsparameter

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
		return self.dX

	def get_dY(self):
		return self.dY

	def get_abstand(self):
		return self.abstand

	def get_charL(self):
		return self.charL

	def get_polygonzug(selk):
		pass

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