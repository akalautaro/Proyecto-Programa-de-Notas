import usuarios.conexion as conexion

# Instancio los elementos de la funcion que conecta a la DB 
connect = conexion.conectar() 
database = connect[0] # Conexion a la base de datos
cursor = connect[1]

class Nota:

    def __init__(self, usuario_id, titulo, contenido):
        self.usuario_id = usuario_id
        self.titulo = titulo
        self.contenido = contenido
    
    def guardar(self):
        sql = "INSERT INTO notas VALUES(null, %s, %s, %s, NOW())"
        nota = (self.usuario_id, self.titulo,self.contenido)

        cursor.execute(sql, nota)
        database.commit()

        return (cursor.rowcount, self)

    def listar(self):
        sql = f"SELECT * FROM notas WHERE usuario_id = {self.usuario_id}"

        cursor.execute(sql)
        result = cursor.fetchall()

        return result

    def eliminar(self):
        sql = f"DELETE FROM notas WHERE usuario_id = {self.usuario_id} AND titulo = {self.titulo}" # Si uso AND titulo LIKE '%titulo%' borro donde está contenido el título
        # nota = (self.usuario_id, self.titulo)

        cursor.execute(sql)
        database.commit()

        return (cursor.rowcount, self)