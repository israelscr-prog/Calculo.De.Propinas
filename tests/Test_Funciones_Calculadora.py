#Funciones
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.Funciones_Calculadora import Calcular_10_por_ciento,Calcular_propina


#Test ejemplo de la Función 1
cantidad = 100
resultado = Calcular_10_por_ciento(cantidad)
print(f"Ejemplo de: 10% de {cantidad} es {resultado}") 

#Test 2
cantidad = float(input("Ingrese una cantidad: "))
resultado = Calcular_10_por_ciento(cantidad)
print(f"El 10% de {cantidad} es {resultado}")  

#Test 1 de la Función 2
cuenta = 100
porcentaje = 15
resultado = Calcular_propina(cuenta, porcentaje)
print(f"La propina de {cuenta} con un {porcentaje}% es {resultado}")