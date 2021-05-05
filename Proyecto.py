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
        Archivo = open("clave de acceso.txt")
        Archivo2 = Archivo.readlines()
        clave = input("\n\t>>>>>Escriba la clave de acceso:")
        if(clave in Archivo2):
            return menu2()
        else:
            print("\n\t\t>>>>>La clave de acceso es incorrecta<<<<<")
            return SistemaDeReservación()
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
        return ConsultaViajes()
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
    print("\n\t1 - Incluir empresa\n\n\t2 - Eliminar empresa\n\n\t3 - Modificar empresa\n\n\t4 - Mostrar empresas\n\n\t5 - Retornar")
    
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
        Archivo3 = open(Archivo)
        Comprobar = Archivo3.readlines()
        if("Cédula júridica:"+Cedula+"\n") in Comprobar:
            print("\n\t\t>>>>>La cédula ya existe<<<<<")
            return IncluirEmpresa()
        else:
            Nombre = input("\n\tEscriba el nombre de la empresa:")
    else:
        print("\n\t\tLa cédula jurídica debe tener 10 dígitos")
        return IncluirEmpresa()
    Ubicacion = input("\n\tEscriba la ubicación de la empresa:")
    Archivo2.write("Cédula júridica:"+Cedula+"\n")
    Archivo2.write("Nombre de la empresa:"+Nombre+"\n")
    Archivo2.write("Ubicación de la empresa:"+Ubicacion+"\n")
    Archivo2.write("..............................."+"\n")
    Archivo2.close()
    print("\n\t\t>>>>>La empresa ha sido agregada<<<<<")
    print("\n")
    GestionEmpresas()
#--------------------------------------------------------------------------------------------------------------------
"""
Nombre: EliminarEmpresa
Entradas: No posee entradas
Salidas: al dígitar la cédula jurídica se eliminarán los datos almacenados de la empresa
Restricciones:No posee restricciones
"""
def EliminarEmpresa():
    Cedula = input("\n\tDígite el número de cédula jurídica:")
    print("\n")
    Almacen = open("Información de la empresa.txt")
    Borrar = Almacen.readlines()
    if("Cédula júridica:"+Cedula+ "\n")in Borrar:
        ContarLineas = Borrar.index("Cédula júridica:"+Cedula+ "\n")
        Almacen2 = open("Información del transporte.txt")
        Linea = Almacen2.readlines()
        if("Empresa del transporte:"+Borrar[ContarLineas+1][21:])in Linea:
            print("\n\t\t>>>>>La empresa está asociada a un transporte<<<<<")
            print("\n\t1 - Eliminar empresa\n\n\t2 - Regresar a menú gestión empresas")
            submenu = input("\n\t>>>>>Seleccione una de las siguientes opciones:")
            if(submenu == "1"):
                return EliminarEmpresa()
            else:
                return GestionEmpresas()
        else:
            BorrarLineas = EliminarEmpresa_aux(Borrar,ContarLineas,0)
            Almacen.close()
            Abrir = open("Información de la empresa.txt","w")
            Abrir.write(BorrarLineas)
            Abrir.close()
            print("\n\t>>>>>La empresa ha sido eliminada<<<<<")
            print("\n")
            GestionEmpresas()
    else:
        print("\n\t\t>>>>>La empresa no existe<<<<<")
        print("\n")
        GestionEmpresas()
"""
Nombre: EliminarEmpresa_aux
Entradas: Borrar,ContarLineas,contador
Salidas: TransformarString(Borrar)
Restricciones: No posee
"""
def EliminarEmpresa_aux(Borrar,ContarLineas,contador):
    if contador == 4:
        return TransformarString(Borrar)
    else:
        print(Borrar[ContarLineas].rstrip())
        Borrar.pop(ContarLineas)
        return EliminarEmpresa_aux(Borrar,ContarLineas,contador+1)
