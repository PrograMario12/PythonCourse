def suma(*args):
	num = 0;
	for agr in args:
		num += arg

	return num

def producto(*args):
	num = 1
	for arg in args:
		num *= arg
	return num

OPERACIONES = {
	"suma": suma,
	"producto": producto,
}

def operacion(*args, **kwargs):
	return operaciones.get(kwargs.get("operacion"))(*args)