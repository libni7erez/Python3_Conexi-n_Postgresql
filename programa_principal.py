import psycopg2
import funciones_crud

##Se crea la Función Principal
def main (): 
    funciones_crud.menu ()
    ingreso=input("Ingrese Opción: ")
    opcion=int(ingreso)

    ##Lo que hacemos acá es llevar al usuario a la acción que quiere realizar segun lo que digite desde teclado
    if opcion == 1:
        funciones_crud.insertar()
     
    elif opcion == 2:
        funciones_crud.listar()
    elif opcion == 3:
           funciones_crud.eliminar()
    else:
        print("Error....")


#LLamada a la Funcion del PROGRAMA PRINCIPAL
main()




            
                    


