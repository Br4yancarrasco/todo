from requests.models import Response
from Database import Database
import os
db=Database()
def listartiquet():

    evaluacin4=db.listtiquet()
   
    for m in evaluacin4.json():
      
       print("* id-> {}".format(m["id"]))
       print("* sector-> {}".format(m["Sector"]))
       print("* asiento-> {}".format(m["Asiento"]))
       print("* tarifa-> {}".format(m["Tarifa"]))
       print("*********************************")

def listartiquetsector():
    sector=input("ingrese comuna a buscar \t")
    Response=db.listsector(sector)
    if db.buscarsector(sector):
        print("sector no existe en la BD \t")
    else:
        for m in Response.json():
            print("* id-> {}".format(m["id"]))
            print("* sector-> {}".format(m["Sector"]))
            print("* asiento-> {}".format(m["Asiento"]))
            print("* tarifa-> {}".format(m["Tarifa"]))
            print("*********************************")

def agregartiquet():
    id=int(input("Ingrese id \t"))
    sector=(input("Ingrese sector \t"))
    asiento=int(input("Ingrese asiento \t"))
    if db.buscartiquet(id,sector,asiento):
        print("id o sector y asiento ya existe en la BD \t")
    else:
        tarifa=int(input("Ingrese tarifa \t"))
        db.Agregartiquets(id,sector,asiento,tarifa)
        print("Agregado a la BD")


def default():
    print("No existe esa opcion")

def sumt():
    sum=db.suma()
    for b in sum.json():
        print("* suma-> {}".format(b["suma"]))

respuesta="si"
switch={1:listartiquet, 2:agregartiquet, 3:listartiquetsector, 4:sumt}

while respuesta=="si":
    print("******************************************************************")
    print("*    opcion 1: Listar tiquets                                    *")
    print("*    opcion 2: Agregar tiquet                                    *")
    print("*    opcion 3: buscar tiquets por sector                         *")
    print("*    opcion 4: Mostrar la suma de todas las tarifas              *")
    print("******************************************************************")
    x=int(input("Seleccione su opcion \t"))
    switch.get(x,default)()
    respuesta=input("\n Desea continuar si/no \t")
    os.system("cls")