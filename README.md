# 🧾 Calculadora de Propinas

Aplicación de consola en Python para calcular propinas y dividir cuentas entre comensales de forma sencilla, rápida e interactiva.

---

## 🚀 Características

* ✅ Cálculo de propina por porcentaje
* ✅ Propina con monto fijo
* ✅ División automática de cuenta entre múltiples personas
* ✅ Validación de entradas (evita errores comunes)
* ✅ Interfaz interactiva en consola
* ✅ Compatible con Windows, Linux y macOS

---

## 📂 Estructura del Proyecto

```
📦 calculadora-propinas
├── src/
│   └── Funciones_Calculadora.py
├── main.py
└── README.md
```

---

## 🛠️ Tecnologías utilizadas

* 🐍 Python 3.10+
* 📦 Librerías estándar (`os`, `sys`)

---

## ⚙️ Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/tu-usuario/calculadora-propinas.git
cd calculadora-propinas
```

2. Ejecuta el programa:

```bash
python main.py
```

---

## 🧑‍💻 Uso

Al iniciar la aplicación verás un menú interactivo:

```
1. 🧾 Nueva cuenta (Porcentaje o Fija)
2. 💰 Solo dividir cuenta
3. 🚪 Salir
```

### 🔹 Opción 1: Nueva cuenta

Permite:

* Introducir el total de la cuenta
* Elegir tipo de propina:

  * Porcentaje (%)
  * Monto fijo ($)
* Dividir entre comensales

📌 Ejemplo:

```
Total cuenta: 100
Comensales: 4
Propina: 15%

Resultado:
Cada persona paga: 28.75
```

---

### 🔹 Opción 2: Solo dividir cuenta

Divide el total sin aplicar propina.

📌 Ejemplo:

```
Cuenta: 80
Personas: 4

Resultado:
Cada uno paga: 20
```

---

## 🧠 Funciones principales

### 📌 `Calcular_propina_en_porcentaje(cuenta, porcentaje)`

Calcula la propina basada en un porcentaje.

### 📌 `Calcular_propina_fija(monto_fijo)`

Devuelve una propina fija definida por el usuario.

### 📌 `Dividir_cuenta(cuenta, numero_personas)`

Divide el total entre los comensales.

### 📌 `menu_propina()`

Permite elegir el tipo de propina de forma interactiva.

### 📌 `pedir_cuenta_total()`

Solicita y valida el total de la cuenta.

### 📌 `limpiar_pantalla()`

Limpia la consola según el sistema operativo.

---

## 🔒 Validaciones implementadas

* ❌ Evita números negativos o inválidos
* ❌ Control de errores (`ValueError`)
* ❌ Número de comensales debe ser mayor que 0
* ❌ Porcentaje entre 0 y 100

---

## 💡 Mejoras futuras

* 🌐 Interfaz gráfica (Tkinter / Web)
* 💾 Guardar historial de cuentas
* 🌍 Soporte multi-moneda
* 📱 Versión móvil
* 🧪 Tests automatizados

---

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas!

1. Haz un fork del proyecto
2. Crea una rama (`git checkout -b feature/nueva-feature`)
3. Haz commit (`git commit -m 'Añadir nueva feature'`)
4. Haz push (`git push origin feature/nueva-feature`)
5. Abre un Pull Request

---

## 📄 Licencia

Este proyecto está bajo la licencia MIT.

---

## 👨‍💻 Autor

Desarrollado por Isra NEW DEVELOPER inc. 

---

⭐ Si te gusta este proyecto, ¡dale una estrella en GitHub!

DALE UN LIKE, COMENTARIO Y SUBCRIBETE ;D  
