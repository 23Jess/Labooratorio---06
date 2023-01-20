#Realizar operaciones de unión, intersección y diferencia de conjuntos

grupo_a = set(['Rosario', 'Fernando', 'Carlos', 'María'])
grupo_b = set(['Rosario', 'Pedro', 'Carlos', 'Antonio'])

#Unión de conjuntos
print('Unión de conjuntos: ')
union = grupo_a.union(grupo_b)
print(union)

#intersección de conjuntos
print('Intersección de los conjuntos: ')
interseccion = grupo_a.intersection(grupo_b)
print(interseccion)
print()

#diferencia de conjuntos
print('Diferencia de los conjuntos (grupo_a - grupo_b)')
diferencia1 = grupo_a.difference(grupo_b)
diferencia2 = grupo_b.difference(grupo_a)
print(diferencia1)
print()
print('Diferencia de los conjuntos (grupo_b - grupo_a)')
print(diferencia2)


