import requests
from requests.api import request
from requests.models import Response
class Database:
    def listtiquet(self):
        response=requests.get("http://localhost/evaluacion4/conecta.php")
        return response

    def listsector(self,sector):
        Response=requests.get('http://localhost/evaluacion4/conectasector.php?sector='+sector)
        return Response

    def buscartiquet(self,id,sector,asiento):
        bandera=False
        count=requests.get('http://localhost/evaluacion4/buscarid2.php?id='+str(id)+'&&sector='+sector+'&&asiento='+str(asiento))
        for x in count.json():
            cantidad=x["contador"]
        if cantidad=="1":
            bandera=True
        return bandera

    def buscarsector(self,sector):
        bandera=False
        count=requests.get('http://localhost/evaluacion4/buscarid.php?sector='+sector)
        for x in count.json():
            cantidad=x["contador"]
        if cantidad=="0":
            bandera=True
        return bandera

    
    def Agregartiquets(self,id,sector,asiento,tarifa):
        if self.buscartiquet(id,sector,asiento):
            print("Ya existe en la BD")
        else:
            url='http://localhost/evaluacion4/agregartiquet.php?id='+str(id)+'&&sector='+sector+'&&asiento='+str(asiento)+'&&tarifa='+str(tarifa)
            Response=requests.get(url)
        return Response
    

    def suma(self):
        sum=requests.get("http://localhost/evaluacion4/sumtarifa.php")
        return sum
    

       