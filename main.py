
# Función 1 para calcular el 10% de una cantidad
def Calcular_10_por_ciento(cantidad):
    return cantidad * 0.10

#Testeo de la Función 1
cantidad = 78
resultado = Calcular_10_por_ciento(cantidad)
print(f"Ejemplo de: 10% de {cantidad} es {resultado}") 

#Test 2
cantidad = float(input("Ingrese una cantidad: "))
resultado = Calcular_10_por_ciento(cantidad)
print(f"El 10% de {cantidad} es {resultado}")  

