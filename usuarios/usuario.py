from usuarios import conexion as conexion
import datetime
import hashlib

# Instancio los elementos de la funcion que conecta a la DB 
connect = conexion.conectar() 
database = connect[0]
cursor = connect[1]
class Usuario:

    def __init__(self, nombre, apellido, email, password):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.password = password
    
    def registrar(self):
        fecha = datetime.datetime.now()

        # Cifrar contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8')) # Para convertir tengo que pasarle valor en bytes, por eso encode, sino sería un stringvar
        
        sql = "INSERT INTO usuarios VALUES(null, %s, %s, %s, %s, %s)"
        usuario = (self.nombre, self.apellido, self.email, cifrado.hexdigest(), fecha) #hexdigest guarda el string hexadecimal que genero el cifrado

        try:
            cursor.execute(sql, usuario)
            database.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0, self]
        
        return result

    def identificar(self):
        
        # Consulta para comprobar si existe el usuario
        sql = "SELECT * from usuarios WHERE email = %s AND password = %s"

        # Cifrar contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8')) 

        # Datos para la consulta
        usuario = (self.email, cifrado.hexdigest())

        cursor.execute(sql, usuario)
        result = cursor.fetchone()

        return result