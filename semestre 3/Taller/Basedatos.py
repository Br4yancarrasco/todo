import pymysql


class MyBaseDate():

    def __init__(self):
        self.conexion = pymysql.connect(
        host = "localhost",
        user = "root",
        password = "",
        db = "listadotrabajadores"

        )
        self.cursor = self.conexion.cursor()



        # CARGAS FAMILIARES DE EMERGENCIA UPDATE, DELETE , INSERT


    def trabajador_agregarCARGAS_FAMILIARES(self,Rut_trabajador,NombreCarga,Rut_Carga,Parentesco,Sexo):

        if self.buscar_Carga(Rut_Carga):
            print("Carga ya existe en base de datos")
            

        else:
            query:"insert into Cargas_familiares values ('{}','{}','{}','{}','{}')".format(Rut_trabajador,NombreCarga,Rut_Carga,Parentesco,Sexo)
            self.cursor.execute(query)
            self.conexion.commit()
            print ("\n--------- Carga agregada exitosamente ---------")   

    def trabajador_eliminarCARGAS_FAMILIARES(self,Rut_trabajador,Rut_Carga):

        if self.buscar_Carga(Rut_Carga):
            query:"DELETE FROM Cargas_familiares WHERE Rut_trabajador='{}'  and Rut_Carga = '{}';".format(Rut_trabajador,Rut_Carga)
            self.cursor.execute(query)
            self.conexion.commit()
            print ("\n--------- Carga eliminada exitosamente ---------")   

        else:
            print("No se encuentra carga")


    def trabajador_actualizarCARGAS_FAMILIARES(self,NombreCarga,Rut_Carga,Parentesco,Sexo,Rut_trabajador):

        if self.buscar_Carga(Rut_Carga):
            query:"UPDATE Cargas_familiares SET NombreCarga = '{}', Rut_Carga= '{}', Parentesco= '{}', Sexo= '{}' WHERE Rut_Carga = '{}' and Rut_trabajador = '{}';".format(NombreCarga,Rut_Carga,Parentesco,Sexo,Rut_Carga,Rut_trabajador)
            self.cursor.execute(query)
            self.conexion.commit()
            print ("\n--------- Datos actualizados exitosamente ---------")   
        
        else:
            print("Error no se encuentra su Rut")


    # CONTACTOS DE EMERGENCIA UPDATE, DELETE , INSERT

    def trabajador_agregarCONTACTOS_EMERGENCIA(self,NombreContacto,Relacion,Rut_trabajador,TelefonoContacto):

        if self.buscar_contacto(TelefonoContacto):
            print("Carga ya existe en base de datos")
            

        else:
            query:"insert into contacto_emergencia values('{}','{}','{}',{})".format(NombreContacto,Relacion,Rut_trabajador,TelefonoContacto)
            self.cursor.execute(query)
            self.conexion.commit()
            print ("\n--------- Contacto agregado exitosamente ---------")   



    def trabajador_eliminarCONTACTOS_EMERGENCIA(self,TelefonoContacto,Rut_trabajador,Rut_Carga):

        if self.buscar_contacto(TelefonoContacto):
            query:"DELETE FROM contacto_emergencia WHERE Rut_trabajador='{}'  and TelefonoContacto = {};".format(Rut_trabajador,TelefonoContacto)
            self.cursor.execute(query)
            self.conexion.commit()
            print ("\n--------- Contacto eliminado exitosamente ---------")   

        else:
            print("No se encuentra el contacto")

    def trabajador_actualizarCONTACTOS_EMERGENCIA(self,NombreContacto,Relacion,Rut_trabajador,TelefonoContacto):

        if self.buscar_contacto(TelefonoContacto):
            query:"UPDATE contacto_emergencia SET NombreContacto = '{}', Relacion= '{}', TelefonoContacto= {} WHERE Rut_trabajador = '{}' and TelefonoContacto = '{}';".format(NombreContacto,Relacion,Rut_trabajador,TelefonoContacto)
            self.cursor.execute(query)
            self.conexion.commit()
            print ("\n--------- Datos actualizados exitosamente ---------")   
        
        else:
            print("Error contacto de emergencia")







    def trabajador_actualizarDATOS_PERSONALES(self,Rut_trabajador,Nombre,Clave,ApellidoMat,ApellidoPat,Sexo,Direccion,Telefono):

        query:"UPDATE Datos_personales SET Nombre = '{}', Clave= {}, ApellidoMat= '{}', ApellidoPat= '{}', Sexo= '{}', Direccion= '{}', Telefono= {} WHERE Rut_trabajador = '{}';".format(Nombre,Clave,ApellidoMat,ApellidoPat,Sexo,Direccion,Telefono,Rut_trabajador)
        self.cursor.execute(query)
        self.conexion.commit()
        print ("\n--------- Datos actualizados exitosamente ---------")    
        # HACER COSO DEL RUT EN EL MAIN





    def Insertar_trabajador_1(self,Rut_trabajador,Nombre,Clave,ApellidoMat,ApellidoPat,Sexo,Direccion,Telefono,Cargo,FechaIngreso,AreaTrabajo,Departamento,NombreContacto,Relacion,TelefonoContacto,NombreCarga,Rut_Carga,Parentesco,Sexo2):
        
        if self.buscar_Rut(Rut_trabajador):
            print("\nERROR, Ya se encuentra en la base de datos")

        else: 
            query = "insert into Datos_personales values('{}','{}',{},'{}','{}','{}','{}',{})".format(Rut_trabajador,Nombre,Clave,ApellidoMat,ApellidoPat,Sexo,Direccion,Telefono)
            self.cursor.execute(query)
            query2 = "insert into Datos_laborales values ('{}','{}','{}','{}','{}')".format(Cargo,Rut_trabajador,FechaIngreso,AreaTrabajo,Departamento)
            self.cursor.execute(query2)
            query3 = "insert into Contacto_emergencia ('{}','{}','{}',{})".format(NombreContacto,Relacion,Rut_trabajador,TelefonoContacto)
            self.cursor.execute(query3)
            query4 = "insert into Cargas_familiares values ('{}','{}','{}','{}','{}')".format(NombreCarga,Rut_Carga,Rut_trabajador,Parentesco,Sexo2)
            self.cursor.execute(query4)
            self.conexion.commit()
            print ("\n--------- Propiedad ingresada exitosamente ---------")    

    

    def Listar_trabajadores(self):
        try:
            query="SELECT * FROM datos_personales DP JOIN Datos_laborales D ON DP.Rut_trabajador = D.Rut_trabajador"
            self.cursor.execute(query)
            evaluacion3=self.cursor.fetchall()
        except Exception as err:
            print(err)
        return evaluacion3



    def validacion(self,rut):
        if self.buscar_Rut(rut):
            clave = input("\nIngrese clave: ")
            while self.buscar_clave(clave) != 1:
                print("Clave incorrecta")
                clave = input("\nIngrese clave nuevamente: ")
            print("Acceso Exitoso")

        else:
            print("Error no se encuentra su Rut")

    def buscar_Rut(self,rut):
        bandera=False
        query = "select count('{}') from Datos_personales where Rut_trabajador = '{}'".format(rut,rut)
        self.cursor.execute(query)
        pr = self.cursor.fetchall()
        for x in pr:
            cantidad = x[0]

        if cantidad == 1:
            bandera=True
        return bandera

    def buscar_Carga(self,Rut_Carga):
        bandera=False
        query = "select count('{}') from Cargas_familiares where Rut_Carga = '{}'".format(Rut_Carga,Rut_Carga)
        self.cursor.execute(query)
        pr = self.cursor.fetchall()
        for x in pr:
            cantidad = x[0]

        if cantidad == 1:
            bandera=True
        return bandera

    def buscar_clave(self,clave):
        bandera2=False
        query = "select count('{}') from Datos_personales where Clave = '{}'".format(clave,clave)
        self.cursor.execute(query)
        pr2 = self.cursor.fetchall()
        for x in pr2:
            cantidad = x[0]

        if cantidad == 1:
            bandera2=True
        return bandera2

    def buscar_contacto(self,TelefonoContacto):
        bandera2=False
        query = "select count('{}') from Contacto_emergencia where TelefonoContacto = {}".format(TelefonoContacto,TelefonoContacto)
        self.cursor.execute(query)
        pr2 = self.cursor.fetchall()
        for x in pr2:
            cantidad = x[0]

        if cantidad == 1:
            bandera2=True
        return bandera2