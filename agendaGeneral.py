import csv
from tabulate import tabulate


## Con esta función leemos el archivo CSV el cual esta almacenado todos los datos de la agenda los cuales están en forma
## de diccionario.


def leer_archivo():
    file = open(f"Bd/Agenda.csv", "r")
    return list(csv.DictReader(file))

## Con esta función actualizamos los datos de la agenda en el archivo CSV.

def actualizar_agenda(lista_agenda):
    file = open(f"Bd/Agenda.csv", "w", newline="")
    encabezados = list(lista_agenda[0].keys())
    escritor = csv.DictWriter(file, encabezados)
    escritor.writeheader()
    escritor.writerows(lista_agenda)
    file.close()



## Con esta función hacemos varias cosas: la primera es  que si el nombre que estamos buscando y que está incluido
## en la variable buscar_nom coincide con algún valor de la clave nombre del diccionario nos da la posición y nos arroja
## el valor del Correo, Teléfono y Edad del respectivo nombre, si el nombre no está en el diccionario el for arrojara
## el valor del tamaño de la lista agenda + 1 para poder hacer una comparación.



def buscar_contacto_posicion(agenda):
    buscar_nom = (input("Ingrese el nombre del contacto que desea buscar: ").capitalize())
    print()
    for i in range(len(agenda)):
        if (agenda[i]["nombre"]) == buscar_nom:
            lista = [ ["correo: ", agenda[i]["correo"]],
                      ["telefono: ", agenda[i]["telefono"]],
                      ["edad: ", agenda[i]["edad"]]
            ]
            print(tabulate(lista, headers=["Item", "Datos" ],tablefmt="fancy_grid"))
            contador = i
            return contador
    return len(agenda)+1
print()




## Función para agregar contacto:

## En esta función el programa pide los datos requeridos para ingresar un contacto nuevo a la agenda.


def agregar_contacto():

    ## llamamos a la funcion Leer_archivo
    agenda = leer_archivo()


    print("AGREGAR CONTACTO \n")

    print("Ingrese los datos pedidos de su nuevo contacto \n")

    while True:

        ## Vamos a ingresar los datos a la agenda por medio de un diccionario llamado datos.

        datos = {
            "nombre": input("Ingrese el nombre completo: ").capitalize(),
            "correo": input("Ingrese el correo electrónico: "),
            "telefono": input("Ingrese el número de teléfono: "),
            "edad": input("Ingrese la edad: ")
        }

        ## se agregara los valos ingresados al diccionario en la lista de diccionarios.

        agenda.append(datos)

        ## Llamamos a la funcion actualizar_agenda para que escribier el ultimo diccionario ingresado en el archivo CSV.

        actualizar_agenda(agenda)

        ## Preguntamos si desea ingresar mas contactos en caso de que no se sale del bucle

        respuesta = input("Desea ingresar mas contactos. responda S/N: ").upper()
        if respuesta != "S":
            break

## Funcion para la seccion buscar contacto

## En esta funcion se ingresa el nombre y el sisitema devuelve todos los datos que estan en la agenda.
# Si el nombre no es encontrado devuelve el mensaje "Este contacto no existe"

def buscar_contacto():
    while True:
        ## llamamos a la función Leer_archivo.

        agenda = leer_archivo()

        print("BUSCAR CONTACTO \n")

        ## Llamamos la función buscar_contacto_posicion y la incluimos en una variable para poder trabajar solo
        ## con la variable i

        i = buscar_contacto_posicion(agenda)

        ## Si se ingresa un nombre que no existe en la lista agenda la función devuelve un valor en la variable que es
        ## mayor que el tamaño de la lista. Si es así saca el mensaje "Este contacto no existe"

        if i > len(agenda):
            print("Este contacto no existe")

        ## Preguntamos si desea buscar más contactos en caso de que no se sale del bucle

        print()
        respuesta = input("Desea buscar mas contactos. responda S/N: ").upper()
        if respuesta != "S":
            break

## Función para la sección modificar contacto

