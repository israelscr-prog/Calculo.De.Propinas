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

def mostrar_menu_principal():
    """Menu principal del programa."""
    print("\n" + "="*66)
    print("===================== CALCULADORA DE PROPINAS ====================\n")
    print("Bienvenido a la Calculadora de Propinas que te ayuda a calcular propinas y pagos por comensal.\n")
    print("Selecciona una opción:")
    print("1. 🧾 Nueva cuenta (Porcentaje o Fija)")
    print("2. 💰 Solo dividir cuenta")
    print("3. 🚪 Salir")
    print("="*66)

def Calcular_completo():
    """Función principal para calcular propina y dividir cuenta."""
    # Paso 1: Total cuenta
    total = pedir_cuenta_total()
    print(f"Ha introducido: ${total:.2f} \n")

    # Paso 2: Comensales (validado)
    while True:
        try:
            comensales = int(input("¿Cuántos comensales son? "))
            if comensales > 0:
                break
            print("❌ Debe ser mayor que 0")
        except ValueError:
            print("❌ Ingrese un número válido")

    # PASO 3: CAMBIADO → Menú en lugar de solo porcentaje
        propina_tipo, valor_propina = menu_propina()
        
    # Paso 4: Cálculo según tipo 
    if propina_tipo == "porcentaje":
        propina_total = Calcular_propina_en_porcentaje(total, valor_propina)
    else:  # fija
        propina_total = Calcular_propina_fija(valor_propina)

    # Resultados
    total_a_pagar = total + propina_total
    pago_por_comensal = Dividir_cuenta(total_a_pagar, comensales)

    # Resultados
    print("\n" + "="*60)
    print("📊RESULTADOS:")
    print(f"Cuenta original:     ${total:.2f} ")
    print(f"Propina total: ({propina_tipo.title()}): ${propina_total:.2f}")
    print(f"Total a pagar:       ${total_a_pagar:.2f} ")
    print(f"Pago por comensal:   ${pago_por_comensal:.2f}")
    print("="*60)
    input("\nPresiona Enter para continuar...")

def solo_dividir():
    """Solo divide cuenta sin propina."""
    total = pedir_cuenta_total()
    while True:
        try:
            comensales = int(input("¿Cuántos comensales? "))
            if comensales > 0:
                break
            print("❌ Debe ser mayor que 0")
        except ValueError:
            print("❌ Número válido")
    
    resultado = Dividir_cuenta(total, comensales)
    print(f"\n✅ Cada comensal paga: ${resultado:.2f}")
    input("\nPresiona Enter para continuar...")

def main():
    """Menú principal interactivo."""
    while True:
        limpiar_pantalla()
        mostrar_menu_principal()
        
        opcion = input("→ Elige opción (1-3): ").strip()
        
        if opcion == "1":
            Calcular_completo()
        elif opcion == "2":
            solo_dividir()
        elif opcion == "3":
            print("\n👋 ¡Gracias por usar la calculadora!")
            break
        else:
            print("❌ Opción inválida. Presiona Enter...")
            input()

if __name__ == "__main__":
    main()

