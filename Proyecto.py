
#2.
def SistemaDeReservación():
    print("\n\t\tSistema de reservación de boletos")
    print("\n\tMenú Principal:")
    print("\n\t1 - Opciones administrativas\n\n\t2 - Opciones de usuario normal\n\n\t3 - Salir")
    op = input("\n\tDígite una de las siguientes opciones:")

    if(op == "1"):
        return menu2()
    elif(op == "2"):
        return menu3()
    elif(op == "3"):
        return print("\n\tHasta pronto")
    else:
        print("\n\tSeleccione una de las siguientes opciones:")
#3.
def menu2():
    print("\n\t\tMenú Administrativo:")
    print("\n\t1 - Gestión de empresas")
    print("\n\t2 - Gestión de transporte por empresa")
    print("\n\t3 - Gestión de viaje")
    print("\n\t4 - Consultar historial de reservaciones")
    print("\n\t5 - Estadísticas de viaje")

    op = input("\n\tElija una de las siguientes opciones:")

    if(op == "1"):
        return GestionEmpresas()
    elif(op == "2"):
        return GestionTransporte()
    elif(op == "3"):
        return GestionViaje()
    elif(op == "4"):
        return ConsultarHistorial()
    elif(op == "5"):
        return Estadisticas()
    else:
        print("\n\tSeleccione una de las siguientes opciones:")
#4.
def menu3():
    print("\n\t\tMenú General")
    print("\n\t1 - Consulta de viajes")
    print("\n\t2 - Reservación de viaje")
    print("\n\t3 - Cancelación de reservación")

    print("\n\t4 - Salir ")#

    op = input("\n\tElija una de las siguientes opciones:")

    if(op == "1"):
        return Consulta()
    elif(op == "2"):
        return Reservacion()
    elif(op == "3"):
        return Cancelacion()
    elif(op == "4"):
        return print("\n\tHasta pronto")
    else:
        print("\n\tSeleccione una de las siguientes opciones:")
#--------------------------------------------------------------------------------------
#3.1
def GestionEmpresas():
    print("\n\t1 - Incluir empresa\n\n\t2 - Eliminar empresa\n\n\t3 - Modificar\n\n\t4 - Mostrar empresas")
    
    op = input("\n\tSeleccione una de las siguientes opciones:")

    if(op == "1"):
        return IncluirEmpresas()
    elif(op == "2"):
        return EliminarEmpresa()
    elif(op == "3"):
        return ModificarEmpresa()
    elif(op == "4"):
        return MostrarEmpresas()
    else:
        print("\n\tSeleccione una de las siguientes opciones:")
        return GestionEmpresas()

#-------------------------------------------------------------------------------------

def IncluirEmpresa():
    print("\n\t\tInformación de la empresa")
    Archivo = "Información de la empresa.txt"
    Archivo2 = open(Archivo,"a")
    Cedula = input("\n\tDígite el número de cédula jurídica:")
    if len(Cedula)== 10:
        Nombre = input("\n\tEscriba el nombre de la empresa:")
    else:
        print("La cédula jurídica debe tener 10 dígitos")
        return IncluirEmpresa()
    Ubicacion = input("\n\tEscriba la ubicación de la empresa:")
    Archivo2.write("Cédula júridica:"+Cedula+"\n")
    Archivo2.write(Nombre+"\n")
    Archivo2.write(Ubicacion+"\n")
    Archivo2.write("........................"+"\n")
    Archivo2.close()
    print ("\n\t\tLa empresa ha sido agregada")#

#-----------------------------------------------------------------------------------------
#def EliminarEmpresa():

#-----------------------------------------------------------------------------------------
def MostrarEmpresas():
    
#-----------------------------------------------------------------------------------------
#3.2
def GestionTransporte():
    print("\n\t1 - Incluir transporte\n\n\t2 - Eliminar transporte\n\n\t3 - Mostrar transportes")
    
    op = input("\n\tSeleccione una de las siguientes opciones:")
    
    if(op == "1"):
        return IncluirTransporte()
    elif(op == "2"):
        return EliminarTransporte()
    elif(op == "3"):
        return MostrarTransportes()
    else:
        print("\n\tSeleccione una de las siguientes opciones:")  
#----------------------------------------------------------------------------------------       
def IncluirTransporte():
    print("\n\t\tInformación del transporte")
    Archivo = "Información del transporte.txt"
    Archivo2 = open(Archivo,"a")
    Placa = input("\n\tEscriba la placa del transporte:")
    Marca = input("\n\tEscriba la marca del transporte:")
    Modelo = input("\n\tEscriba el modelo del transporte:")
    Año = input("\n\tDigite el año del transporte:")
    Archivo3 = open("Información de la empresa.txt")
    Informacion = Archivo3.read()
    print(Informacion)
    Empresa = input("\n\tSeleccione una de las empresas:")
    Cantidad = input("\n\t")
    Archivo2.write(Placa+"\n")
    Archivo2.write(Marca+"\n")
    Archivo2.write(Modelo+"\n")
    Archivo2.write(Año+"\n")
    Archivo2.write(Empresa+"\n")
    Archivo2.write(Cantidad+"\n")
    Archivo2.close()
    print ("\n\t\tEl transporte ha sido almacenado")

#-----------------------------------------------------------------------------------------
#def EliminarTransporte():

#-----------------------------------------------------------------------------------------
#def MostrarTransportes():
#-----------------------------------------------------------------------------------------
#3.3
def GestionViaje():
    print("\n\t1 - Incluir viaje\n\n\t2 - Eliminar viaje\n\n\t3 - Mostrar viajes")
    
    op = input("\n\tSeleccione una de las siguientes opciones:")
    
    if(op == "1"):
        return IncluirViaje()
    elif(op == "2"):
        return EliminarViaje()
    elif(op == "3"):
        return MostrarViajes()
    else:
        print("\n\tSeleccione una de las siguientes opciones:")
#---------------------------------------------------------------------------------------
def IncluirViaje():
    print("\n\t\tInformación por viaje")
    Archivo = "Información por viaje.txt"
    Archivo2 = open(Archivo,"a")
    
    NumeroViaje = input("\n\tNúmero del viaje:")#
    CiudadSalida = input("\n\tCiudad de salida:")
    FechaYHoraSalida = input("\n\tFecha y hora de salida:")
    CiudadLLegada = input("\n\tCiudad de llegada:")
    FechaYHoraLLegada = input("\n\tFecha y hora de llegada:")
    EmpresaYTransporte = input("\n\tEmpresa y transporte:")#
    MontoAsientoVIP = input("\n\tEmpresa y transporte:")#
    MontoAsientoNormal = input("\n\tEmpresa y transporte:")
    MontoAsientoEconomica = input("\n\tEmpresa y transporte:")
    Archivo2.write(NumeroViaje+"\n")
    Archivo2.write(CiudadSalida+"\n")
    Archivo2.write(FechaYHoraSalida+"\n")
    Archivo2.write(CiudadLLegada+"\n")
    Archivo2.write(FechaYHoraLLegada+"\n")
    Archivo2.write(EmpresaYTransporte+"\n")
    Archivo2.close()
    print ("\n\t\tEl transporte ha sido almacenado")

#----------------------------------------------------------------------------------------
#def EliminarViaje():

#-----------------------------------------------------------------------------------------
#def MostrarViajes():
#-----------------------------------------------------------------------------------------
#3.4
#def ConsultarHistorial():

#------------------------------
#3.5
#def Estadisticas():
#-------------------------------
"""
#4.1
def Consulta():
  
"""
#--------------------------------
#4.2
#def Reservacion():



SistemaDeReservación()
    
