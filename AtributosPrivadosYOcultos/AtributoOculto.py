class Usuario:
	def __init__(self, nombre, contenidoPremium):
		self.nombre = nombre 
		self.__contenidoPremium = contenidoPremium

user = Usuario("Mario Abarca", "Curso de Python")

print(user.nombre)
#print(user.__contenidoPremium)

print(user._Usuario__contenidoPremium)