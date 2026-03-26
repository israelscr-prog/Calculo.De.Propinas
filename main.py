# Calculadora de Propinas - Archivo Principal
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.Funciones_Calculadora import (
    limpiar_pantalla,
    Calcular_propina_en_porcentaje,
    Calcular_propina_fija,
    menu_propina,
    Dividir_cuenta,
    pedir_cuenta_total,
    )

def main():
    """Función principal con opción de reinicio."""
    while True:
        limpiar_pantalla()
        print("\n" + "="*66)
        print("===================== CALCULADORA DE PROPINAS ====================\n")
        print("Calculadora que te ayuda a calcular propinas y pagos por comensal.\n")
        print("="*66)

        # Paso 1: Total cuenta
        total = pedir_cuenta_total()
        print(f"Ha introducido: ${total:.2f} \n")

        # Paso 2: Comensales (validado)
        while True:
            try:
                comensales = int(input("¿Cuántos comensales son? "))
                if comensales > 0:
                    break
                print("Debe ser mayor que 0")
            except ValueError:
                print("Ingrese un número válido")

        # PASO 3: CAMBIADO → Menú en lugar de solo porcentaje
        propina_tipo, valor_propina = menu_propina()
        
        # Cálculo según tipo 
        if propina_tipo == "porcentaje":
            propina_total = Calcular_propina_en_porcentaje(total, valor_propina)
        else:  # fija
            propina_total = Calcular_propina_fija(valor_propina)

        # Cálculos
        propina_total = Calcular_propina_en_porcentaje(total, valor_propina)
        total_a_pagar = total + propina_total
        pago_por_comensal = Dividir_cuenta(total_a_pagar, comensales)

        # Resultados
        print("\n" + "="*50)
        print("RESULTADOS:")
        print(f"Cuenta original:     ${total:.2f} ")
        print(f"Propina total:       ${propina_total:.2f} ")
        print(f"Total a pagar:       ${total_a_pagar:.2f} ")
        print(f"Pago por comensal:   ${pago_por_comensal:.2f}")
        print("="*60)

        # ¿Reiniciar?
        while True:
            opcion = input("\n¿Borrar y calcular de nuevo? (s/n): ").strip().lower()
            if opcion in ["s", "si", "y", "yes"]:
                break  # Reinicia el bucle principal
            elif opcion in ["n", "no"]:
                print("\n¡Gracias por usar mi funcion de calcular precio de un restaurante! 👋")
                return  # Sale del programa
            else:
                print("Escribe 's' para sí o 'n' para no")

if __name__ == "__main__":
    main()