"""
Nombre: TransformarString
Entradas: Borrar
Salidas: retorna la lista en string
Restricciones: no posee
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
    if ("Cédula júridica:"+Cedula+ "\n") in empresa:
        Indice = empresa.index("Cédula júridica:"+Cedula+"\n")
        Empresa2_aux(empresa,Indice,0)
        EmpresaNueva = Empresa3_aux(empresa,Indice+1,0)
        Abrir = open("Información de la empresa.txt","w")
        Abrir.write(TransformarString_aux(EmpresaNueva))
        Abrir.close()
        print("\n\t\t>>>>>La empresa ha sido modificada<<<<<")
        print("\n")
        GestionEmpresas()
"""
Nombre: Empresa2_aux
Entradas: lista,Indice,contador
Salidas: muestra la empresa a modificar
Restricciones: no posee
"""
def Empresa2_aux(lista,Indice,contador):
    if contador == 3:
        print("") 
    else:
        print("\n\t",lista[Indice].rstrip())
        return Empresa2_aux(lista,Indice+1,contador+1)
"""
Nombre: Empresa3_aux
Entradas: Dato,Indice,contador
Salidas: dato modificado
Restricciones:
"""
def Empresa3_aux(Dato,Indice,contador):
    if contador > 1 :
        return Dato
    elif contador == 0:
        Dato2 = input("\n\tNombre de la empresa:")
        Dato[Indice]=("Nombre de la empresa:"+Dato2+ "\n")
        return Empresa3_aux(Dato,Indice+1,contador+1)
    else:
        Dato2 = input("\n\tUbicación de la empresa:")
        Dato[Indice]=("Ubicación de la empresa:"+Dato2+ "\n")
        return Empresa3_aux(Dato,Indice+1,contador+1)
        
"""
Nombre: TransformarString_aux
Entradas: dato
Salidas: transforma la lista a string
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
    print("\n")
    Abrir = open("Información de la empresa.txt","r")
    Abrir2 = Abrir.read()
    print(Abrir2)
    Abrir.close()
    print("\n")
    GestionEmpresas()
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
    Archivo3 = open(Archivo)
    Comprobar = Archivo3.readlines()
    if("Placa del transporte:"+Placa+"\n") in Comprobar:
        print("\n\t\t>>>>>La matricula ya existe<<<<<")
        return IncluirTransporte()
    else:
        Marca = input("\n\tEscriba la marca del transporte:")
        Modelo = input("\n\tEscriba el modelo del transporte:")
        Año = input("\n\tDígite el año del transporte:")
        Archivo3 = open("Información de la empresa.txt")
        Informacion = Archivo3.read()
        print("\n"+Informacion)
        Empresa = input("\n\tEscriba el nombre de la empresa:")
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
        print ("\n")
        GestionTransporte()

#--------------------------------------------------------------------------------------------------------------------
"""
Nombre: EliminarTransporte
Entradas: No posee entradas
Salidas: al escribir la placa del transporte se podrá eliminar los datos almacenados del transporte
Restricciones: No posee restricciones
"""
def EliminarTransporte():
    Placa = input("\n\tEscriba la placa del transporte:")
    print("\n")
    Almacen = open("Información del transporte.txt")
    Borrar = Almacen.readlines()
    if("Placa del transporte:"+Placa+"\n")in Borrar:
        ContarLineas = Borrar.index("Placa del transporte:"+Placa+"\n")
        Almacen2 = open("Información por viaje.txt")
        Linea = Almacen2.readlines()
        if("Placa del transporte:"+Borrar[ContarLineas][21:])in Linea:
            print("\n\t>>>>>El transporte está asociado a un viaje")
            print("\n\t1 - Eliminar transporte\n\n\t2 - Regresar a menu gestion transporte")
            submenu = input("\n\t>>>>>Seleccione una de las siguientes opciones:")
            if(submenu == "1"):
                return EliminarTransporte()
            else:
                return GestionTransporte()
        else:
            BorrarLineas = EliminarTransporte_aux(Borrar,ContarLineas,-5)
            Almacen.close()
            Abrir = open("Información del transporte.txt","w")
            Abrir.write(BorrarLineas)
            Abrir.close()
            print("\n\t\t>>>>>El transporte ha sido eliminado<<<<<")
            print ("\n")
            GestionTransporte()
    else:
        print("\n\t\t>>>>>El transporte no existe<<<<<")
        print ("\n")
        GestionTransporte()
