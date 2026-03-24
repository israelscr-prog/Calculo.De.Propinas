#Calculadora de Propinas - Archivo Principal

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.Funciones_Calculadora import (
    Calcular_propina,
    Dividir_cuenta,
    pedir_cuenta_total
    )
def main():
    """Función principal de la calculadora de propinas."""
    print("=== CALCULADORA DE PROPINAS ===")

# Paso 1: Pedir total de la cuenta
Cuenta_total = pedir_cuenta_total()

# PASO 2: ¿Cuántos comensales son?
print("\nPASO 2: Número de comensales")
comensales = int(input("¿Cuántos comensales son? "))