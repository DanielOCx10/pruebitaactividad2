#ejemplo de lista
compras = ["pan", "leche", "huevos"]
print("lista original",compras)

#Modificar un elemento 
compras[1] = "jugo"

# Agregar nuevo elemento
compras.append("café")

print("lista modificada: ",compras)

print(" --------- -----------")

#ejemplo de tupla con coordenadas
coordenadas = (10, 20)
#Intentar modificarla produciría un error
#coordenadas[0] = 5  NO está permitido

print("ejemplo de tupla:", coordenadas)
