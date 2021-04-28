"""
Nombre: SistemaDeReservación
Entradas:No posee entradas
Salidas: retorna el menú principal
Restriciones:No posee restricciones
"""
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
#-----------------------------------------------------------------------------------------------------------------
"""
Nombre: menu2
Entradas: No posee entradas
Salidas: retorna el menú administrativo
Restricciones:No posee restricciones
"""
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
#--------------------------------------------------------------------------------------------------------------
"""
Nombre: menu3
Entradas: No posee entradas
Salidas: retorna el menú general
Restricciones:No posee restricciones
"""        
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
#--------------------------------------------------------------------------------------------------------------
"""
Nombre: GestionEmpresas
Entradas: No posee entradas
Salidas: retorna el menú de gestión de empresas
Restricciones:No posee restricciones
"""
#3.1
def GestionEmpresas():
    print("\n\t1 - Incluir empresa\n\n\t2 - Eliminar empresa\n\n\t3 - Modificar empresa\n\n\t4 - Mostrar empresas\n\n\t5 - Retoranar ")
    
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
#------------------------------------------------------------------------------------------------------------------
"""
Nombre: IncluirEmpresa
Entradas: No posee entradas
Salidas: crea el archivo de texto "Información de la empresa" y almacena los datos de la empresa
Restricciones:La cédula jurídica debe tener 10 dígitos
"""
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
    print ("\n\t\t>>>>>La empresa ha sido agregada<<<<<")
#--------------------------------------------------------------------------------------------------------------------
"""
Nombre: EliminarEmpresa
Entradas: No posee entradas
Salidas: al dígitar la cédula jurídica se eliminarán los datos almacenados de la empresa
Restricciones:No posee restricciones
"""
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
"""
Nombre: EliminarEmpresa_aux
Entradas: Borrar,ContarLineas,contador
Salidas:
Restricciones:
"""
def EliminarEmpresa_aux(Borrar,ContarLineas,contador):
    if contador == 3:
        return TransformarString(Borrar)
    else:
        print(Borrar[ContarLineas].rstrip())
        Borrar.pop(ContarLineas)
        return EliminarEmpresa_aux(Borrar,ContarLineas,contador+1)
"""
Nombre: TransformarString
Entradas: Borrar
Salidas:
Restricciones:
"""
def TransformarString(Borrar):
    if isinstance(Borrar,list):
        string = ""
        for linea in Borrar:
            string += linea
        return string
    else:
        print("")
#-------------------------------------------------------------------------------------------------------------------
"""
Nombre: ModificarEmpresa
Entradas: No posee entradas
Salidas: al dígitar  el número de cédula jurídica se podrá modificar los datos almacenados de la empresa
Restricciones:No posee restricciones
"""
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
"""
Nombre: Empresa2_aux
Entradas: lista,Indice,contador
Salidas:
Restricciones:
"""
def Empresa2_aux(lista,Indice,contador):
    if contador == 3:
        print("") 
    else:
        print(lista[Indice].rstrip())
        return Empresa2_aux(lista,Indice+1,contador+1)
"""
Nombre: Empresa3_aux
Entradas: Dato,Indice,contador
Salidas:
Restricciones:
"""
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
"""
Nombre: TransformarString_aux
Entradas: dato
Salidas:
Restricciones:
"""
def TransformarString_aux(dato):
    if isinstance(dato,list):
        string = ""
        for linea in dato:
            string += linea
        return string
    else:
        print("")
#--------------------------------------------------------------------------------------------------------------------
"""
Nombre: MostrarEmpresas
Entradas: No posee entradas
Salidas: abre el archivo de texto "Información de la empresa" y muestra su contenido
Restricciones:No posee restricciones
"""
def MostrarEmpresas():
    Abrir = open("Información de la empresa.txt","r")
    for Agregar in Abrir:
        print(Agregar)
    Abrir.close()
#--------------------------------------------------------------------------------------------------------------------
"""
Nombre: GestionTransporte
Entradas: No posee entradas
Salidas: retorna el menú de gestión de transporte por empresa
Restricciones:No posee restricciones
"""
#3.2
def GestionTransporte():
    print("\n\t1 - Incluir transporte\n\n\t2 - Eliminar transporte\n\n\t3 - Modificar transporte\n\n\t4 - Mostrar transportes\n\n\t5 - Retornar")
    
    op = input("\n\t>>>>>Seleccione una de las siguientes opciones:")
    
    if(op == "1"):
        return IncluirTransporte()
    elif(op == "2"):
        return EliminarTransporte()
    elif(op == "3"):
        return ModificarTransporte()
    elif(op == "4"):
        return MostrarTransportes()
    elif(op == "5"):
        return menu2()
    else:
        print("\n\t>>>>>Seleccione una de las siguientes opciones:")
        return GestionTransporte()