"""
Nombre: EliminarTransporte_aux
Entradas: Borrar,ContarLineas,contador
Salidas:elimina el indice
Restricciones:no posee
"""
def EliminarTransporte_aux(Borrar,ContarLineas,contador):
    if contador == 5:
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
    if ("Placa del transporte:"+Placa+ "\n") in transporte:
        Indice = transporte.index("Placa del transporte:"+Placa+ "\n")
        Transporte2_aux(transporte,Indice,0)
        TransporteNuevo = Transporte3_aux(transporte,Indice+1,0)
        Abrir = open("Información del transporte.txt","w")
        Abrir.write(TransformarString_aux(TransporteNuevo))
        Abrir.close()
        print("\n\t\t>>>>>El transporte ha sido modificado<<<<<")
        print ("\n")
        GestionTransporte()
"""
Nombre: Transporte2_aux
Entradas: lista,Indice,contador
Salidas:imprime el indice de la lista
Restricciones:no posee
"""
def Transporte2_aux(lista,Indice,contador):
    if contador == 8:
        print("") 
    else:
        print("\n\t"+lista[Indice].rstrip())
        return Transporte2_aux(lista,Indice+1,contador+1)
"""
Nombre: Transporte3_aux
Entradas: Dato,Indice,contador
Salidas:modifica los datos del transporte
Restricciones:no posee
"""
def Transporte3_aux(Dato,Indice,contador):
    if contador > 6 :
        return Dato
    elif contador == 0:
        Dato2 = input("\n\tEscriba la marca del transporte:")
        Dato[Indice]=("Marca del transporte:"+Dato2+ "\n")
        return Transporte3_aux(Dato,Indice+1,contador+1)
    else:
        if contador == 1:
            Dato2 = input("\n\tEscriba el modelo del transporte:")
            Dato[Indice]=("Modelo del transporte:"+Dato2+ "\n")
            return Transporte3_aux(Dato,Indice+1,contador+1)
        elif contador == 2:
            Dato2 = input("\n\tDígite el año del transporte:")
            Dato[Indice]=("Año del transporte:"+Dato2+ "\n")
            return Transporte3_aux(Dato,Indice+1,contador+1)
        elif contador == 3:
            Archivo3 = open("Información de la empresa.txt")
            Informacion = Archivo3.read()
            print("\n"+Informacion)
            Dato2 = input("\n\tEscriba el nombre de la empresa:")
            Dato[Indice]=("Empresa del transporte:"+Dato2+ "\n")
            return Transporte3_aux(Dato,Indice+1,contador+1)
        elif contador == 4:
            Dato2 = input("\n\tCantidad de asientos clase VIP:")
            Dato[Indice]=("Cantidad de asientos clase VIP:"+Dato2+ "\n")
            return Transporte3_aux(Dato,Indice+1,contador+1)
        elif contador == 5: 
            Dato2 = input("\n\tCantidad de asientos clase normal:")
            Dato[Indice]=("Cantidad de asientos clase normal:"+Dato2+ "\n")
            return Transporte3_aux(Dato,Indice+1,contador+1)
        else:
            Dato2 = input("\n\tCantidad de asientos clase económica:")
            Dato[Indice]=("Cantidad de asientos clase económica:"+Dato2+ "\n")
            return Transporte3_aux(Dato,Indice+1,contador+1)
            
