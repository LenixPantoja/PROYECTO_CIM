""" Librerias  """
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
from rest_framework import generics
from django.http import JsonResponse
from base64 import *
""" Modelos """
from AppComputadoras.serializers import *
from AppComputadoras.models import *
from django.core.files.uploadedfile import InMemoryUploadedFile

class AppComputers_API_CrearMouse(APIView):
    def post(self, request, format = None):

        try:

            serializer = MouseSerializers(data = request.data)

            if serializer.is_valid():
                dataMouse = request.data
                mouse = Mouse(
                    marca_mouse = dataMouse['marca_mouse'],
                    modelo_mouse = dataMouse['modelo_mouse'],
                    serial_mouse = dataMouse['serial_mouse'],
                    fecha_adquisicion_mouse =  dataMouse['fecha_adquisicion_mouse'],
                    fecha_instalacion_mouse = dataMouse['fecha_instalacion_mouse'],
                    fecha_garantia_mouse = dataMouse['fecha_garantia_mouse'],
                    registro_fotografico_mouse  = dataMouse['registro_fotografico_mouse'].read(),
                    foto_requisicion_mouse = dataMouse['foto_requisicion_mouse'].read(),
                    foto_acta_salida = dataMouse['foto_acta_salida'].read(),
                    foto_acta_recepcion = dataMouse['foto_acta_recepcion'].read(),
                    foto_factura = dataMouse['foto_factura'].read()
                )
                mouse.save()
                return Response({'mensaje': 'Se creo el mouse :)'})
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class AppComputers_API_CrearTeclado(APIView):
    def post(self, request, format = None):
        try:
            serializer = TecladoSerializers(data = request.data)

            if serializer.is_valid():
                dataTeclado = request.data
                teclado = Teclado(
                    marca_teclado = dataTeclado['marca_teclado'],
                    modelo_teclado = dataTeclado['modelo_teclado'],
                    serial_teclado = dataTeclado['serial_teclado'],
                    fecha_adquisicion_teclado = dataTeclado['fecha_adquisicion_teclado'],
                    fecha_instalacion_teclado = dataTeclado['fecha_instalacion_teclado'],
                    fecha_garantia_teclado = dataTeclado['fecha_garantia_teclado'],
                    registro_fotografico_teclado = dataTeclado['registro_fotografico_teclado'].read(),
                    foto_requisicion_teclado = dataTeclado['foto_requisicion_teclado'].read(),
                    foto_acta_salida_teclado = dataTeclado['foto_acta_salida_teclado'].read(),
                    foto_acta_recepcion_teclado = dataTeclado['foto_acta_recepcion_teclado'].read(),
                    foto_factura_teclado = dataTeclado['foto_factura_teclado'].read()
                )
                teclado.save()
            return Response({'mensaje': 'Se creo el teclado'})
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class AppComputers_API_CrearMonitor(APIView):
    def post(self, request, format = None):
        try:
            serializer = MonitorSerializers(data = request.data)

            if serializer.is_valid():
                dataMonitor = request.data
                monitor = Monitor(
                    codigo_interno_monitor = dataMonitor['codigo_interno_monitor'],
                    marca_monitor = dataMonitor['marca_monitor'],
                    modelo_monitor = dataMonitor['modelo_monitor'],
                    serial_monitor = dataMonitor['serial_monitor'],
                    descripcion_monitor = dataMonitor['descripcion_monitor'],
                    fecha_adquisicion_monitor = dataMonitor['fecha_adquisicion_monitor'],
                    fecha_instalacion_monitor = dataMonitor['fecha_instalacion_monitor'],
                    fecha_garantia_monitor = dataMonitor['fecha_garantia_monitor'],
                    registro_fotografico_monitor = dataMonitor['registro_fotografico_monitor'].read(),
                    foto_requisicion_monitor = dataMonitor['foto_requisicion_monitor'].read(),
                    foto_acta_salida_monitor = dataMonitor['foto_acta_salida_monitor'].read(),
                    foto_acta_recepcion_monitor = dataMonitor['foto_acta_recepcion_monitor'].read(),
                    foto_factura_monitor = dataMonitor['foto_factura_monitor'].read()
                )
                monitor.save()
            return Response({'mensaje': 'Se creo el monitor'})
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class AppComputers_API_CrearTorre(APIView):
    def post(self, request, format =  None):
        try:
            serializer = TorreSerializers(data = request.data)

            if serializer.is_valid():
                dataTorre = request.data
                torre = Torre(
                    codigo_interno_torre = dataTorre['codigo_interno_torre'],
                    dominio_torre = dataTorre['dominio_torre'],
                    nombre_equipo = dataTorre['nombre_equipo'],
                    marca_torre = dataTorre['marca_torre'],
                    modelo_torre = dataTorre['modelo_torre'],
                    serial_torre = dataTorre['serial_torre'],
                    direccion_ip_torre = dataTorre['direccion_ip_torre'],
                    direccion_mac_torre = dataTorre['direccion_mac_torre'],
                    descripcion_torre = dataTorre['descripcion_torre'],
                    fecha_adquisicion_torre = dataTorre['fecha_adquisicion_torre'],
                    fecha_instalacion_torre = dataTorre['fecha_instalacion_torre'],
                    fecha_garantia_torre = dataTorre['fecha_garantia_torre'],
                    registro_fotografico_torre = dataTorre['registro_fotografico_torre'].read(),
                    foto_requisicion_torre = dataTorre['foto_requisicion_torre'].read(),
                    foto_acta_salida_torre = dataTorre['foto_acta_salida_torre'].read(),
                    foto_acta_recepcion_torre = dataTorre['foto_acta_recepcion_torre'].read(),
                    foto_factura_torre = dataTorre['foto_factura_torre'].read()
                )
                torre.save()
            return Response({'mensaje': 'Se creo la torre'})
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)      
        
