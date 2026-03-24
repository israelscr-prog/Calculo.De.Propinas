# debug.py
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    import src.Funciones_Calculadora
    print("✅ Módulo importado OK")
    print("Funciones disponibles:")
    import inspect
    functions = [name for name, obj in inspect.getmembers(src.Funciones_Calculadora) if inspect.isfunction(obj)]
    print(functions)
except Exception as e:
    print("❌ Error:", e)
