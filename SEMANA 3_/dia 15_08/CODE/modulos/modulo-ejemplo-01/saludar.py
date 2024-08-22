#Existen dos maneras de importar
import modulo_saludar as mSalud
from modulo_saludar import saludar
# from modulo_saludar import * # No es una buena tecnica

import modulo_fuera.calcular_edad as calEdad
# CREACIÓN DE LA VARIABLE

variable_saludar = mSalud.saludar("Juan")
variable_edad=calEdad.calcularEdad(2004,2024)

print(variable_saludar)
print(variable_edad)





#Despedida
variable_saludar = mSalud.despedida("Juan")


#Calcular edad 
