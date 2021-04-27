
#2.
def SistemaDeReservación():
    print("\n\t\tSistema de reservación de boletos")
    print("\n\tMenú Principal:")
    print("\n\t1 - Opciones administrativas\n\n\t2 - Opciones de usuario normal\n\n\t3 - Salir")
    op = input("\n\t>>>>>Dígite una de las siguientes opciones:")

    if(op == "1"):
        return menu2()
    elif(op == "2"):
        return menu3()
    elif(op == "3"):
        return print("\n\tHasta pronto")
    else:
        print("\n\t>>>>>Seleccione una de las siguientes opciones:")
#3.
def menu2():
    print("\n\tMenú Administrativo:")
    print("\n\t1 - Gestión de empresas")
    print("\n\t2 - Gestión de transporte por empresa")
    print("\n\t3 - Gestión de viaje")
    print("\n\t4 - Consultar historial de reservaciones")
    print("\n\t5 - Estadísticas de viaje")
    print("\n\t6 - Salir de menú administrativo")

    op = input("\n\t>>>>>Elija una de las siguientes opciones:")

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
    elif(op == "6"):
        return SistemaDeReservación()
    else:
        print("\n\t>>>>>Seleccione una de las siguientes opciones:")
#4.
def menu3():
    print("\n\tMenú General")
    print("\n\t1 - Consulta de viajes")
    print("\n\t2 - Reservación de viaje")
    print("\n\t3 - Cancelación de reservación")
    print("\n\t4 - Salir de menú general")

    op = input("\n\t>>>>>Elija una de las siguientes opciones:")

    if(op == "1"):
        return Consulta()
    elif(op == "2"):
        return Reservacion()
    elif(op == "3"):
        return Cancelacion()
    elif(op == "4"):
        return SistemaDeReservación()
    else:
        print("\n\t>>>>>Seleccione una de las siguientes opciones:")
#--------------------------------------------------------------------------------------
#3.1
def GestionEmpresas():
    print("\n\t1 - Incluir empresa\n\n\t2 - Eliminar empresa\n\n\t3 - Modificar empresas\n\n\t4 - Mostrar empresas\n\n\t5 - Retoranar ")
    
    op = input("\n\t>>>>>Seleccione una de las siguientes opciones:")

    if(op == "1"):
        return IncluirEmpresa()
    elif(op == "2"):
        return EliminarEmpresa()
    elif(op == "3"):
        return ModificarEmpresa()
    elif(op == "4"):
        return MostrarEmpresas()
    elif(op == "5"):
        return menu2()
    else:
        print("\n\t>>>>>Seleccione una de las siguientes opciones:")
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
    Archivo2.write("Nombre de la empresa:"+Nombre+"\n")
    Archivo2.write("Ubicación de la empresa:"+Ubicacion+"\n")
    Archivo2.write("..............................."+"\n")
    Archivo2.close()
    print ("\n\t\t>>>>>La empresa ha sido agregada<<<<<")#

#-----------------------------------------------------------------------------------------
def EliminarEmpresa():
    Cedula = input("\n\tDígite el número de cédula jurídica:")
    Almacen = open("Información de la empresa.txt")
    Borrar = Almacen.readlines()
    if(Cedula + "\n")in Borrar:
        ContarLineas = Borrar.index(Cedula + "\n")
        BorrarLineas = EliminarEmpresa_aux(Borrar,ContarLineas,0)
        Almacen.close()
        Abrir = open("Información de la empresa.txt","w")
        Abrir.write(BorrarLineas)
        Abrir.close()
        print("\n\t>>>>>La empresa ha sido eliminada<<<<<")
        print("\n")
        SistemaDeReservación()
    else:
        print("\n\t>>>>>La empresa no existe<<<<<")
        print("\n")
        SistemaDeReservación()

def EliminarEmpresa_aux(Borrar,ContarLineas,contador):
    if contador == 3:
        return TransformarString(Borrar)
    else:
        print(Borrar[ContarLineas].rstrip())
        Borrar.pop(ContarLineas)
        return EliminarEmpresa_aux(Borrar,ContarLineas,contador+1)