#--------------------------------------------------------------------------------------------------------------------       
"""
Nombre: IncluirTransporte
Entradas: No posee entradas
Salidas: crea el archivo de texto "Información del transporte" y almacena los datos del transporte
Restricciones:no posee restricciones
"""
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

#--------------------------------------------------------------------------------------------------------------------
"""
Nombre: EliminarTransporte
Entradas: No posee entradas
Salidas: al escribir la placa del transporte se podrá eliminar los datos almacenados del transporte
Restricciones: No posee restricciones
"""
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
"""
Nombre: EliminarTransporte_aux
Entradas: Borrar,ContarLineas,contador
Salidas:
Restricciones:
"""
def EliminarTransporte_aux(Borrar,ContarLineas,contador):
    if contador == 8:
        return TransformarString(Borrar)
    else:
        print(Borrar[ContarLineas].rstrip())
        Borrar.pop(ContarLineas)
        return EliminarEmpresa_aux(Borrar,ContarLineas,contador+1)
#---------------------------------------------------------------------------------------------------------------------
"""
Nombre: ModificarTransporte
Entradas: No posee entradas
Salidas: al escribir la placa del transporte se podrá modificar los datos almacenados del transporte
Restricciones: No posee restricciones
"""
def ModificarTransporte():
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
"""
Nombre: Transporte2_aux
Entradas: lista,Indice,contador
Salidas:
Restricciones:
"""
def Transporte2_aux(lista,Indice,contador):
    if contador == 8:
        print("") 
    else:
        print(lista[Indice].rstrip())
        return Transporte2_aux(lista,Indice+1,contador+1)
"""
Nombre: Transporte3_aux
Entradas: Dato,Indice,contador
Salidas:
Restricciones:
"""
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
#---------------------------------------------------------------------------------------------------------------------
"""
Nombre: MostrarTransportes
Entradas: No posee entradas
Salidas: abre el archivo de texto "Información del transporte" y muestra su contenido
Restricciones:No posee restricciones
"""
def MostrarTransportes():
    Abrir = open("Información del transporte.txt","r")
    for Agregar in Abrir:
        print(Agregar)
    Abrir.close()
#---------------------------------------------------------------------------------------------------------------------
"""
Nombre: GestionViaje
Entradas: No posee entradas
Salidas: retorna el menú de gestión de viaje
Restricciones:No posee restricciones
"""
#3.3
def GestionViaje():
    print("\n\t1 - Incluir viaje\n\n\t2 - Eliminar viaje\n\n\t3 - Modificar viaje\n\n\t4 - Mostrar viajes\n\n\t5 - Retornar")
    
    op = input("\n\t>>>>>Seleccione una de las siguientes opciones:")
    
    if(op == "1"):
        return IncluirViaje()
    elif(op == "2"):
        return EliminarViaje()
    elif(op == "3"):
        return ModificarViaje()
    elif(op == "4"):
        return MostrarViajes()
    elif(op == "5"):
        return menu2()
    else:
        print("\n\t>>>>>Seleccione una de las siguientes opciones:")
        return GestionViaje()
#---------------------------------------------------------------------------------------------------------------------
"""
Nombre: IncluirViaje
Entradas: No posee entradas
Salidas: crea el archivo de texto "Información por viaje" y almacena los datos del viaje
Restricciones: no posee restricciones
"""
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
#--------------------------------------------------------------------------------------------------------------------
"""
Nombre: EliminarViaje
Entradas: No posee entradas
Salidas: al escribir el número del viaje se eliminarán los datos almacenados de la empresa
Restricciones:No posee restricciones
"""
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
        print("\n\t>>>>>El viaje ha sido eliminado<<<<<")
        print("\n")
        SistemaDeReservación()
    else:
        print("\n\t>>>>>El viaje no existe<<<<<")
        print("\n")
        SistemaDeReservación()
