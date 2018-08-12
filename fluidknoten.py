from node import *

print('Importiere: Subklasse Fluidknoten')
class Fluidknoten(node):
	def __init__(self, par_x, par_y, typ=Knotentyp(1) ):
		super().__init__(par_x, par_y)
		self.druck=0
		self.vx=0
		self.vy=0

	def transport(self):
		pass