def TransformarString(Borrar):
    if isinstance(Borrar,list):
        string = ""
        for linea in Borrar:
            string += linea
        return string
    else:
        print("")

#----------------------------------------------------------------------------------------
def ModificarEmpresa():
    Cedula = input("\n\tDígite el número de cédula jurídica:")
    Abrir = open("Información de la empresa.txt")
    empresa = Abrir.readlines()
    Abrir.close()
    if (Cedula + "\n") in empresa:
        Indice = empresa.index(Cedula+ "\n")
        Empresa2_aux(empresa,Indice,0)
        EmpresaNueva = Empresa3_aux(empresa,Indice+1,0)
        Abrir = open("Información de la empresa.txt","w")
        Abrir.write(TransformarString_aux(EmpresaNueva))
        Abrir.close()

def Empresa2_aux(lista,Indice,contador):
    if contador == 3:
        print("") 
    else:
        print(lista[Indice].rstrip())
        return Empresa2_aux(lista,Indice+1,contador+1)

def Empresa3_aux(Dato,Indice,contador):
    if contador > 5:
        return Dato
    elif contador == 1:
        Dato2 = input("\n\tNombre de la empresa:")
        Dato[Indice]=Dato2 + "\n"
        return Empresa3_aux(Dato,Indice+1,contador+1)
    else:
        if contador == 2:
            Dato2 = input("\n\tUbicación de la empresa:")
            Dato[Indice]=Dato2 + "\n"
            return Empresa3_aux(Dato,Indice+1,contador+1)
        
        else: 
            Dato2 = input("\n\tLugar de trabajo:")#
            Dato[Indice]=Dato2 + "\n"                 #
            return Contacto3_aux(Dato,Indice+1,contador+1)#

def TransformarString_aux(dato):
    if isinstance(dato,list):
        string = ""
        for linea in dato:
            string += linea
        return string
    else:
        print("")
        
#-----------------------------------------------------------------------------------------
def MostrarEmpresas():
    Abrir = open("Información de la empresa.txt","r")
    for Agregar in Abrir:
        print(Agregar)
    Abrir.close()

   
#-----------------------------------------------------------------------------------------
#3.2
def GestionTransporte():
    print("\n\t1 - Incluir transporte\n\n\t2 - Eliminar transporte\n\n\t3 - Modificar transportes\n\n\t4 - Mostrar transportes\n\n\t5 - Retornar")
    
    op = input("\n\t>>>>>Seleccione una de las siguientes opciones:")
    
    if(op == "1"):
        return IncluirTransporte()
    elif(op == "2"):
        return EliminarTransporte()
    elif(op == "3"):
        return ModificarTransportes()
    elif(op == "4"):
        return MostrarTransportes()
    elif(op == "5"):
        return menu2()
    else:
        print("\n\t>>>>>Seleccione una de las siguientes opciones:")
        return GestionTransporte()
#----------------------------------------------------------------------------------------       
def IncluirTransporte():
    print("\n\t\tInformación del transporte")
    Archivo = "Información del transporte.txt"
    Archivo2 = open(Archivo,"a")
    Placa = input("\n\tEscriba la placa del transporte:")
    Marca = input("\n\tEscriba la marca del transporte:")
    Modelo = input("\n\tEscriba el modelo del transporte:")
    Año = input("\n\tDígite el año del transporte:")
    Archivo3 = open("Información de la empresa.txt")
    Informacion = Archivo3.read()
    print(Informacion)
    Empresa = input("\n\tSeleccione una de las empresas:")
    CantidadAsientosVIP = input("\n\tCantidad de asientos clase VIP:")
    CantidadAsientosNormal = input("\n\tCantidad de asientos clase normal:")
    CantidadAsientosEconomicos = input("\n\tCantidad de asientos clase económica:")
    Archivo2.write("Placa del transporte:"+Placa+"\n")
    Archivo2.write("Marca del transporte:"+Marca+"\n")
    Archivo2.write("Modelo del transporte:"+Modelo+"\n")
    Archivo2.write("Año del transporte:"+Año+"\n")
    Archivo2.write("Empresa del transporte:"+Empresa+"\n")
    Archivo2.write("Cantidad de asientos clase VIP:"+CantidadAsientosVIP+"\n")
    Archivo2.write("Cantidad de asientos clase normal:"+CantidadAsientosNormal+"\n")
    Archivo2.write("Cantidad de asientos clase económica:"+CantidadAsientosEconomicos+"\n")
    Archivo2.write("......................................"+"\n")
    Archivo2.close()
    print ("\n\t\t>>>>>El transporte ha sido almacenado<<<<<")