## en esta función se busca el contacto que se quiere modificar por el nombre, si se acepta seguir con el proceso
## el sistema pedirá todos los datos nuevamente.


def modificar_contacto():

    ## llamamos a la función Leer_archivo

    agenda = leer_archivo()


    print("MODIFICAR CONTACTO \n")

    ## Llamamos la función buscar_contacto_posicion y la incluimos en una variable para poder trabajar solo
    ## con la variable i

    i = buscar_contacto_posicion(agenda)

    ## Si se ingresa un nombre que no existe en la lista agenda la función devuelve un valor en la variable que es
    ## mayor que el tamaño de la lista. Si es así saca el mensaje "Este contacto no existe"

    if i > len(agenda):
        print("Este contacto no existe")
    else:
        preguntar = input(f"Realmente desea cambiar los datos del contacto {agenda[i]['nombre']}. Responder S/N").upper()

        if preguntar == "S":

            ## En este punto el programa dependiendo del valor i y su clave pide la modificación del valor en el
            ## diccionario y de esta manera se actualiza el contacto.

            agenda[i]["correo"] = input("Ingrese el nuevo correo: ")
            agenda[i]["telefono"] = input("Ingrese el nuevo número de teléfono: ")
            agenda[i]["edad"] = input("Ingrese la nueva edad: ")

            ## También dependiendo del valor de i el sistema busca la posición y reescribe los valores.

            file = open(f"Bd/Agenda.csv", "w", newline="")
            encabezados = list(agenda[i].keys())
            escritor = csv.DictWriter(file, encabezados)
            escritor.writeheader()
            escritor.writerows(agenda)
            file.close()

        else:
            print("No esta seguro")


## Función para eliminar contacto

## Con esta función se busca el contacto por el nombre y si se desea se borrara del archivo CSV.


def eliminar_contacto():

    ## llamamos a la función Leer_archivo.

    agenda = leer_archivo()


    print("ELIMINAR CONTACTO \n")

    ## Llamamos la función buscar_contacto_posicion y la incluimos en una variable para poder trabajar solo
    ## con la variable i

    i = buscar_contacto_posicion(agenda)

    if i > len(agenda):
        print("Este contacto no existe")
    else:
        preguntar = input(f"Realmente desea eliminar los datos de este contacto {agenda[i]['nombre']}. Responder S/N").upper()

        if preguntar == "S":

            ## Según el valor de i el sistema ubica el diccionario dentro de la lista y lo borra, desplazando
            ## todos los demás diccionarios una posición hacia atrás.

            del agenda[i]

            ## También dependiendo del valor de i el sistema busca la posición y reescribe los valores.
            file = open(f"Bd/Agenda.csv", "w", newline="")
            encabezados = list(agenda[i].keys())
            escritor = csv.DictWriter(file, encabezados)
            escritor.writeheader()
            escritor.writerows(agenda)
            file.close()

        else:
            print("no esta seguro")



## Función para imprimir agenda

## Con esta función se muestra todos los datos de la agenda.


def imprimir_agenda():

    ## llamamos a la función Leer_archivo.

    agenda = leer_archivo()

    ## esta funcion es para imprimir la totalidad de la agenda con la libreria tabulate.
    print(tabulate(agenda, headers="keys", tablefmt="fancy_grid", showindex=True))


while True:
    print("\n ¿Que desea hacer? para elegir una opcion escriba el numero que corresponda. \n")
    print("1. Agregar contacto.")
    print("2. Buscar contacto.")
    print("3. Modificar contacto.")
    print("4. Eliminar contacto.")
    print("5. Imprimir agenda.")
    print("6. Salir.")
    respuesta = input()
    print()
    if respuesta == "1":
        agregar_contacto()
    elif respuesta == "2":
        buscar_contacto()
    elif respuesta == "3":
        modificar_contacto()
    elif respuesta == "4":
        eliminar_contacto()
    elif respuesta == "5":
        imprimir_agenda()
    elif respuesta == "6":
        break
    else:
        print("Ingrese una opcion valida.")