"""
Nombre: EliminarViaje_aux
Entradas: Borrar,ContarLineas,contador
Salidas:
Restricciones:
"""
def EliminarViaje_aux(Borrar,ContarLineas,contador):
    if contador == 9:
        return TransformarString(Borrar)
    else:
        print(Borrar[ContarLineas].rstrip())
        Borrar.pop(ContarLineas)
        return EliminarViaje_aux(Borrar,ContarLineas,contador+1)
#---------------------------------------------------------------------------------------------------------------------
"""
Nombre: ModificarViaje
Entradas: No posee entradas
Salidas: al escribir el número del viaje se podrá modificar los datos almacenados del viaje
Restricciones: No posee restricciones
"""
def ModificarViaje():
    NumeroViaje  = input("\n\tEscriba el número del viaje:")
    Abrir = open("Información por viaje.txt")
    viaje = Abrir.readlines()
    Abrir.close()
    if (NumeroViaje  + "\n") in viaje:
        Indice = viaje.index(NumeroViaje+ "\n")
        Viaje2_aux(viaje,Indice,0)
        ViajeNuevo = Viaje3_aux(viaje,Indice+1,0)
        Abrir = open("Información por viaje.txt","w")
        Abrir.write(TransformarString_aux(ViajeNuevo))
        Abrir.close()
"""
Nombre: Viaje2_aux
Entradas: lista,Indice,contador
Salidas:
Restricciones:
"""
def Viaje2_aux(lista,Indice,contador):
    if contador == 9:
        print("") 
    else:
        print(lista[Indice].rstrip())
        return Viaje2_aux(lista,Indice+1,contador+1)
"""
Nombre: Viaje3_aux
Entradas: Dato,Indice,contador
Salidas:
Restricciones:
"""
def Viaje3_aux(Dato,Indice,contador):
    if contador > 5:
        return Dato
    elif contador == 1:
        Dato2 = input("\n\tCiudad de salida:")
        Dato[Indice]=Dato2 + "\n"
        return Viaje3_aux(Dato,Indice+1,contador+1)
    else:
        if contador == 2:
            Dato2 = input("\n\tFecha y hora de salida:")
            Dato[Indice]=Dato2 + "\n"
            return Viaje3_aux(Dato,Indice+1,contador+1)
        elif contador == 3:
            Dato2 = input("\n\tCiudad de llegada:")
            Dato[Indice]=Dato2 + "\n"
            return Viaje3_aux(Dato,Indice+1,contador+1)
        elif contador == 4:
            Dato2 = input("\n\tFecha y hora de llegada:")
            Dato[Indice]=Dato2 + "\n"
            return Viaje3_aux(Dato,Indice+1,contador+1)
        elif contador == 5:
            Dato2 = input("\n\tEmpresa y transporte:")
            Dato[Indice]=Dato2 + "\n"
            return Viaje3_aux(Dato,Indice+1,contador+1)
        elif contador == 6: 
            Dato2 = input("\n\tMonto de asiento VIP:")
            Dato[Indice]=Dato2 + "\n"
            return Viaje3_aux(Dato,Indice+1,contador+1)
        elif contador == 7: 
            Dato2 = input("\n\tMonto de asiento normal:")
            Dato[Indice]=Dato2 + "\n"
            return Viaje3_aux(Dato,Indice+1,contador+1)
        else:
            Dato2 = input("\n\tMonto de asiento económico")
            Dato[Indice]=Dato2 + "\n"
            return Viaje3_aux(Dato,Indice+1,contador+1)
#---------------------------------------------------------------------------------------------------------------------
"""
Nombre: MostrarViajes
Entradas: No posee entradas
Salidas: abre el archivo de texto "Información por viaje" y muestra su contenido
Restricciones:No posee restricciones
"""
def MostrarViajes():
    Abrir = open("Información por viaje.txt","r")
    for Agregar in Abrir:
        print(Agregar)
    Abrir.close()
#---------------------------------------------------------------------------------------------------------------------
"""
Nombre:
Entradas:
Salidas:
Restricciones:
"""
#3.4
#def ConsultarHistorial():
#---------------------------------------------------------------------------------------------------------------------
"""
Nombre:
Entradas:
Salidas:
Restricciones:
"""
#3.5
#def Estadisticas():
#---------------------------------------------------------------------------------------------------------------------
"""
Nombre:
Entradas:
Salidas:
Restricciones:
"""
#4.1
#def Consulta():
#---------------------------------------------------------------------------------------------------------------------
"""
Nombre:
Entradas:
Salidas:
Restricciones:
"""
#4.2
#def Reservacion():
SistemaDeReservación()
