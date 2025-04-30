import mariadb


def conectar_y_consultar():
    try:
        #establecer conexion a la bdd
        conexion = mariadb.connect(
            #host="192.168.0.6,
            host="localhost",
            database="almacen",
            user="root",
            password="",
            port=3306
        )
        print(type(conexion))
        print("Conexion a la base de datos del servidor ounus")

        #crear un cursos y ejecutar la consulta
        cursor = conexion.cursor()
        consulta = "select * from usuarios"         #Consulta tabla usuarios
        cursor.execute(consulta)
        #recuperar y mostrar resultados
        resultados = cursor.fetchall()
        print("Resultado", type(resultados))
        print("Datos en la tabla usuarios")
        for fila in resultados:
            #print(fila)
            print(f"ID: {fila[0]}, Nombre de usuario: {fila[2]}, Correo: {fila[3]}, Contrasena: {fila[4]}, Id_Rol: {fila[1]}")

        consulta = "select * from roles"         #Consulta tabla roles
        cursor.execute(consulta)
        # recuperar y mostrar resultados
        resultados = cursor.fetchall()
        print("Resultado", type(resultados))
        print("Datos en la tabla roles")
        for fila in resultados:
            # print(fila)
            print(f"ID: {fila[0]}, Nombre Rol: {fila[1]}")

        consulta = "select * from privilegios"  # Consulta tabla privilegios
        cursor.execute(consulta)
        # recuperar y mostrar resultados
        resultados = cursor.fetchall()
        print("Resultado", type(resultados))
        print("Datos en la tabla privilegios")
        for fila in resultados:
            # print(fila)
            print(f"ID: {fila[0]}, Titulo privilegio: {fila[1]}")

        consulta = "select * from roles_permisos"  # Consulta tabla roles_permisos
        cursor.execute(consulta)
        # recuperar y mostrar resultados
        resultados = cursor.fetchall()
        print("Resultado", type(resultados))
        print("Datos en la tabla permisos")
        for fila in resultados:
            # print(fila)
            print(f"ID Privilegio: {fila[0]}, Fecha de aignacion: {fila[2]}, Id_Rol: {fila[1]}")

    except mariadb.Error as e:
        print(f"Error al conectar con la base de datos: {e}")

    finally:
        #cerrar la conextion y el cursos si estan aabiertos
        if 'cursor' in locals() and cursor:
            cursor.close()
            print("Conexion cerrada.")

if __name__ == '__main__':
    conectar_y_consultar()

