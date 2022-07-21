from Database import Database
import os
db=Database()
def listarpropiedades():

    evaluacin3=db.Listarpropiedades()
   
    for m in evaluacin3:
      
       print("* id-> {}".format(m[0]))
       print("* direccion-> {}".format(m[1]))
       print("* comuna-> {}".format(m[2]))
       print("* valor-> {}".format(m[3]))
       print("**************************")


def listarpropiedadescomuna():
    comuna=input("ingrese comuna \t")
    lcomunas=db.Listarpropiedadescomuna(comuna)

    if db.buscarpropiedadescomuna(comuna):
        for m in lcomunas:
            print("* id-> {}".format(m[0]))
            print("* direccion-> {}".format(m[1]))
            print("* comuna-> {}".format(m[2]))
            print("* valor-> {}".format(m[3]))
            print("**************************")

    else:
        print("no hay comuna")


def agregarpropiedades():
    id=int(input("Ingrese id \t"))
    if db.buscarpropiedades(id):
        print("Ya existe en la BD \t")
    else:
        direccion=(input("Ingrese direccion \t"))
        comuna=(input("Ingrese comuna \t"))
        valor=float(input("Ingrese valor \t"))
        db.Agregarpropiedades(id,direccion,comuna,valor)
        print("Agregado a la BD")

def eliminarpropiedades():
    id=int(input("Ingrese id a eliminar \t"))
    if db.buscarpropiedades(id):
        db.eliminarPropiedades(id)
        print("eliminado de la BD")
    else:
        print("no existe en la BD \t")

def actualizarpropiedades():
    id=int(input("Ingrese id de propiedad a actualizar \t"))
    if db.buscarpropiedades(id):
        direccion=(input("Ingrese direccion \t"))
        comuna=(input("Ingrese comuna \t"))
        valor=float(input("Ingrese valor \t"))
        db.actualizarpropiedades(id,direccion,comuna,valor)
        print("Agregado a la BD")
    else:
        print("no existe en la BD \t")


def default():
    print("No existe esa opcion")

def promedio():
    pro=db.promedio()
    for b in pro:
        print("promedio-> {}".format(b[0]))

respuesta="si"
switch={1:listarpropiedades, 2:agregarpropiedades, 3:eliminarpropiedades, 4:actualizarpropiedades, 5:listarpropiedadescomuna, 6:promedio}

while respuesta=="si":
    print("******************************************************************")
    print("*    opcion 1: Listar propiedades                                *")
    print("*    opcion 2: Agregar propiedades                               *")
    print("*    opcion 3: eliminar propiedades                              *")
    print("*    opcion 4: actualizar propiedades                            *")
    print("*    opcion 5: buscar propiedad por comuna                       *")
    print("*    opcion 6: Mostrar el promedio del valor de las propiedades  *")
    print("******************************************************************")
    x=int(input("Seleccione su opcion \t"))
    switch.get(x,default)()
    respuesta=input("\n Desea continuar si/no \t")
    os.system("cls")