from node import *

# Einlass und Auslass vom Stroemungskanal
#
#
print('Importiere: Subklasse Flussknoten_Einlass')
class Flussknoten_Einlass(node):
	def __init__(self, par_x, par_y, typ=Knotentyp(5) ):
		super().__init__(par_x, par_y)