#---------------------------------------------------------------------------------------------------------------------
"""
Nombre: MostrarTransportes
Entradas: No posee entradas
Salidas: abre el archivo de texto "Información del transporte" y muestra su contenido
Restricciones:No posee restricciones
"""
def MostrarTransportes():
    print("\n")
    Abrir = open("Información del transporte.txt","r")
    Abrir2 = Abrir.read()
    print(Abrir2)
    Abrir.close()
    print ("\n")
    GestionTransporte()
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
    Archivo3 = open(Archivo)
    Archivo3 = Archivo3.readlines()
    NumeroViaje = numeroAutomatico(Archivo3,1)
    CiudadSalida = input("\n\tCiudad de salida:")
    FechaYHoraSalida = input("\n\tFecha y hora de salida:")
    CiudadLLegada = input("\n\tCiudad de llegada:")
    FechaYHoraLLegada = input("\n\tFecha y hora de llegada:")
    Archivo4 = open("Información del transporte.txt")
    Informacion = Archivo4.read()
    print("\n"+Informacion)
    Empresa = input("\n\tEscriba el nombre de la empresa:")
    Transporte = input("\n\tEscriba la placa del transporte:")
    MontoAsientoVIP = input("\n\tMonto de asiento VIP:")
    MontoAsientoNormal = input("\n\tMonto de asiento normal:")
    MontoAsientoEconomico = input("\n\tMonto de asiento económico:")
    Archivo2.write("Número de viaje:"+str(NumeroViaje)+"\n")
    Archivo2.write("Ciudad de salida:"+CiudadSalida+"\n")
    Archivo2.write("Fecha y hora de salida:"+FechaYHoraSalida+"\n")
    Archivo2.write("Ciudad de llegada:"+CiudadLLegada+"\n")
    Archivo2.write("Fecha y hora de llegada:"+FechaYHoraLLegada+"\n")
    Archivo2.write("Nombre de la empresa:"+Empresa+"\n")
    Archivo2.write("Placa del transporte:"+Transporte+"\n")
    Archivo2.write("Monto de asiento clase VIP:"+MontoAsientoVIP+"\n")
    Archivo2.write("Monto de asiento clase normal:"+MontoAsientoNormal+"\n")
    Archivo2.write("Monto de asiento clase económica:"+MontoAsientoEconomico+"\n")
    Archivo2.write("......................................"+"\n")
    Archivo2.close()
    print ("\n\t\t>>>>>El viaje ha sido almacenado<<<<<")
    print("\n")
    GestionViaje()

def numeroAutomatico(archivo,contador):
    if archivo == []:
        return contador//9+1
    else:
        return numeroAutomatico(archivo[1:],contador+1)
#--------------------------------------------------------------------------------------------------------------------
"""
Nombre: EliminarViaje
Entradas: No posee entradas
Salidas: al escribir el número del viaje se eliminarán los datos almacenados de la empresa
Restricciones:No posee restricciones
"""
def EliminarViaje():
    NumeroViaje = input("\n\tEscriba el número del viaje:")
    print("\n")
    Almacen = open("Información por viaje.txt")
    Borrar = Almacen.readlines()
    if("Número de viaje:"+NumeroViaje+ "\n")in Borrar:
        ContarLineas = Borrar.index("Número de viaje:"+NumeroViaje+ "\n")
        BorrarLineas = EliminarViaje_aux(Borrar,ContarLineas,0)
        Almacen.close()
        Abrir = open("Información por viaje.txt","w")
        Abrir.write(BorrarLineas)
        Abrir.close()
        print("\n\t\t>>>>>El viaje ha sido eliminado<<<<<")
        print("\n")
        GestionViaje()
    else:
        print("\n\t\t>>>>>El viaje no existe<<<<<")
        print("\n")
        GestionViaje()

def EliminarViaje_aux(Borrar,ContarLineas,contador):
    if contador == 11:
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
    if ("Número de viaje:"+NumeroViaje+ "\n") in viaje:
        Indice = viaje.index("Número de viaje:"+NumeroViaje+ "\n")
        Viaje2_aux(viaje,Indice,0)
        ViajeNuevo = Viaje3_aux(viaje,Indice+1,1)
        Abrir = open("Información por viaje.txt","w")
        Abrir.write(TransformarString_aux(ViajeNuevo))
        Abrir.close()
        print("\n\t\t>>>>>El viaje ha sido modificado<<<<<")
        print("\n")
        GestionViaje()
    else:
        print("\n\t\t>>>>>El viaje no existe<<<<<")
        return ModificarViaje()

def Viaje2_aux(lista,Indice,contador):
    if contador == 10:
        print("") 
    else:
        print("\n\t"+lista[Indice].rstrip())
        return Viaje2_aux(lista,Indice+1,contador+1)