class AppComputers_API_CiudadSede(APIView):
    def post(self, request, format = None):
        try:
            serializerCiudad = CiudadSerializers(data = request.data)
            serializerSede = SedeSerializers(data = request.data)

            if serializerCiudad.is_valid() and serializerSede.is_valid():
                dataCiudad = request.data
                dataSede = request.data
                ciudad = Ciudad(
                    nombre_ciudad = dataCiudad['nombre_ciudad']
                )
                sede = Sede(
                    nombre_sede = dataSede['nombre_sede'],
                    ciudad = ciudad
                )
                ciudad.save()
                sede.save()
            return Response ({'mensaje': 'Se creo exitosamente'})
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
                
class AppComputers_API_CrearArea(APIView):
    def post(self, request, format =  None):
        try:
            serializer = AreaSerializers(data = request.data)

            if serializer.is_valid():
                dataArea = request.data
                area = Area(
                    nombre_area = dataArea['nombre_area'],
                    sedes = dataArea['sedes']
                )
                area.save()
            return Response ({'mensaje': 'Se creo el area'})
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class AppComputers_API_CrearWorkstation(APIView):
    def post(self, request, format = None):
        try:
            serializer = WorkstationSerializers(data = request.data)

            if serializer.is_valid():
                dataWorkstation = request.data
                workstation = Workstation(
                    puesto_trabajo = dataWorkstation['puesto_trabajo']
                )
                workstation.save()
            return Response ({'mensaje': 'Se creo el workstation'})
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class AppComputers_API_CrearComputador(APIView):
    def post(self, request, format = None):
        try:
            serializer = ComputadorSerializers(data = request.data)

            if serializer.is_valid():
                dataComputador = request.data
                computador = Computador(
                    area = dataComputador['area'],
                    workstation = dataComputador['workstation'],
                    monitor = dataComputador['monitor'],
                    teclado = dataComputador['teclado'],
                    mouse = dataComputador['mouse'],
                    torre = dataComputador['torre'],
                    responsable = dataComputador['responsable'],
                )
                computador.save()
            return Response ({'mensaje': 'Se creo el computador'})
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class AppComputers_API_CrearImpresora(APIView):
    def post(self, request, format = None):
        try:
            serializer = ImpresorasSerializers(data = request.data)

            if serializer.is_valid():
                dataImpresora = request.data
                impresora = Impresoras(
                    computador = dataImpresora['computador'],
                    codigo_interno_impresora = dataImpresora['codigo_interno_impresora'],
                    nombre_impresora = dataImpresora['nombre_impresora'],
                    modelo_impresora = dataImpresora['modelo_impresora'],
                    serial_impresora = dataImpresora['serial_impresora'],
                    descripcion_impresora = dataImpresora['descripcion_impresora'],
                    fecha_adquisicion_impresora = dataImpresora['fecha_adquisicion_impresora'],
                    fecha_instalacion_impresora = dataImpresora['fecha_instalacion_impresora'],
                    fecha_garantia_impresora = dataImpresora['fecha_garantia_impresora'],
                    registro_fotografico_impresora = dataImpresora['registro_fotografico_impresora'].read(),
                    foto_requisicion_impresora = dataImpresora['foto_requisicion_impresora'].read(),
                    foto_acta_salida_impresora = dataImpresora['foto_acta_salida_impresora'].read(),
                    foto_acta_recepcion_impresora = dataImpresora['foto_acta_recepcion_impresora'].read(),
                    foto_factura_impresora = dataImpresora['foto_factura_impresora'].read(),
                )
                impresora.save()
            return Response ({'mensaje': 'Se creo la impresora'})
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class AppComputers_API_CrearAccesorio(APIView):
    def post(self, request, format = None):
        try:
            serializer = AccesoriosSerializers(data = request.data)

            if serializer.is_valid():
                dataAccesorio = request.data
                accesorio = Accesorios(
                    computador = dataAccesorio['computador'],
                    codigo_interno_accesorio = dataAccesorio['codigo_interno_accesorio'],
                    nombre_accesorio = dataAccesorio['nombre_accesorio'],
                    serial_accesorio = dataAccesorio['serial_accesorio'],
                    modelo_accessorio = dataAccesorio['modelo_accessorio'],
                    marca_accesorio = dataAccesorio['marca_accesorio'],
                    descripcion_accesorio = dataAccesorio['descripcion_accesorio'],
                    fecha_adquisicion_accesorio = dataAccesorio['fecha_adquisicion_accesorio'],
                    fecha_instalacion_accesorio = dataAccesorio['fecha_instalacion_accesorio'],
                    fecha_garantia_accesorio = dataAccesorio['fecha_garantia_accesorio'],
                    registro_fotografico_accesorio = dataAccesorio['registro_fotografico_accesorio'].read(),
                    foto_requisicion_accesorio = dataAccesorio['foto_requisicion_accesorio'].read(),
                    foto_acta_salida_accesorio = dataAccesorio['foto_acta_salida_accesorio'].read(),
                    foto_acta_recepcion_accesorio = dataAccesorio['foto_acta_recepcion_accesorio'].read(),
                    foto_factura_accesorio = dataAccesorio['foto_factura_accesorio'].read(),
                )
                accesorio.save()
            return Response ({'mensaje': 'Se creo el accesorio'})
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        

                

    
