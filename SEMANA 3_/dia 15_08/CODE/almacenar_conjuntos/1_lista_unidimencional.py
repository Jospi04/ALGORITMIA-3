# Lista (array) unidimencional - números enteros
listNumeros = [1,2,3,4,20,6,7,8,9,10,]
# Creacion de variables
suma = 0
mayorNumero = listNumeros[0]

# Bucle for - Para encontrar el mayor número
for varNumero in listNumeros:
    suma += varNumero
    if varNumero > mayorNumero:
        mayorNumero = varNumero

print("El número mayor es :", mayorNumero)
print("La duma total es : ", suma)