def Viaje3_aux(Dato,Indice,contador):
    if contador > 9:
        return Dato
    elif contador == 1:
        Dato2 = input("\n\tCiudad de salida:")
        Dato[Indice]=("Ciudad de salida:"+Dato2+ "\n")
        return Viaje3_aux(Dato,Indice+1,contador+1)
    else:
        if contador == 2:
            Dato2 = input("\n\tFecha y hora de salida:")
            Dato[Indice]=("Fecha y hora de salida:"+Dato2+ "\n")
            return Viaje3_aux(Dato,Indice+1,contador+1)
        elif contador == 3:
            Dato2 = input("\n\tCiudad de llegada:")
            Dato[Indice]=("Ciudad de llegada:"+Dato2+ "\n")
            return Viaje3_aux(Dato,Indice+1,contador+1)
        elif contador == 4:
            Dato2 = input("\n\tFecha y hora de llegada:")
            Dato[Indice]=("Fecha y hora de llegada:"+Dato2+ "\n")
            return Viaje3_aux(Dato,Indice+1,contador+1)
        elif contador == 5:
            Archivo4 = open("Información del transporte.txt")
            Informacion = Archivo4.read()
            print("\n"+Informacion)
            Dato2 = input("\n\tEscriba el nombre de la empresa:")
            Dato[Indice]=("Nombre de la empresa:"+Dato2+ "\n")
            return Viaje3_aux(Dato,Indice+1,contador+1)
        elif contador == 6:
            Dato2 = input("\n\tEscriba la placa del transporte:")
            Dato[Indice]=("Placa del transporte:"+Dato2+ "\n")
            return Viaje3_aux(Dato,Indice+1,contador+1)
        elif contador == 7: 
            Dato2 = input("\n\tMonto de asiento VIP:")
            Dato[Indice]=("Monto de asiento VIP:"+Dato2+ "\n")
            return Viaje3_aux(Dato,Indice+1,contador+1)
        elif contador == 8: 
            Dato2 = input("\n\tMonto de asiento normal:")
            Dato[Indice]=("Monto de asiento normal:"+Dato2+ "\n")
            return Viaje3_aux(Dato,Indice+1,contador+1)
        else:
            Dato2 = input("\n\tMonto de asiento económico:")
            Dato[Indice]=("Monto de asiento económico:"+Dato2+ "\n")
            return Viaje3_aux(Dato,Indice+1,contador+1)
            
#---------------------------------------------------------------------------------------------------------------------
"""
Nombre: MostrarViajes
Entradas: No posee entradas
Salidas: abre el archivo de texto "Información por viaje" y muestra su contenido
Restricciones:No posee restricciones
"""
def MostrarViajes():
    print("\n")
    Abrir = open("Información por viaje.txt","r")
    Abrir2 = Abrir.read()
    print(Abrir2)
    Abrir.close()
    print("\n")
    GestionViaje()
#---------------------------------------------------------------------------------------------------------------------
"""
Nombre: ConsultarHistorial
Entradas:no posee
Salidas:imprime el menú de consulta el historial de reservaciones
Restricciones:
"""
#3.4
def ConsultarHistorial():
    print("\n\t1 - Rango de fecha de salida\n\n\t2 - Rango de fecha de llegada\n\n\t3 - Rango de fecha de la reservacion\n\n\t4 - Lugar de salida\n\n\t5 - Lugar de llegada\n\n\t6 - Salir")
    op = input("\n\t>>>>>Seleccione una de las siguientes opciones:")
    if(op == "1"):
        return RangoFechaSalida()
    elif(op == "2"):
        return RangoFechaLLegada()
    elif(op == "3"):
        return RangoReservacion()
    elif(op == "4"):
        return LugarDeSalida()
    elif(op == "5"):
        return LugarDeLLegada()
    elif(op == "6"):
        return menu2()
    else:
        print("\n\t>>>>>Seleccione una de las siguientes opciones:")
        return menu2()

def RangoFechaSalida():
    Salida = input("\n\tRango de fecha de salida:")
    print("\n")
    datos = datos_aux()
    Buscar1(datos,Salida,5,False,5)
    print("\n")
    ConsultarHistorial()

def datos_aux():
    Abrir = open("Información de reservación.txt")
    Almacenar = Abrir.readlines()
    Abrir.close()
    return Almacenar

def Buscar1(reservacion,filtrar,indice,verificar,linea):
    if indice > len(reservacion):
        if verificar :
            return print("\n\t>>>>>La reservacion ha sido encontrada<<<<<")
        else:
            print("\n\t>>>>>La reservacion no fue encontrada<<<<<<")
    else:
        if filtrar in reservacion[indice]:
            BuscarReservacion(reservacion,indice-linea,0)
            return Buscar1(reservacion,filtrar,indice+15,True,linea)
        else:
            return Buscar1(reservacion,filtrar,indice+15,verificar,linea)

def BuscarReservacion(reservacion,indice,contador):        
    if contador > 14:
        print("")
    else:
        print(reservacion[indice].rstrip())
        return BuscarReservacion(reservacion,indice+1,contador+1)

