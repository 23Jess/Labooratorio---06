#Calcular la diferencia simétrica entre 2 conjuntos

conjuntoA=set() #Creamos un conjunto vacío para el primer conjunto
numElementA= int(input("Ingrese la cantidad de elementos del conjunto A= ")) #se ingresa la cantidad de elemntos que va a tener el conjunto A
for i in range (numElementA):
    elemento = int(input("Ingrese los elementos del conjunto A: ")) #Se ingresa los elementos para el conjunto A de tipo (int)
    conjuntoA.add(elemento)

conjuntoB = set() #Creamos un conjunto vacío para el segundo conjunto
numElementB= int(input("Ingrese la cantidad de elementos del conjunto B= ")) #se ingresa la cantidad de elemntos que va a tener el conjunto B
for j in range (numElementB):
    elemento = int(input("Ingrese los elementos del conjunto B: ")) #Se ingresa los elementos para el conjunto B de tipo (int)
    conjuntoB.add(elemento) #Cada elemento se va agregando
print("Número de elementos de A es: ",len(conjuntoA))
print("Número de elementos de B es: ",len(conjuntoB))

print("conjuntoA= ", conjuntoA)
print("conjuntoB= ", conjuntoB)

print("Diferencia simétrica")
diferencia_simetrica= conjuntoA.symmetric_difference(conjuntoB)
print("A ⊕ B = ", diferencia_simetrica)