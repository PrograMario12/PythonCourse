'Creamos la lista e imprimimos el tipo que es la variable'
lista = [1,2,3,4,5]
print(type(lista))

'Con append añadimos valores al final de la lista'
lista.append(lista[2])
print(lista)

'''Con pop eliminamos el último elemento de la lista
pero si le pasamos un parámetro elimina el elemento
indicado, index sirve para buscar en que posicón está
determinado elemento'''
lista.pop(lista.index(3))
print(lista)