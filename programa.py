import mysql
from usuarios import acciones # Importo modulos desde paquete
from usuarios import usuario # Importo modulos desde paquete


print("""
Acciones disponibles
        - Registro
        - Login
""")

hazEl = acciones.Acciones() # Instancio mi clase
accion = input("¡Bievenido! ¿Qué quieres hacer?\n")

if accion=="Registro":
    hazEl.registro() # Invoco método
elif accion == "Login":
    hazEl.login() # Invoco método
