'''Cree una clase Punto que reciba las coordenadas 
(x,y) y un método que indique a qué cuadrante 
pertence'''

class Punto:
	"""docstring for Punto"""
	def __init__(self, x, y):
		self.x = x
		self.y = y 

	@property
	def x(self):
		return self._x

	@x.setter
	def x(self, x):
		self._x = x

	@property
	def y(self):
		return self._y

	@y.setter
	def y(self, y):
		self._y = y

	@property
	def cuadrante(self):
		posicion = "Está en medio"
		print(self.x, " es el valor de x")
		if(self.x < 0 and self.y < 0):
			posicion = "Está en el cuadrante 3"
		elif (self.x < 0 and self.y > 0):
			posicion = "Está en el cuadrante 1"
		elif (self.x > 0 and self.y > 0):
			posicion = "Está en el cuadrante 2"
		elif (self.x > 0 and self.y < 0):
			posicion = "Está en el cuadrante 4"
		
		return posicion


p = Punto(5,0)
print(p.cuadrante)
print("X es igual a ", p.x)

p.x = 15
p.y = 2
print("X es igual a ", p.x)
print(p.cuadrante)