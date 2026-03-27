"""Módulo con funciones para calculadora de propinas."""

import os

def limpiar_pantalla():
    """Limpia la consola en Windows."""
    os.system("cls" if os.name == "nt" else "clear")

def Calcular_10_por_ciento(cantidad: float) -> float:
    """Calcula el 10% de una cantidad."""
    return cantidad * 0.10

def Calcular_propina_en_porcentaje(cuenta: float, porcentaje: float) -> float:
    """Calcula propina según porcentaje de la cuenta."""
    return cuenta * (porcentaje / 100)

def Calcular_propina_fija(monto_fijo: float) -> float:
    """Propina con monto fijo."""
    return monto_fijo

def menu_propina():
    """Menú para elegir porcentaje o monto fijo."""
    print("\n🧾 TIPO DE PROPINA:")
    print("1. Porcentaje (%)")
    print("2. Monto fijo ($)")
    opcion = input("Elige (1 o 2): ").strip()
    
    if opcion == "1":
        while True:
            try:
                valor = float(input("¿Qué porcentaje? (ej: 15): "))
                if 0 <= valor <= 100:
                    return "porcentaje", valor
                print("Debe estar entre 0 y 100")
            except ValueError:
                print("Ingrese un número válido")
    elif opcion == "2":
        while True:
            try:
                valor = float(input("¿Monto fijo propina? (ej: 20): "))
                return "fija", valor
            except ValueError:
                print("Ingrese un número válido")
    else:
        print("Usando porcentaje 15% por defecto.")
        return "porcentaje", 15.0

def pedir_cuenta_total(cuenta_input: str | None = None) -> float:
    """Pide o convierte total de cuenta a float."""
    if cuenta_input is None:
        cuenta_input = input("Introduce el total de la cuenta: ")
    try:
        return float(cuenta_input)
    except ValueError:
        raise ValueError("El total debe ser un número válido.")

def Dividir_cuenta(cuenta: float, numero_personas: int) -> float:
    """Divide cuenta entre número de personas."""
    if numero_personas <= 0:
        raise ValueError("El número de personas debe ser mayor que cero.")
    return cuenta / numero_personas
