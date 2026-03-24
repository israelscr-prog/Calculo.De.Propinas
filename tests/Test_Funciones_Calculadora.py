
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.Funciones_Calculadora import (
    Calcular_10_por_ciento,
    Calcular_propina,
    Dividir_cuenta,
    pedir_cuenta_total
    )


#Test ejemplo de la Función 1
cantidad = 100
resultado = Calcular_10_por_ciento(cantidad)
print(f"Ejemplos:Test 1: 10% de {cantidad} es {resultado}") 

#Test 2 de función 1
cantidad = float(input("Test N2: Ingrese una cantidad: "))
resultado = Calcular_10_por_ciento(cantidad)
print(f"El 10% de {cantidad} es {resultado}")  

#Test 1 de la Función 2
cuenta = 100
porcentaje = 15
resultado = Calcular_propina(cuenta, porcentaje)
print(f"La propina de {cuenta} con un {porcentaje}% es {resultado}")

#Test 1 de la Función 3
print("Prueba de pedir_cuenta_total()")
total = pedir_cuenta_total()
print("Valor devuelto por la función:", total)