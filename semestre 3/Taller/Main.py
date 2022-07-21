from Basedatos import MyBaseDate

datos = MyBaseDate()




# rutTrabajador = input("\nIngrese rutTrabajador: ")
# Name = input("\nIngrese Name : ")
# Contraseña = input("\nIngrese Contraseña ")
# ApellidoPaterno = input("\nIngrese ApellidoPaterno ")
# ApellidoMaterno = input("\nIngrese ApellidoMaterno")
# sexooooo = input("\nIngrese sexooooo")
# direccioooon = input("\nIngrese direccioooon")
# numeroTelefono = int(input("\nIngrese numeroTelefono"))



# print('*******datos laborales***************')
# Cargoasd = input("\nIngrese direccioooon")
# FechaIngresoasd = input("\nIngrese FechaIngreso")
# AreaTrabajoasd = input("\nIngrese AreaTrabajo")
# Departamentoasd = input("\nIngrese Departament")

# datos.Insertar_trabajador_1(rutTrabajador,Name,Contraseña,ApellidoPaterno,ApellidoMaterno,sexooooo,direccioooon,numeroTelefono,Cargoasd,FechaIngresoasd,AreaTrabajoasd,Departamentoasd)

# print('*******contactos de emergencia***************')
# NombreContacto = input("\nIngrese NombreContacto")
# Relacion = input("\nIngrese Relacion")
# TelefonoContacto = input("\nIngrese TelefonoContacto")
# print('*******cargas familiares***************')
# NombreCarga = input("\nIngrese NombreCarga")
# Rut_Carga = input("\nIngrese Rut_Carga")
# Parentesco = input("\nIngrese Parentesco")
# Sexo2 = input("\nIngrese Sexo2")



# datos.Insertar_trabajador(rutTrabajador,Name,Contraseña,ApellidoPaterno,ApellidoMaterno,sexooooo,direccioooon,numeroTelefono)

# ,Cargo,FechaIngreso,AreaTrabajo,Departamento,NombreContacto,Relacion,TelefonoContacto,NombreCarga,Rut_Carga,Parentesco,Sexo2)




evaluacin3=datos.Listar_trabajadores()
for m in evaluacin3:

    print("* id-> {}".format(m[5]))
    print("* direccion-> {}".format(m[11]))
    print("* valor-> {}".format(m[8]))
    print("----------------------------------------")





# evaluacin3=datos.Listar_trabajadores()
# for m in evaluacin3:

#     print("* id-> {}".format(m[0]))
#     print("* direccion-> {}".format(m[1]))
#     print("* valor-> {}".format(m[5]))
#     print("* valor-> {}".format(m[8]))
#     print("----------------------------------------")

# rut = input("\nIngrese su rut: ")
# datos.validacion(rut)


