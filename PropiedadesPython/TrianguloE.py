class Triangulo:
	def __init__(self, base, altura):
		self.base = base
		self.altura = altura

	@property
	def base(self):
		return self._base

	@base.setter
	def base(self, base):
		if base < 0:
			raise ValueError("La base no puede ser un número negativo")
		self._base = base

	@property
	def altura(self):
		return self._altura

	@altura.setter
	def altura(self, altura):
		if altura < 0:
			raise ValueError("La altura no puede ser un número negativo")
		self._altura = altura

	@property
	def area(self):
		return self.base * self.altura / 2

t = Triangulo(4, 5)
print("Área:", t.area)

t.base = 10
print("Nuevo área", t.area)