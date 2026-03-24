# Funciones para la calculadora de propinas
cantidad = 100
# Función Numero 1: calcular el 10% de una cantidad
def Calcular_10_por_ciento(cantidad):
    return cantidad * 0.10

#Funcion Número 2: Calcular Propinas
def Calcular_propina(cuenta, porcentaje):
    return cuenta * (porcentaje / 100)

#Funcion Número 3: Pedir el total de la cuenta
def pedir_cuenta_total(cantidad, cuenta):
    total = float(input("Introduce el total de la cuenta: "))
    return total

#Funcion Número 4: Dividir la cuenta entre el número de personas
def Dividir_cuenta(cuenta, numero_personas):
    if numero_personas <= 0:
        raise ValueError("El número de personas debe ser mayor que cero.")
    return cuenta / numero_personas

