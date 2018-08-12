from node import *

# Einlass und Auslass vom Stroemungskanal
#
#
print('Importiere: Subklasse Flussknoten_Auslass\n')
class Flussknoten_Auslass(node):
	def __init__(self, par_x, par_y, typ=Knotentyp(6) ):
		super().__init__(par_x, par_y)