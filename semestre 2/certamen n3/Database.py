import pymysql
class Database:
    def __init__(self):
        self.connection=pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='evaluacion3'
        )
        self.cursor=self.connection.cursor()

    def buscarpropiedades(self,id):
        bandera=False
        query="select count(id) from evaluacion3 where id="+str(id)
        self.cursor.execute(query)
        levaluacion3=self.cursor.fetchall()
        for x in levaluacion3:
            cantidad=x[0]
        if cantidad>0:
            bandera=True
        return bandera

    def buscarpropiedadescomuna(self,Comuna):
        bandera=False
        query="select count(ID) from evaluacion3 where Comuna='"+Comuna+"'"
        self.cursor.execute(query)
        levaluacion3=self.cursor.fetchall()
        for x in levaluacion3:
            cantidad=x[0]
        
        if cantidad>0:
            bandera=True
        return bandera

    
    
    def Listarpropiedades(self):
        try:
            query="Select*from evaluacion3"
            self.cursor.execute(query)
            evaluacion3=self.cursor.fetchall()
        except Exception as err:
            print(err)
        return evaluacion3
    
    def Agregarpropiedades(self,id,direccion,comuna,valor):
        if self.buscarpropiedades(id):
            print("Ya existe en la BD")
        else:
            query="insert into evaluacion3 values("+str(id)+",'"+direccion+"','"+comuna+"',"+str(valor)+")"
            self.cursor.execute(query)
            self.connection.commit()
    
    
    def eliminarPropiedades(self,ID):
        query="delete from evaluacion3 where id="+str(ID)
        self.cursor.execute(query)
        self.connection.commit()
    
    def actualizarpropiedades(self,id,direccion,comuna,valor):
        if self.buscarpropiedades(id):
            query="update evaluacion3 set Direccion='"+(direccion)+"',Comuna='"+(comuna)+"',valor="+str(valor)+" where ID="+str(id)+""
            self.cursor.execute(query)
            self.connection.commit()
        else:
            print("no existe en la BD")

    def Listarpropiedadescomuna(self,Comuna):
        try:
            query="select*from evaluacion3 where Comuna='"+Comuna+"'"
            self.cursor.execute(query)
            lcomuna=self.cursor.fetchall()
        except Exception as err:
            print(err)
        return lcomuna

    def promedio(self):
        query="select avg(Valor) from evaluacion3"
        self.cursor.execute(query)
        pro=self.cursor.fetchall()
        return pro
    

       