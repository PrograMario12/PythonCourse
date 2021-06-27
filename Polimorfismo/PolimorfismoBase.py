class Humano:
	def atacar(self):
		print("Puñetazo!")

class Rey(Humano):
	pass

class Mago(Humano):
	pass
	# def atacar(self):
	# 	print("Hechizo!")

class Guerrero(Humano):
	def atacar(self):
		print("Espada!")
		
class Brujo(Mago, Guerrero):
	pass

if __name__ == '__main__':
	humano = Humano()
	rey = Rey()
	mago = Mago()
	guerrero = Guerrero()
	brujo = Brujo()

	humano.atacar()
	rey.atacar()
	mago.atacar()
	guerrero.atacar()
	brujo.atacar()

	print(Brujo.__mro__)