#-----------------------------------------------------------------------------------------
def EliminarTransporte():
    Placa = input("\n\tEscriba la placa del transporte:")
    Almacen = open("Información del transporte.txt")
    Borrar = Almacen.readlines()
    if(Placa + "\n")in Borrar:
        ContarLineas = Borrar.index(Placa + "\n")
        BorrarLineas = EliminarTransporte_aux(Borrar,ContarLineas,0)
        Almacen.close()
        Abrir = open("Información del transporte.txt","w")
        Abrir.write(BorrarLineas)
        Abrir.close()
        print("\n\t>>>>>El transporte ha sido eliminado<<<<<")
        print("\n")
        SistemaDeReservación()
    else:
        print("\n\t>>>>>La empresa no existe<<<<<")
        print("\n")
        SistemaDeReservación()

def EliminarTransporte_aux(Borrar,ContarLineas,contador):
    if contador == 8:
        return TransformarString(Borrar)
    else:
        print(Borrar[ContarLineas].rstrip())
        Borrar.pop(ContarLineas)
        return EliminarEmpresa_aux(Borrar,ContarLineas,contador+1)

#-----------------------------------------------------------------------------------------
def ModificarTransportes():
    Placa = input("\n\tEscriba la placa del transporte:")
    Abrir = open("Información del transporte.txt")
    transporte = Abrir.readlines()
    Abrir.close()
    if (Placa + "\n") in transporte:
        Indice = transporte.index(Placa+ "\n")
        Transporte2_aux(transporte,Indice,0)
        TransporteNuevo = Transporte3_aux(transporte,Indice+1,0)
        Abrir = open("Información del transporte.txt","w")
        Abrir.write(TransformarString_aux(TransporteNuevo))
        Abrir.close()

def Transporte2_aux(lista,Indice,contador):
    if contador == 8:
        print("") 
    else:
        print(lista[Indice].rstrip())
        return Transporte2_aux(lista,Indice+1,contador+1)

def Transporte3_aux(Dato,Indice,contador):
    if contador > 5:
        return Dato
    elif contador == 1:
        Dato2 = input("\n\tEscriba la marca del transporte:")
        Dato[Indice]=Dato2 + "\n"
        return Transporte3_aux(Dato,Indice+1,contador+1)
    else:
        if contador == 2:
            Dato2 = input("\n\tEscriba el modelo del transporte:")
            Dato[Indice]=Dato2 + "\n"
            return Transporte3_aux(Dato,Indice+1,contador+1)
        elif contador == 3:
            Dato2 = input("\n\tDígite el año del transporte:")
            Dato[Indice]=Dato2 + "\n"
            return Transporte3_aux(Dato,Indice+1,contador+1)
        elif contador == 4:
            Dato2 = input("\n\tSeleccione una de las empresas:")
            Dato[Indice]=Dato2 + "\n"
            return Transporte3_aux(Dato,Indice+1,contador+1)
        elif contador == 5:
            Dato2 = input("\n\tCantidad de asientos clase VIP:")
            Dato[Indice]=Dato2 + "\n"
            return Transporte3_aux(Dato,Indice+1,contador+1)
        elif contador == 6: 
            Dato2 = input("\n\tCantidad de asientos clase normal:")
            Dato[Indice]=Dato2 + "\n"
            return Transporte3_aux(Dato,Indice+1,contador+1)
        else:
            Dato2 = input("\n\tCantidad de asientos clase económica:")
            Dato[Indice]=Dato2 + "\n"
            return Transporte3_aux(Dato,Indice+1,contador+1)

