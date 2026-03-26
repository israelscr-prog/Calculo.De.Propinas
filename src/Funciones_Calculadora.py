"""Módulo con funciones para calculadora de propinas."""

import os

def limpiar_pantalla():
    """Limpia la consola en Windows, Linux o Mac."""
    os.system("cls" if os.name == "nt" else "clear")

def Calcular_10_por_ciento(cantidad: float) -> float:
    """Calcula el 10% de una cantidad."""
    return cantidad * 0.10

def Calcular_propina(cuenta: float, porcentaje: float) -> float:
    """Calcula propina según porcentaje de la cuenta."""
    return cuenta * (porcentaje / 100)

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
