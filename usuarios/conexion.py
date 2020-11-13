import mysql
import mysql.connector
"""
Creo este modulo para no tener que repetir codigo.
De ahora en más sólo tengo que importar el modulo.
"""
def conectar():
    database = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "",
        database = "proyectopython1",
        port = 3306
    )

    # print(database) compruebo la conexion

    cursor = database.cursor(buffered=True)

    return [database, cursor]