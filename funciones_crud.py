import psycopg2
from conexiondb import conexion

##Función para el MENU PRINCIPAL
def menu ():
    
    print("        **** BIENVENIDO ****        ")
    print("1. Ingresar Curso ")
    print("2. Ver todos los cursos")
    print("3. Eliminar registro")

##FUNCION INSERTAR DATOS
def insertar ():
    try:
        with conexion.cursor() as cursor:
            nombre=str(input("Ingrese Curso: "))
            consulta = "INSERT INTO materias (nombrecurso) VALUES (%s); "
            cursor.execute(consulta,[nombre])
            conexion.commit() #Se usa Commit para guardar los cambios Realizados
    except psycopg2.Error as e:
        print("Ocurrio un Error en Insertar: ", e)
    finally:
        conexion.close()  #Cerramos la conexión
       

#FUNCIÓN LISTAR DATOS
def listar ():
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM materias; ")
            query_result=cursor.fetchall()  
            print(query_result)
    except psycopg2.Error as e:
        print("Ocurrio un Error en Listar ", e)
    finally:
        conexion.close()
       

#FUNCION ELIMINAR DATOS
def eliminar ():
    try:
        with conexion.cursor() as cursor:
            codigo=str(input("Ingrese Curso: "))
            consulta = "DELETE FROM materias WHERE nombrecurso = %s; "
            cursor.execute(consulta,[codigo])
            conexion.commit()
    except psycopg2.Error as e:
        print("Ocurrio un Error en Eliminar ", e)
    finally:
        conexion.close()