def RangoFechaLLegada():
    Llegada = input("\n\tRango de fecha de llegada:")
    print("\n")
    datos = datos_aux()
    Buscar1(datos,Llegada,7,False,7)
    print("\n")
    ConsultarHistorial()

def RangoReservacion():
    Reservacion = input("\n\tRango de fecha de la reservacion:")
    print("\n")
    datos = datos_aux()
    Buscar1(datos,Reservacion,11,False,11)
    print("\n")
    ConsultarHistorial()

def LugarDeSalida():
    LugarSalida = input("\n\tLugar de salida:")
    print("\n")
    datos = datos_aux()
    Buscar1(datos,LugarSalida,4,False,4)
    print("\n")
    ConsultarHistorial()

def LugarDeLLegada():
    LugarLLegada = input("\n\tLugar de llegada:")
    print("\n")
    datos = datos_aux()
    Buscar1(datos,LugarLLegada,6,False,6)
    print("\n")
    ConsultarHistorial()
#---------------------------------------------------------------------------------------------------------------------
"""
Nombre: Estadisticas()
Entradas: no posee
Salidas:muestra la información de los viajes existentes
Restricciones:no posee
"""
#3.5
def Estadisticas():
    print("\n")
    Archivo = open("Información por viaje.txt")
    Leer = Archivo.read()
    print(Leer)
    Usuario = input("\n\t>>>>>Escriba el numero del viaje:")
    print("\n")
    Abrir = open("Información por viaje.txt")
    Listas = Abrir.readlines()
    Indice = ubicarIndice(Listas,"Número de viaje:"+Usuario+"\n",0)
    print(Listas[Indice])
    print(Listas[Indice+5])
    print(Listas[Indice+6])
    print(Listas[Indice+1])
    print(Listas[Indice+2])
    print(Listas[Indice+3])
    print(Listas[Indice+4])
    Archivo2 = open("Información de reservación.txt")
    Listas2 = Archivo2.readlines()
    Indice2 = ubicarIndice(Listas,"Número de viaje:"+Usuario+"\n",0)
    print("Cantidad de asientos clase VIP reservados:"+(Listas2[Indice2+8][36:-1])+"\n")
    print("Cantidad de asientos clase normal reservados:"+(Listas2[Indice2+9][41:-1])+"\n")
    print("Cantidad de asientos clase económica reservados:"+(Listas2[Indice2+10][43:-1])+"\n")
    print(Listas[Indice+7])
    Archivo3 = open("Información del transporte.txt")
    Listas3 = Archivo3.readlines()
    Indice3 = ubicarIndice(Listas,"Placa del transporte:"+Usuario+"\n",0)
    print(Listas3[Indice3+5])#vip transporte
    print(Listas3[Indice3+6])#normal transporte
    print(Listas3[Indice3+7])#economico transporte
    Resta = int(Listas3[Indice3+5][31:-1])-(int(Listas2[Indice2+8][36:-1]))
    print("Cantidad de asientos clase VIP disponibles:"+str(Resta)+"\n")
    Resta2 = int(Listas3[Indice3+6][34:-1])-(int(Listas2[Indice2+9][41:-1]))
    print("Cantidad de asientos clase normal disponibles:"+str(Resta2)+"\n")
    Resta3 = int(Listas3[Indice3+7][37:-1])-(int(Listas2[Indice2+10][43:-1]))
    print("Cantidad de asientos clase económica disponibles:"+str(Resta)+"\n")
    Suma =int(Listas2[Indice2+8][36:-1])*(int(Listas[Indice+7][27:-1]))
    Suma2 = int(Listas2[Indice2+9][41:-1])*(int(Listas[Indice+8][30:-1]))
    Suma3 = int(Listas2[Indice2+10][43:-1])*(int(Listas[Indice+9][33:-1]))
    Total = Suma+Suma2+Suma3
    print("Monto recaudado por el viaje:"+str(Total)+"\n")
    print("\n")
    menu2()
    
    
    
    
