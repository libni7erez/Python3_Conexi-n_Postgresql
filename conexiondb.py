##Acá se encuentran las credenciales para poder realizar la conexión al Gestor
##PostgreSql

import psycopg2

try:
    credenciales = {
        "host": "localhost",
         "port": 5432, #Agregamos el puerto en el que esta trabajando nuestro gestos
         "database": "Colegio", #Aquí va el Nombre de la Base de datos
         "user": "postgres",  #Aquí se agrega el nombre del Usuario 
         "password": "libniarmando" #Acá va la contraseña que le tenemos agregado a nuestro gestor
    }
    conexion = psycopg2.connect(**credenciales) #En esta parte realizamos la conexión.
    print("Conexión Exitosa")
except psycopg2.Error as e:
    print("A ocurrido un Error durante la Conexión: ",e )