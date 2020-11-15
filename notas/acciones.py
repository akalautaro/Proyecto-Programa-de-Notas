from notas import nota as modelo

class Acciones:

    def crear(self, usuario):
        print(f"\nOk, {usuario[1]}, vamos a crear una nueva nota: ")

        titulo = input("Introduce el titulo de tu nota: ")
        contenido = input("Escribe tu nota: ")

        nota = modelo.Nota(usuario[0], titulo, contenido)
        guardar = nota.guardar()

        if guardar[0] >= 0:
            print(f"Perfecto, guardaste la nota: {nota.titulo}")

        else:
            print(f"No se ha guardado la nota, lo siento {usuario[1]}")

    def mostrar(self, usuario):
        print(f"\n{usuario[1]}, éstas son tus notas: \n")

        nota = modelo.Nota(usuario[0],"","")
        notas = nota.listar()

        for nota in notas:
            print("----------------------------------------------------------------------------")
            print(f"Titulo: {nota[2]}")
            print(f"Contenido: {nota[3]}")
            print(f"Fecha de creación: {nota[4]}")
        print("----------------------------------------------------------------------------")

    def borrar(self, usuario):
        print(f"\nOk, {usuario[1]}, vamos a borrar notas")

        titulo = input("Introduce el titulo de la nota que quieres borrar: ")

        # nota = modelo.Nota(usuario[0], titulo)
        nota = modelo.Nota(usuario[0], titulo,'')
        eliminar = nota.eliminar()

        if eliminar[0]>=1:
            print(f"Hemos borrado la nota: {nota.titulo}")

        else:
            print(f"No se ha borrado la nota, prueba luego.")

