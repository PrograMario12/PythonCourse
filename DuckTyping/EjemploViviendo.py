class Vivienda:
	def abrirPuerta(self):
		print("Abriendo puerta")

class Persona:
	def ingresarVivienda(self, vivienda):
		vivienda.abrirPuerta()
		#Asumimos que una vivienda debe tener el método abrir puerta

departamento = Vivienda()
perso = Persona()
perso.ingresarVivienda(departamento)