#---------------------------------------------------------------------------------------------------------------------
"""
Nombre:ConsultaViajes
Entradas:No posee
Salidas:imprime el menú de colsulta de viajes 
Restricciones:no posee
"""
#4.1
def ConsultaViajes():
    print("\n\t1 - Empresa\n\n\t2 - Lugar de salida\n\n\t3 - Lugar de llegada\n\n\t4 - Rango de fecha de salida\n\n\t5 - Rango de fecha de llegada\n\n\t6 - Salir")
    op = input("\n\t>>>>>Seleccione una de las siguientes opciones:")

    if(op == "1"):
        return Empresa()
    elif(op == "2"):
        return LugarSalida()
    elif(op == "3"):
        return LugarLLegada()
    elif(op == "4"):
        return RangoSalida()
    elif(op == "5"):
        return RangoLLegada()
    elif(op == "6"):
        return menu3()
    else:
        print("\n\t>>>>>Seleccione una de las siguientes opciones:")
        return menu3()
    
def Empresa():
    Empresa = input("\n\tEmpresa:")
    print("\n")
    datos = datos1()
    Buscar(datos,Empresa,5,False,5)
    print("\n")
    ConsultaViajes()

def datos1():
    Abrir = open("Información por viaje.txt")
    Almacenar = Abrir.readlines()
    Abrir.close()
    return Almacenar

def Buscar(viajes,filtrar,indice,verificar,linea):
    if indice > len(viajes):
        if verificar :
            return print("\n\t\t>>>>>El viaje fue encontrado<<<<<")
        else:
            print("\n\t\t>>>>>El viaje no fue encontrado<<<<<<")
    else:
        if filtrar in viajes[indice]:
            BuscarViaje(viajes,indice-linea,0)
            return Buscar(viajes,filtrar,indice+12,True,linea)
        else:
            return Buscar(viajes,filtrar,indice+12,verificar,linea)

def BuscarViaje(viajes,indice,contador):        
    if contador > 9:
        print("")
    else:
        print(viajes[indice].rstrip())
        return BuscarViaje(viajes,indice+1,contador+1)

def LugarSalida():
    CiudadSalida = input("\n\tLugar de salida:")
    print("\n")
    datos = datos1()
    Buscar(datos,CiudadSalida,1,False,1)
    print("\n")
    ConsultaViajes()

def RangoSalida():
    FechaYHoraSalida = input("\n\tRango de salida:")
    print("\n")
    datos = datos1()
    Buscar(datos,FechaYHoraSalida,2,False,2)
    print("\n")
    ConsultaViajes()

def LugarLLegada():
    CiudadLLegada = input("\n\tLugar de llegada:")
    print("\n")
    datos = datos1()
    Buscar(datos,CiudadLLegada,3,False,3)
    print("\n")
    ConsultaViajes()

def RangoLLegada():
    FechaYHoraLLegada = input("\n\tRango de llegada:")
    print("\n")
    datos = datos1()
    Buscar(datos,FechaYHoraLLegada,4,False,4)
    print("\n")
    ConsultaViajes()
