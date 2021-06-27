'''Cree un programa que almacene en variables los 
conjuntos {1,5,7,3,4,2} y {1,4,9,15,21} e indique:
a. La intersección entre ambas variables (valores que se
encuentran en ambas variables).
b. Los valores que se encuentran en cualquiera de los 
dos conjuntos pero no en ambos a la vez.'''

conjunto_1 = {1,5,7,3,4,2}
conjunto_2 = {1,4,9,15,21}

print(conjunto_1&conjunto_2)
print(conjunto_1^conjunto_2)