# Calculadora de Propinas - Archivo Principal
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
    print("=== BIENVENIDO A LA CALCULADORA DE PROPINAS ===")
    print("Calculadora que te ayuda a calcular propinas y pagos por comensal.\n")

    # Paso 1: Total cuenta
    total = pedir_cuenta_total()
    print(f"Ha introducido: {total:.2f} €\n")

    # Paso 2: Comensales (validado)
    while True:
        try:
            comensales = int(input("¿Cuántos comensales son? "))
            if comensales > 0:
                break
            print("Debe ser mayor que 0")
        except ValueError:
            print("Ingrese un número válido")

    # Paso 3: Porcentaje propina (validado)
    while True:
        try:
            porcentaje = float(input("¿Qué porcentaje de propina desea dejar? "))
            if 0 <= porcentaje <= 100:
                break
            print("Debe estar entre 0 y 100")
        except ValueError:
            print("Ingrese un número válido")

    # Cálculos
    propina_total = Calcular_propina(total, porcentaje)
    total_a_pagar = total + propina_total
    pago_por_comensal = Dividir_cuenta(total_a_pagar, comensales)

    # Resultados formateados
    print("\n" + "="*50)
    print(f"RESULTADOS:")
    print(f"Propina total:      {propina_total:.2f} €")
    print(f"Total a pagar:      {total_a_pagar:.2f} €")
    print(f"Pago por comensal:  {pago_por_comensal:.2f} €")
    print("="*50)

if __name__ == "__main__":
    main()