#---------------------------------------------------------------------------------------------------------------------
"""
Nombre:Reservacion
Entradas:No posee
Salidas: Hace la reservación de viaje
Restricciones:validar que existan espacios disponibles en cada categoria 
"""
#4.2
def Reservacion():
    from datetime import datetime 
    Archivo2 = open("Información de reservación.txt","a") 
    Archivo2.close()
    print("\n\t\tInformación de reservación")
    Archivo3 = open("Información por viaje.txt")
    Informacion = Archivo3.read()
    print("\n"+Informacion)
    Abrir = open("Información por viaje.txt")
    Archivo3 = Abrir.readlines()
    Viaje = input("\n\tDígite el número del viaje:")
    Archivo4 = ubicarIndice(Archivo3,"Número de viaje:"+Viaje+"\n",0)
    Empresa = Archivo3[Archivo4+5][21:-1]
    Transporte = Archivo3[Archivo4+6][21:-1]
    LugarSalida = Archivo3[Archivo4+1][17:-1]
    FechaYHoraSalida = Archivo3[Archivo4+2][23:-1]
    LugarLLegada = Archivo3[Archivo4+3][18:-1]
    FechaYHoraLLegada = Archivo3[Archivo4+4][24:-1]
    Nombre = input("\n\tEscriba su nombre:")
    CantidadVIP = input("\n\tCantidad de espacios a reservar VIP:")
    Placa = Archivo3[Archivo4+6][21:-1]
    Archivo5 = open("Información del transporte.txt")
    Archivo5 = Archivo5.readlines()
    Indice = Archivo5.index("Placa del transporte:"+Placa+"\n")
    VIPdisponible = Archivo5[Indice+5][31:-1]
    if int(VIPdisponible) - int(CantidadVIP)>= 0:
        CantidadNormal = input("\n\tCantidad de espacios a reservar normal:")
        NormalDisponible = Archivo5[Indice+6][34:-1]
        if int(NormalDisponible) - int(CantidadNormal)>= 0:
            CantidadEconomico = input("\n\tCantidad de espacios a reservar económicos:")
            EconomicoDisponible = Archivo5[Indice+7][37:-1]
            if int(EconomicoDisponible) - int(CantidadEconomico)>= 0:
                Monto = int(CantidadVIP)*(int(Archivo3[Archivo4+7][27:-1]))
                Monto2 = int(CantidadNormal)*(int(Archivo3[Archivo4+8][30:-1]))
                Monto3 = int(CantidadEconomico)*(int(Archivo3[Archivo4+9][33:-1]))
                Archivo = "Información de reservación.txt"
                Archivo2 = open(Archivo)
                lineas = Archivo2.readlines()
                Identificador = identificador(lineas,0)
                FechaHora = datetime.now()
                Archivo2 = open("Información de reservación.txt","a") 
                Archivo2.write("Numero del viaje:"+Viaje+"\n")
                Archivo2.write("Nombre de persona que reserva:"+Nombre+"\n")
                Archivo2.write("Empresa:"+Empresa+"\n")
                Archivo2.write("Transporte:"+Transporte+"\n")
                Archivo2.write("Lugar de salida:"+LugarSalida+"\n")
                Archivo2.write("Fecha y hora de salida:"+FechaYHoraSalida+"\n")
                Archivo2.write("Lugar de llegada:"+LugarLLegada+"\n")
                Archivo2.write("Fecha y hora de llegada:"+FechaYHoraLLegada+"\n")
                Archivo2.write("Cantidad de espacios VIP reservados:"+CantidadVIP+"\n")
                Archivo2.write("Cantidad de espacios normales reservados:"+CantidadNormal+"\n")
                Archivo2.write("Cantidad de espacios economicos reservados:"+CantidadEconomico+"\n")
                Archivo2.write("Fecha y hora de la reservacion:"+str(FechaHora)+"\n")
                Archivo2.write("Monto de reservacion:"+str(Monto+Monto2+Monto3)+"\n")
                Archivo2.write("Identificador:"+str(Identificador)+"\n")
                Archivo2.write("......................................................."+"\n")
                Archivo2.close()
                print("\n\t\t>>>>>Se ha realizado la reservación<<<<<")

                print("\n")
                menu3()
    
def ubicarIndice(listas,buscar,contador):
    if listas == []:
        return False
    elif buscar in listas[0]:
        return contador
    else:
        return ubicarIndice(listas[1:],buscar,contador+1)
        
def identificador(lineas,contador):
    if lineas == []:
        return contador//14+1
    else:
        return identificador(lineas[1:],contador+1) 
#---------------------------------------------------------------------------------------------------------------
"""
Nombre:Cancelacion
Entradas:no posee
Salidas:cancela la reservación
Restricciones:se debe liberar los asientos reservados
"""
#4.3    
def Cancelacion():
    Dato = input("\n\t>>>>>Ingrese el número del identificador:")
    Buscar = open("Información de reservación.txt")
    Archivo = Buscar.readlines()
    if("Identificador:"+Dato+"\n")in Archivo:
       Indice = ubicarIndice(Archivo,("Identificador:"+Dato+"\n"),0)
       Eliminar = eliminarListas(Archivo,Indice-13,0)
       Buscar.close()
       Abrir = open("Información de reservación.txt","w")
       Abrir.write(Eliminar)
       Abrir.close()
       print("\n\t\t>>>>>Se ha cancelado la recervacion<<<<<")
       print("\n")
       menu3()

def eliminarListas(archivo,indice,contador):
    if contador > 14:
        return TransformarString_aux(archivo)
    else:
        archivo.pop(indice)
        return eliminarListas(archivo,indice,contador+1)

SistemaDeReservación()
