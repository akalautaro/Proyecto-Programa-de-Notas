from usuarios import usuario as modelo
import notas.acciones
"""
Agregar en el registro función que verifique si ya 
existe usuario con ese mail.
"""

class Acciones:
    
    def registro(self):
        print("\nVamos a registrarte en el sistema: ")

        nombre = input("Introduzca su nombre: ")
        apellido = input("Introduzca su apellido: ")
        email = input("Introduzca su email: ")
        password = input("Introduzca su contraseña: ")

        usuario = modelo.Usuario(nombre,apellido,email,password)
        registro = usuario.registrar()

        if registro[0]>=1:
            print(f"\nPerfecto {registro[1].nombre}, el registro ha sido exitoso!")

        else:
            print("\nNo te has registrado correctamente")

    def login(self):
        print("\nIdentificate en el sistema: ")
        
        try:
            email = input("Introduzca su email: ")
            password = input("Introduzca su contraseña: ")

            usuario = modelo.Usuario('','',email, password)
            login = usuario.identificar()

            if email == login[3]:
                print(f"\nBienvenido {login[1]}!")
            self.proximasAcciones(login)

        except Exception as e:
            # print(type(e))
            # print(type(e).__name__)
            print(f"Credenciales incorrectas")

    def proximasAcciones(self, usuario):
        
        print("""
            Acciones disponiles:
        - Crear nota (Crear)
        - Mostrar notas (Mostrar)
        - Eliminar nota (Eliminar)
        - Salir (Salir)
        """)

        accion = input("¿Qué quieres hacer?: ")
        hazEl = notas.acciones.Acciones() # Llamo a los metodos y a la clase, para poder crear el objeto

        if accion == "Crear":
            # print("\nVamos a crear una nota")

            hazEl.crear(usuario)
            self.proximasAcciones(usuario)

        elif accion == "Mostrar":

            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)

        elif accion == "Eliminar":

            hazEl.borrar(usuario)
            self.proximasAcciones(usuario)

        elif accion == "Salir":
            print(f"\nHasta pronto, {usuario[1]}!")
            exit()

        