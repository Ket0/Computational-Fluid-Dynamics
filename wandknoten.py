from node import *

# Wandknoten
#
#
print('Importiere: Subklasse Wandknoten')
class Wandknoten(node):
	def __init__(self, par_x, par_y, par_typ=Knotentyp(2)):
		super().__init__( par_x, par_y)
		self.typ = par_typ