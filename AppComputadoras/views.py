""" Librerias  """
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
from rest_framework import generics
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
# Modelos y serializers
# ---------------------------------------------------------------
from AppComputadoras.serializers import *
from AppComputadoras.models import *
# ---------------------------------------------------------------
# Otras Librerias
# ---------------------------------------------------------------
from django.core.files.storage import default_storage
from pathlib import *
# ---------------------------------------------------------------


"""
Clase para la creacion de un Mouse a traves de la API
class Mouse()
    mouse = class(objects)
    Se crea API AppComputers_API_CrearMouse con los atributos del objeto Mouse
    @process files
    Toma la dataMouse para crear una ruta en donde se guardara los files, y se lo distingue por el serial del mouse
"""
class AppComputers_API_CrearMouse(APIView):
    # Metodo POST
    def post(self, request, format = None):
        # Crear un objeto MouseSerializers con los datos de entrada
        serializer = MouseSerializers(data = request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            mouse = Mouse(**validated_data)
            mouse.save()
            serializer_response = MouseSerializers(mouse)
            return Response(serializer_response.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
    # Obtener todos los datos del mouse
    def get(self, request, format =None):
        mouses = Mouse.objects.all()
        serializer = MouseSerializers(mouses, many=True)
        print(serializer.data)
        return Response(serializer.data)

    # Metodo PUT
    def put(self, request, pk, format = None):
        try:
            mouse = Mouse.objects.get(pk = pk)
            serializers =  MouseSerializers(mouse, data = request.data)
            serializers.is_valid(raise_exception = True)
            serializers.save()
            return  Response(serializers.data)
        except Mouse.DoesNotExist:
            return Response("El mouse no existe", status = status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"Error": str(e)}, status = status.HTTP_400_BAD_REQUEST)

    # Metodo DELETE    
    def delete(self, request, pk, format = None):
        try:
            mouse = Mouse.objects.get(pk = pk)
            mouse.delete()
            return Response({"Msg": 'Registro eliminado correctamente'}, status = status.HTTP_200_OK)
        except Mouse.DoesNotExist:
            return Response({"Error": "La ciudad no existe"}, status = status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response ({"Error": str(e)}, status = status.HTTP_400_BAD_REQUEST)
        
# ---------------------------------------------------------------------------------------------------------------------------#
        
class AppComputers_API_CrearTeclado(APIView):
    # Metodo POST (Agregar un nuevo teclado)
    def post(self, request, format = None):
        serializer = TecladoSerializers(data = request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            teclado = Teclado(**validated_data)
            teclado.save()
            serializer_response = TecladoSerializers(teclado)
            return Response(serializer_response.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    # Metodo GET (Mirar datos de un teclado)
    def get(self, request, format =None):
        try:
            teclado = Teclado.objects.all()
            serializer = TecladoSerializers(teclado, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"Error": str(e)}, status = status.HTTP_400_BAD_REQUEST)
    
    # Metodo  PUT (Actualizar datos de un teclado)
    def put(self, request, pk, format=None):
        try:
            teclado = Teclado.objects.get(pk = pk)
            serializer = TecladoSerializers(teclado, data = request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        except Teclado.DoesNotExist:
            return Response({"Error": "El teclado no existe"}, status = status.HTTP_404_NOT_FOUND)
        except  Exception as e:
            return Response({"Error": str(e)}, status = status.HTTP_400_BAD_REQUEST)
    
    # Metodo DELETE(Eliminar un teclado)
    def delete(self, request, pk ,format = None):
        try:
            teclado = Teclado.objects.get(pk = pk)
            teclado.delete()
            return Response({"Msg": "Registro eliminado conrrectamente"}, status =  status.HTTP_200_OK)
        except Teclado.DoesNotExist:
            return Response({"Error":"El teclado no existe"}, status = status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return  Response({'error':str(e)}, status = status.HTTP_400_BAD_REQUEST)

# ---------------------------------------------------------------------------------------------------------------------------#     
        
class AppComputers_API_CrearMonitor(APIView):
    # Metodo POST
    def post(self, request, format = None):
        serializer = MonitorSerializers(data = request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            monitor = Monitor(**validated_data)
            monitor.save()
            serializer_response = MonitorSerializers(monitor)
            return Response(serializer_response.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
    # Metodo GET
    def get(self, request, format = None):
        try:
            teclado = Monitor.objects.all()
            serializer = MonitorSerializers(teclado, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"Error": str(e)}, status = status.HTTP_400_BAD_REQUEST)
    
    # Metodo PUT
    def put(self, request, pk, format = None):
        try:
            monitor = Monitor.objects.get(pk = pk)
            serializer = MonitorSerializers(monitor, data = request.data)
            serializer.is_valid(raise_exception = True)
            serializer.save()
            return Response(serializer.data)
        except Monitor.DoesNotExist:
            return Response({"Error": "El monitor no existe"}, status = status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"Error": str(e)}, status = status.HTTP_400_BAD_REQUEST)
    
    # Metodo DELETE
    def delete(self, request, pk, format = None):
        try:
            monitor = Monitor.objects.get(pk = pk)
            monitor.delete()
            return Response({"Msg": "Registro eliminado correctamente"}, status = status.HTTP_200_OK)
        except Monitor.DoesNotExist:
            return Response({"Error":"El monitor no existe"} , status = status.HTTP_404_NOT_FOUND) 
        except Exception as e:
            return Response({"Error":str(e)}, status = status.HTTP_400_BAD_REQUEST)  

# ---------------------------------------------------------------------------------------------------------------------------#
        
class AppComputers_API_CrearTorre(APIView):
     # Metodo POST
    def post(self, request, format = None):
        serializer = TorreSerializers(data = request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            torre = Torre(**validated_data)
            torre.save()
            serializer_response = TorreSerializers(torre)
            return Response({"Mensaje: ":"Torre Creada 🚀"}, status=status.HTTP_201_CREATED)
        return Response({"Mensaje":"!Ups¡ no se pudo realizar la acción.", "Error":serializer.errors}, status= status.HTTP_400_BAD_REQUEST)
    
    # Metodo GET
    def get(self, request, format = None):
        torre = Torre.objects.all()
        serializer = TorreSerializers(torre, many=True)
        return Response(serializer.data)
    
    # Metodo  PUT 
    def put(self, request, pk, format = None):
        try:
            torre = Torre.objects.get(pk = pk)
            serializer = TorreSerializers(torre, data = request.data)
            serializer.is_valid(raise_exception = True)
            torre = serializer.save()
            return Response(serializer.data)
        except Torre.DoesNotExist:
            return Response({'Error': "La torre no existe"}, status = status.HTTP_404_NOT_FOUND)
        except  Exception as e:
            return Response({"Error": str(e)}, status = status.HTTP_400_BAD_REQUEST)
    
    # Metodo Delete 
    def delete(self, request, pk ,format = None):
        try:
            torre = Torre.objects.get(pk = pk)
            torre.delete()
            return Response({"Msg": "Registro eliminado correctamente"}, status = status.HTTP_200_OK)
        except Torre.DoesNotExist:
            return Response({"Error":"No se existe la torre"}, status = status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response( {"Error":str(e)}, status=status.HTTP_400_BAD_REQUEST)

# ---------------------------------------------------------------------------------------------------------------------------#
        
# class AppComputers_API_CiudadSede(APIView):
#     def post(self, request, format = None):
#         try:
#             # Crea dos objetos CiudadSerializers, SedeSerializers con los datos de entrada
#             serializerCiudad = CiudadSerializers(data = request.data)
#             serializerSede = SedeSerializers(data = request.data)

#             if serializerCiudad.is_valid() and serializerSede.is_valid():
#                 dataCiudad = request.data
#                 dataSede = request.data
#                 # Crea una ciudad con los datos de entrada y los guarda en la base de datos
#                 ciudad = Ciudad(
#                     nombre_ciudad = dataCiudad['nombre_ciudad']
#                 )
#                 # Crea una sede con los datos de entrada y los guarda en la base de datos
#                 sede = Sede(
#                     nombre_sede = dataSede['nombre_sede'],
#                     ciudad = ciudad
#                 )
#                 ciudad.save()
#                 sede.save()
#             return Response ({'mensaje': 'Se creo exitosamente'})
#         except Exception as e:
#             return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

# ---------------------------------------------------------------------------------------------------------------------------#

class AppComputers_API_Ciudad(APIView):
    # Metodo POST
    def post(self, request, format = None):
        try:
            # Crea dos objetos CiudadSerializers, SedeSerializers con los datos de entrada
            serializerCiudad = CiudadSerializers(data = request.data)
            if serializerCiudad.is_valid():
                dataCiudad = request.data
                # Crea una ciudad con los datos de entrada y los guarda en la base de datos
                ciudad = Ciudad(
                    nombre_ciudad = dataCiudad['nombre_ciudad']
                )
                ciudad.save()
            return Response ({'mensaje': 'Se creo exitosamente'})
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    # Metodo GET
    def get(self, request, format=None):
        try:
            ciudades = Ciudad.objects.all()
            serializer = CiudadSerializers(ciudades, many = True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status = status.HTTP_400_BAD_REQUEST)
    
    # Metodo PUT    
    def put(self, request, pk, format = None):
        try:
            ciudad = Ciudad.objects.get(pk = pk)
            serializers = CiudadSerializers(ciudad, data = request.data)
            serializers.is_valid(raise_exception = True)
            serializers.save()
            return Response(serializers.data)
        except Ciudad.DoesNotExist:
            return Response("La ciudad no existe", status = status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"Error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    # Metodo DELETE    
    def delete(self, request, pk, format = None):
        try:
            ciudad = Ciudad.objects.get(pk = pk)
            ciudad.delete()
            return Response({"Msg": 'Registro eliminado correctamente'}, status = status.HTTP_200_OK)
        except Ciudad.DoesNotExist:
            return Response({"Error": "La ciudad no existe"}, status = status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response ({"Error": str(e)}, status = status.HTTP_400_BAD_REQUEST)

# ---------------------------------------------------------------------------------------------------------------------------#

class AppComputers_API_CrearSede(APIView):

    def post(self, request, format=None):
        try:
            serializerSede = SedeSerializers(data = request.data)
            if serializerSede.is_valid():
                dataSede = request.data
                miCiduad = Ciudad.objects.get(id = dataSede['ciudad'])
                if miCiduad:
                    sede = Sede(
                    nombre_sede = dataSede['nombre_sede'],
                    ciudad = miCiduad
                    )
                    sede.save()
            return Response ({'Mensaje': 'Se creo correctamente'}, status = status.HTTP_200_OK)
        except Exception as e:
            return Response ({'Error': str(e)}, status = status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, format = None):
        try:
            sedes = Sede.objects.all()
            serializer = SedeSerializers(sedes, many = True)
            return Response(serializer.data)
        except Exception as e:
            return Response ({'Error': str(e)}, status = status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, pk, format=None):
        try:
            sede = Sede.objects.get(pk=pk)
            serializer = SedeSerializers(sede, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Sede.DoesNotExist:
            return Response("La sede no existe", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)    
        
    def delete(self, request, pk, format = None):
        try:
            sede = Sede.objects.get(pk = pk)
            sede.delete()
            return Response({"Msg": "Registro eliminado Correctamente"}, status = status.HTTP_200_OK)
        except Sede.DoesNotExist:
            return Response({"Error": "La sede no existe"}, status = status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response ({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

# ---------------------------------------------------------------------------------------------------------------------------#

class AppComputers_API_CrearArea(APIView):
    # Metodo POST
    def post(self, request, format =  None):
        try:
            # Crea un objeto AreaSerializers con los datos de entrada
            serializer = AreaSerializers(data = request.data)
            if serializer.is_valid():
                dataArea = request.data
                miSede = Sede.objects.get(id = dataArea['sedes'])
                if miSede:
                    area = Area(
                    nombre_area = dataArea['nombre_area'],
                    sedes = miSede
                    )
                    area.save()
            return Response ({'mensaje': 'Se creo correctamente'})
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    # Metodo GET   
    def get(self, request, format=None):
        try:
            areas = Area.objects.all()
            serializer = AreaSerializers(areas, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    # Metodo PUT    
    def put(self, request, pk, formato = None):
        try:
            area = Area.objects.get(pk=pk)
            serializer = AreaSerializers(area, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        except Area.DoesNotExist:
            return Response({"Error": "La area no existe"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"Error": str(e)}, status=status.HTTP_400_BAD_REQUEST)  
    
    # Metodo DELETE
    def  delete(self, request, pk, format=None):
        try:
            area = Area.objects.get(pk=pk)
            area.delete()
            return Response({"Msg":"Registro eliminado correctamente"} , status = status.HTTP_200_OK)
        except Area.DoesNotExist:
            return Response({"Error":"El area no  existe"} , status = status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response ({'Error': str(e)}, status = status.HTTP_400_BAD_REQUEST)

# ---------------------------------------------------------------------------------------------------------------------------#

class AppComputers_API_CrearWorkstation(APIView):
    #Metodo POST
    def post(self, request, format = None):
        try:
            # Crea un objeto WorkstationSerializers con los datos de entrada
            serializer = WorkstationSerializers(data = request.data)

            if serializer.is_valid():
                dataWorkstation = request.data
                # Crea un objeto Workstation con los datos de entrada
                workstation = Workstation(
                    puesto_trabajo = dataWorkstation['puesto_trabajo']
                )
                workstation.save()
            return Response ({'mensaje': 'Se creo el workstation'})
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    # Metodo GET
    def get(self, request,  format = None):
        try:
            Puestos_de_Trabajo =  Workstation.objects.all()
            serializer = WorkstationSerializers(Puestos_de_Trabajo, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    # Metodo PUT    
    def put(self, request , pk , format = None):
        try:
            Puesto_de_Trabajo = Workstation.objects.get(pk = pk)
            serializer = WorkstationSerializers(Puesto_de_Trabajo, data = request.data)
            serializer.is_valid(raise_exception = True)
            serializer.save()
            return Response(serializer.data)
        except Workstation.DoesNotExist:
            return Response({"Error": "La workstation no existe"}, status = status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"Error": str(e)}, status = status.HTTP_400_BAD_REQUEST)

    # Metodo  DELETE  
    def delete(self,request,pk,format=None):
        try:
            Puesto_de_Trabajo = Workstation.objects.get(pk =pk)
            Puesto_de_Trabajo.delete()
            return Response ({"Msg":"Registro eliminado correctamente"} , status = status.HTTP_200_OK)
        except Workstation.DoesNotExist:
            return Response ({"Error": "La workstation no existe"}, status = status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response ({"Error":str(e)}, status = status.HTTP_400_BAD_REQUEST)

# ---------------------------------------------------------------------------------------------------------------------------#
        
class AppComputers_API_CrearComputador(APIView):
    # Metodo  POST
    """def post(self, request, format = None):
        try:
            # Crea un objeto ComputadorSerializers con los datos de entrada
            serializerComputador = ComputadorSerializers(data = request.data)
            if serializerComputador.is_valid():
                dataComputador = request.data
                miArea =  Area.objects.get(id = dataComputador['area'])
                miWorkstation = Workstation.objects.get(id = dataComputador['workstation'])
                miMonitor = Monitor.objects.get(id = dataComputador['monitor'])
                miTeclado = Teclado.objects.get(id = dataComputador['teclado'])
                miMouse = Mouse.objects.get(id = dataComputador['mouse'])
                miTorre = Torre.objects.get(id = dataComputador['torre'])
                miResponsable = Responsable.objects.get(id = dataComputador['responsable'])
                # Se crea el computador cons sus respectivos parametros
                computador = Computador(
                    area = miArea,
                    workstation = miWorkstation,
                    monitor = miMonitor,
                    teclado = miTeclado,
                    mouse = miMouse,
                    torre = miTorre,
                    responsable = miResponsable,
                )
                computador.save()
            return Response ({'mensaje': 'Se creo el computador'})
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)"""
    def post(self, request, format=None):
        try:
            serializerComputador = ComputadorSerializers(data=request.data)
            if serializerComputador.is_valid():
                dataComputador = request.data

                # Verificar si los campos necesarios están presentes
                required_fields = ['area', 'workstation', 'monitor', 'teclado', 'mouse', 'torre', 'responsable']
                if not all(field in dataComputador for field in required_fields):
                    return Response({'error': 'Faltan campos requeridos'}, status=status.HTTP_400_BAD_REQUEST)

                # Obtener objetos relacionados
                miArea = Area.objects.get(id=dataComputador['area'])
                miWorkstation = Workstation.objects.get(id=dataComputador['workstation'])
                miMonitor = Monitor.objects.get(id=dataComputador['monitor'])
                miTeclado = Teclado.objects.get(id=dataComputador['teclado'])
                miMouse = Mouse.objects.get(id=dataComputador['mouse'])
                miTorre = Torre.objects.get(id=dataComputador['torre'])
                miResponsable = Responsable.objects.get(id=dataComputador['responsable'])

                # Crear el objeto Computador
                computador = Computador(
                    area=miArea,
                    workstation=miWorkstation,
                    monitor=miMonitor,
                    teclado=miTeclado,
                    mouse=miMouse,
                    torre=miTorre,
                    responsable=miResponsable,
                )
                computador.save()
                return Response({'mensaje': 'Se creó el computador'})
            else:
                return Response(serializerComputador.errors, status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist as e:
            return Response({'error': 'Uno o más objetos relacionados no existen'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


    # Metodo GET
    def get(self, request, format = None):
        try:
            computadores = Computador.objects.all()
            serializer = ComputadorSerializers(computadores, many = True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    # Metodo PUT
    def put(self, request, pk, format = None):
        try:
            computador = Computador.objects.get(pk = pk)
            serializer = ComputadorSerializers(computador, data = request.data)
            serializer.is_valid(raise_exception = True)
            serializer.save()
            return Response(serializer.data)
        except Computador.DoesNotExist:
            return Response('La impresora no existe', status = status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    # Metodo DElETE
    def delete(self, request, pk, format = None):
        try:
            computador = Computador.objects.get(pk = pk)
            computador.delete()
            return Response({"Msg": 'Registro eliminado correctamente'}, status = status.HTTP_200_OK)
        except Computador.DoesNotExist:
            return Response({"Error": "Los accesorios no existen"}, status = status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'Error': str(e)}, status = status.HTTP_400_BAD_REQUEST)
# ---------------------------------------------------------------------------------------------------------------------------#
 
class AppComputers_API_CrearImpresora(APIView):
    # Metodo POST
    def post(self, request, format = None):
        try:
            # Crea un objeto ImpresorasSerializers con los datos de entrada.
            serializerImpresora = ImpresorasSerializers(data = request.data)
            if serializerImpresora.is_valid():
                dataImpresora = request.data
                miComputador = Computador.objects.get(id = dataImpresora['computador'])
                if miComputador:
                    impresora = Impresoras(
                    computador = miComputador,
                    codigo_interno_impresora = dataImpresora['codigo_interno_impresora'],
                    nombre_impresora = dataImpresora['nombre_impresora'],
                    modelo_impresora = dataImpresora['modelo_impresora'],
                    serial_impresora = dataImpresora['serial_impresora'],
                    descripcion_impresora = dataImpresora['descripcion_impresora'],
                    fecha_adquisicion_impresora = dataImpresora['fecha_adquisicion_impresora'],
                    fecha_instalacion_impresora = dataImpresora['fecha_instalacion_impresora'],
                    fecha_garantia_impresora = dataImpresora['fecha_garantia_impresora'],
                    registro_fotografico_impresora = dataImpresora['registro_fotografico_impresora'],
                    foto_requisicion_impresora = dataImpresora['foto_requisicion_impresora'],
                    foto_acta_salida_impresora = dataImpresora['foto_acta_salida_impresora'],
                    foto_acta_recepcion_impresora = dataImpresora['foto_acta_recepcion_impresora'],
                    foto_factura_impresora = dataImpresora['foto_factura_impresora']
                    )
                    impresora.save()
                return Response ({'Mensaje': 'Se creo correctamente'}, status = status.HTTP_200_OK)
        except Exception as e:
            return Response ({'Error': str(e)}, status = status.HTTP_400_BAD_REQUEST)
    
    # Metodo GET
    def get(self, request, format = None):
        try:
            impresoras = Impresoras.objects.all()
            serializer = ImpresorasSerializers(impresoras, many = True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'Error':str(e)}, status = status.HTTP_400_BAD_REQUEST) 

    # Metodo PUT
    def put(self, request, pk, format = None):
        try:
            impresora = Impresoras.objects.get(pk = pk)
            serializers = ImpresorasSerializers(impresora, data = request.data)
            if serializers.is_valid(raise_exception = True):
                serializers.save()
                return Response(serializers.data, status = status.HTTP_200_OK)
            else:
                return Response(serializers.errors, status = status.HTTP_400_BAD_REQUEST)
        except Impresoras.DoesNotExist:
            return  Response({'Error': 'No existe la impresora'}, status = status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'Error':str(e)}, status = status.HTTP_400_BAD_REQUEST)

    # Metodo DELETE
    def delete(self, request, pk, format = None):
        try: 
            impresora = Impresoras.objects.get(pk = pk)
            impresora.delete()
            return Response({"Msg": 'Registro eliminado correctamente'}, status = status.HTTP_200_OK)
        except Impresoras.DoesNotExist:
            return Response({"Error": "La impresora no existe"}, status = status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response ({"Error": str(e)}, status = status.HTTP_400_BAD_REQUEST)
        
# ---------------------------------------------------------------------------------------------------------------------------#

class AppComputers_API_CrearAccesorio(APIView):
    # Metodo POST
    """def post(self, request, format = None):
        try:
            # Crea un objeto AccesoriosSerializers con los datos de entrada
            serializerAccesorio = AccesoriosSerializers(data = request.data)
            if serializerAccesorio.is_valid():
                dataAccesorio = request.data
                miComputador = Computador.objects.get(id = dataAccesorio['computador'])
                if miComputador:
                    accesorio = Accesorios(
                    codigo_interno_accesorio = dataAccesorio['codigo_interno_accesorio'],
                    nombre_accesorio = dataAccesorio['nombre_accesorio'],
                    serial_accesorio = dataAccesorio['serial_accesorio'],
                    modelo_accessorio = dataAccesorio['modelo_accessorio'],
                    marca_accesorio = dataAccesorio['marca_accesorio'],
                    descripcion_accesorio = dataAccesorio['descripcion_accesorio'],
                    fecha_adquisicion_accesorio = dataAccesorio['fecha_adquisicion_accesorio'],
                    fecha_instalacion_accesorio = dataAccesorio['fecha_instalacion_accesorio'],
                    fecha_garantia_accesorio = dataAccesorio['fecha_garantia_accesorio'],
                    registro_fotografico_accesorio = dataAccesorio['registro_fotografico_accesorio'],
                    foto_requisicion_accesorio = dataAccesorio['foto_requisicion_accesorio'],
                    foto_acta_salida_accesorio = dataAccesorio['foto_acta_salida_accesorio'],
                    foto_acta_recepcion_accesorio = dataAccesorio['foto_acta_recepcion_accesorio'],
                    foto_factura_accesorio = dataAccesorio['foto_factura_accesorio']    
                    )
                    accesorio.save()
            return Response ({'mensaje': 'Se creo el accesorio'})
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)"""
    """def post(self, request, format=None):
        try:
            # Crea un objeto AccesoriosSerializers con los datos de entrada
            serializerAccesorio = AccesoriosSerializers(data=request.data)
            if serializerAccesorio.is_valid():
                dataAccesorio = request.data
                miComputador = Computador.objects.get(id=dataAccesorio['computador'])
                if miComputador:
                    accesorio = Accesorios(
                        codigo_interno_accesorio=dataAccesorio['codigo_interno_accesorio'],
                        nombre_accesorio=dataAccesorio['nombre_accesorio'],
                        serial_accesorio=dataAccesorio['serial_accesorio'],
                        modelo_accessorio=dataAccesorio['modelo_accessorio'],
                        marca_accesorio=dataAccesorio['marca_accesorio'],
                        descripcion_accesorio=dataAccesorio['descripcion_accesorio'],
                        fecha_adquisicion_accesorio=dataAccesorio['fecha_adquisicion_accesorio'],
                        fecha_instalacion_accesorio=dataAccesorio['fecha_instalacion_accesorio'],
                        fecha_garantia_accesorio=dataAccesorio['fecha_garantia_accesorio'],
                        registro_fotografico_accesorio=dataAccesorio['registro_fotografico_accesorio'],
                        foto_requisicion_accesorio=dataAccesorio['foto_requisicion_accesorio'],
                        foto_acta_salida_accesorio=dataAccesorio['foto_acta_salida_accesorio'],
                        foto_acta_recepcion_accesorio=dataAccesorio['foto_acta_recepcion_accesorio'],
                        foto_factura_accesorio=dataAccesorio['foto_factura_accesorio']
                    )
                    accesorio.save()
                    return Response({'mensaje': 'Se creó el accesorio'})
            # Si el serializador no es válido o si el computador no existe, devolver un error
            return Response({'error': 'No se pudo crear el accesorio'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)"""
    def post(self, request, format=None):
        try:
            # Crea un objeto AccesoriosSerializers con los datos de entrada
            serializerAccesorio = AccesoriosSerializers(data=request.data)
            if serializerAccesorio.is_valid():
                dataAccesorio = request.data
                miComputador = Computador.objects.get(id=dataAccesorio['computador'])
                if miComputador:
                    accesorio = Accesorios(
                        computador = miComputador,
                        codigo_interno_accesorio=dataAccesorio['codigo_interno_accesorio'],
                        nombre_accesorio=dataAccesorio['nombre_accesorio'],
                        serial_accesorio=dataAccesorio['serial_accesorio'],
                        modelo_accessorio=dataAccesorio['modelo_accessorio'],
                        marca_accesorio=dataAccesorio['marca_accesorio'],
                        descripcion_accesorio=dataAccesorio['descripcion_accesorio'],
                        fecha_adquisicion_accesorio=dataAccesorio['fecha_adquisicion_accesorio'],
                        fecha_instalacion_accesorio=dataAccesorio['fecha_instalacion_accesorio'],
                        fecha_garantia_accesorio=dataAccesorio['fecha_garantia_accesorio'],
                        registro_fotografico_accesorio=dataAccesorio['registro_fotografico_accesorio'],
                        foto_requisicion_accesorio=dataAccesorio['foto_requisicion_accesorio'],
                        foto_acta_salida_accesorio=dataAccesorio['foto_acta_salida_accesorio'],
                        foto_acta_recepcion_accesorio=dataAccesorio['foto_acta_recepcion_accesorio'],
                        foto_factura_accesorio=dataAccesorio['foto_factura_accesorio']
                    )
                    accesorio.save()
                    return Response({'mensaje': 'Se creó el accesorio'})
            # Si el serializador no es válido o si el computador no existe, devolver un error
            return Response({'error': 'No se pudo crear el accesorio'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    # Metodo GET    
    def get(self, request, format = None):
        try: 
            accesorios = Accesorios.objects.all()
            serializer = AccesoriosSerializers(accesorios, many = True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    # Metodo PUT
    def put(self, request, pk, format = None):
        try:
            accesorio = Accesorios.objects.get(pk = pk)
            serializer = AccesoriosSerializers(accesorio, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        except Accesorios.DoesNotExist:
            return Response("Los accesorios no existen", status = status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"Error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    # Metodo DELETE
    def delete(self, request, pk, format = None):
        try:
            accesorio = Accesorios.objects.get(pk = pk)
            accesorio.delete()
            return Response({"Msg": 'Registro eliminado correctamente'}, status = status.HTTP_200_OK)
        except Ciudad.DoesNotExist:
            return Response({"Error": "Los accesorios no existen"}, status = status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response ({"Error": str(e)}, status = status.HTTP_400_BAD_REQUEST)