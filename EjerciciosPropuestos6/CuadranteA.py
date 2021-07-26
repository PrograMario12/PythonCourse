'''Cree una clase Punto que reciba las coordenadas 
(x,y) y un método que indique a qué cuadrante 
pertence'''

class Punto:
	"""docstring for Punto"""
	def __init__(self, x, y):
		self.x = x
		self.y = y 

	def cuadrante(self):
		cuadrante = "Está en medio"
		if(self.x < 0 and self.y < 0):
			cuadrante = "Está en el cuadrante 3"
		elif (self.x < 0 and self.y > 0):
			cuadrante = "Está en el cuadrante 1"
		elif (self.x > 0 and self.y > 0):
			cuadrante = "Está en el cuadrante 2"
		elif (self.x > 0 and self.y < 0):
			cuadrante = "Está en el cuadrante 4"
		return cuadrante

p = Punto(5,0)
print(p.cuadrante())

p.x = 3
p.y = 8

print(p.cuadrante())