#----------------------------------------------------------------------------------------
def MostrarTransportes():
    Abrir = open("Información del transporte.txt","r")
    for Agregar in Abrir:
        print(Agregar)
    Abrir.close()

    
#-----------------------------------------------------------------------------------------
#3.3
def GestionViaje():
    print("\n\t1 - Incluir viaje\n\n\t2 - Eliminar viaje\n\n\t3 - Modificar viajes\n\n\t4 - Mostrar viajes\n\n\t5 - Retornar")
    
    op = input("\n\t>>>>>Seleccione una de las siguientes opciones:")
    
    if(op == "1"):
        return IncluirViaje()
    elif(op == "2"):
        return EliminarViaje()
    elif(op == "3"):
        return ModificarViajes()
    elif(op == "4"):
        return MostrarViajes()
    elif(op == "5"):
        return menu2()
    else:
        print("\n\t>>>>>Seleccione una de las siguientes opciones:")
        return GestionViaje()
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
    MontoAsientoVIP = input("\n\tMonto de asiento VIP:")#
    MontoAsientoNormal = input("\n\tMonto de asiento normal:")
    MontoAsientoEconomico = input("\n\tMonto de asiento económico:")
    Archivo2.write("Número de viaje:"+NumeroViaje+"\n")
    Archivo2.write("Ciudad de salida:"+CiudadSalida+"\n")
    Archivo2.write("Fecha y hora de salida:"+FechaYHoraSalida+"\n")
    Archivo2.write("Ciudad de llegada:"+CiudadLLegada+"\n")
    Archivo2.write("Fecha y hora de llegada:"+FechaYHoraLLegada+"\n")
    Archivo2.write("Empresa y transporte:"+EmpresaYTransporte+"\n")
    Archivo2.write("Monto de asiento clase VIP:"+MontoAsientoVIP+"\n")
    Archivo2.write("Monto de asiento clase normal:"+MontoAsientoNormal+"\n")
    Archivo2.write("Monto de asiento clase económica:"+MontoAsientoEconomico+"\n")
    Archivo2.write("......................................"+"\n")
    Archivo2.close()
    print ("\n\t\t>>>>>El transporte ha sido almacenado<<<<<")

#----------------------------------------------------------------------------------------
def EliminarViaje():
    NumeroViaje = input("\n\tEscriba el número del viaje:")
    Almacen = open("Información por viaje.txt")
    Borrar = Almacen.readlines()
    if(NumeroViaje + "\n")in Borrar:
        ContarLineas = Borrar.index(NumeroViaje + "\n")
        BorrarLineas = EliminarViaje_aux(Borrar,ContarLineas,0)
        Almacen.close()
        Abrir = open("Información por viaje.txt","w")
        Abrir.write(BorrarLineas)
        Abrir.close()
        print("\n\t>>>>>El transporte ha sido eliminado<<<<<")
        print("\n")
        SistemaDeReservación()
    else:
        print("\n\t>>>>>La empresa no existe<<<<<")
        print("\n")
        SistemaDeReservación()

def EliminarViaje_aux(Borrar,ContarLineas,contador):
    if contador == 9:
        return TransformarString(Borrar)
    else:
        print(Borrar[ContarLineas].rstrip())
        Borrar.pop(ContarLineas)
        return EliminarEmpresa_aux(Borrar,ContarLineas,contador+1)

#-----------------------------------------------------------------------------------------
#def ModificarViajes():
#-----------------------------------------------------------------------------------------
def MostrarViajes():
    Abrir = open("Información por viaje.txt","r")
    for Agregar in Abrir:
        print(Agregar)
    Abrir.close()

   
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
    
