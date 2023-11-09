""" Librerias  """
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
from rest_framework import generics
from django.http import JsonResponse
""" Modelos """
from AppComputadoras.serializers import *
from AppComputadoras.models import *
""" Otras Librerias """
from django.core.files.storage import default_storage
from pathlib import *


class AppComputers_API_CrearMouse(APIView):
    def post(self, request, format = None):

        try:

            serializer = MouseSerializers(data = request.data)

            if serializer.is_valid():
                dataMouse = request.data
                files_path = 'mouses/' + dataMouse['serial_mouse'] + '/'
                default_storage.save(files_path + f'{dataMouse['serial_mouse']}_registro_fotografico_mouse.png', dataMouse['registro_fotografico_mouse'])
                default_storage.save(files_path + f'{dataMouse['serial_mouse']}_foto_requisicion_mouse.png', dataMouse['foto_requisicion_mouse'])
                default_storage.save(files_path + f'{dataMouse['serial_mouse']}_foto_acta_salida.png', dataMouse['foto_acta_salida'])
                default_storage.save(files_path + f'{dataMouse['serial_mouse']}_foto_acta_recepcion.png', dataMouse['foto_acta_recepcion'])
                default_storage.save(files_path + f'{dataMouse['serial_mouse']}_foto_factura.png', dataMouse['foto_factura'])
                mouse = Mouse(
                    marca_mouse = dataMouse['marca_mouse'],
                    modelo_mouse = dataMouse['modelo_mouse'],
                    serial_mouse = dataMouse['serial_mouse'],
                    fecha_adquisicion_mouse =  dataMouse['fecha_adquisicion_mouse'],
                    fecha_instalacion_mouse = dataMouse['fecha_instalacion_mouse'],
                    fecha_garantia_mouse = dataMouse['fecha_garantia_mouse'],
                    registro_fotografico_mouse  = files_path + 'registro_fotografico_mouse.png',
                    foto_requisicion_mouse = files_path + 'foto_requisicion_mouse.png',
                    foto_acta_salida = files_path + 'foto_acta_salida.png',
                    foto_acta_recepcion = files_path + 'foto_acta_recepcion.png',
                    foto_factura = files_path + 'foto_factura.png'
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
                files_path = 'teclados/' + dataTeclado['serial_teclado'] + '/'
                default_storage.save(files_path + f'{dataTeclado['serial_teclado']}_registro_fotografico_teclado.png', dataTeclado['registro_fotografico_teclado'])
                default_storage.save(files_path + f'{dataTeclado['serial_teclado']}_foto_requisicion_teclado.png', dataTeclado['foto_requisicion_teclado'])
                default_storage.save(files_path + f'{dataTeclado['serial_teclado']}_foto_acta_salida_teclado.png', dataTeclado['foto_acta_salida_teclado'])
                default_storage.save(files_path + f'{dataTeclado['serial_teclado']}_foto_acta_recepcion_teclado.png', dataTeclado['foto_acta_recepcion_teclado'])
                default_storage.save(files_path + f'{dataTeclado['serial_teclado']}_foto_factura_teclado.png', dataTeclado['foto_factura_teclado'])
                teclado = Teclado(
                    marca_teclado = dataTeclado['marca_teclado'],
                    modelo_teclado = dataTeclado['modelo_teclado'],
                    serial_teclado = dataTeclado['serial_teclado'],
                    fecha_adquisicion_teclado = dataTeclado['fecha_adquisicion_teclado'],
                    fecha_instalacion_teclado = dataTeclado['fecha_instalacion_teclado'],
                    fecha_garantia_teclado = dataTeclado['fecha_garantia_teclado'],
                    registro_fotografico_teclado = files_path + 'registro_fotografico_teclado.png',
                    foto_requisicion_teclado = files_path + 'foto_requisicion_teclado.png',
                    foto_acta_salida_teclado = files_path + 'foto_acta_salida_teclado.png',
                    foto_acta_recepcion_teclado = files_path + 'foto_acta_recepcion_teclado.png',
                    foto_factura_teclado = files_path + 'foto_factura_teclado.png'
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
                files_path = 'monitores/' + dataMonitor['serial_monitor'] + '/'
                default_storage.save(files_path + f'{dataMonitor['serial_monitor']}_registro_fotografico_monitor.png', dataMonitor['registro_fotografico_monitor'])
                default_storage.save(files_path + f'{dataMonitor['serial_monitor']}_foto_requisicion_monitor.png', dataMonitor['foto_requisicion_monitor'])
                default_storage.save(files_path + f'{dataMonitor['serial_monitor']}_foto_acta_salida_monitor.png', dataMonitor['foto_acta_salida_monitor'])
                default_storage.save(files_path + f'{dataMonitor['serial_monitor']}_foto_acta_recepcion_monitor.png', dataMonitor['foto_acta_recepcion_monitor'])
                default_storage.save(files_path + f'{dataMonitor['serial_monitor']}_foto_factura_monitor.png', dataMonitor['foto_factura_monitor'])
                monitor = Monitor(
                    codigo_interno_monitor = dataMonitor['codigo_interno_monitor'],
                    marca_monitor = dataMonitor['marca_monitor'],
                    modelo_monitor = dataMonitor['modelo_monitor'],
                    serial_monitor = dataMonitor['serial_monitor'],
                    descripcion_monitor = dataMonitor['descripcion_monitor'],
                    fecha_adquisicion_monitor = dataMonitor['fecha_adquisicion_monitor'],
                    fecha_instalacion_monitor = dataMonitor['fecha_instalacion_monitor'],
                    fecha_garantia_monitor = dataMonitor['fecha_garantia_monitor'],
                    registro_fotografico_monitor = files_path + 'registro_fotografico_monitor.png',
                    foto_requisicion_monitor = files_path + 'foto_requisicion_monitor.png',
                    foto_acta_salida_monitor = files_path + 'foto_acta_salida_monitor.png',
                    foto_acta_recepcion_monitor = files_path + 'foto_acta_recepcion_monitor.png',
                    foto_factura_monitor = files_path + 'foto_factura_monitor.png'
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
                files_path = 'monitores/' + dataTorre['serial_torre'] + '/'
                default_storage.save(files_path + f'{dataTorre['serial_torre']}_registro_fotografico_torre.png', dataTorre['registro_fotografico_torre'])
                default_storage.save(files_path + f'{dataTorre['serial_torre']}_foto_requisicion_torre.png', dataTorre['foto_requisicion_torre'])
                default_storage.save(files_path + f'{dataTorre['serial_torre']}_foto_acta_salida_torre.png', dataTorre['foto_acta_salida_torre'])
                default_storage.save(files_path + f'{dataTorre['serial_torre']}_foto_acta_recepcion_torre.png', dataTorre['foto_acta_recepcion_torre'])
                default_storage.save(files_path + f'{dataTorre['serial_torre']}_foto_factura_torre.png', dataTorre['foto_factura_torre'])
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
                    registro_fotografico_torre = files_path + 'registro_fotografico_torre.png',
                    foto_requisicion_torre = files_path + 'foto_requisicion_torre.png',
                    foto_acta_salida_torre = files_path + 'foto_acta_salida_torre.png',
                    foto_acta_recepcion_torre = files_path + 'foto_acta_recepcion_torre.png',
                    foto_factura_torre = files_path + 'foto_factura_torre.png'
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
                dataMonitor = request.data
                files_path = 'monitores/' + dataMonitor['serial_monitor'] + '/'
                default_storage.save(files_path + f'{dataMonitor['serial_monitor']}_registro_fotografico_monitor.png', dataMonitor['registro_fotografico_monitor'])
                default_storage.save(files_path + f'{dataMonitor['serial_monitor']}_foto_requisicion_monitor.png', dataMonitor['foto_requisicion_monitor'])
                default_storage.save(files_path + f'{dataMonitor['serial_monitor']}_foto_acta_salida_monitor.png', dataMonitor['foto_acta_salida_monitor'])
                default_storage.save(files_path + f'{dataMonitor['serial_monitor']}_foto_acta_recepcion_monitor.png', dataMonitor['foto_acta_recepcion_monitor'])
                default_storage.save(files_path + f'{dataMonitor['serial_monitor']}_foto_factura_monitor.png', dataMonitor['foto_factura_monitor'])
                monitor = Monitor(
                    codigo_interno_monitor = dataMonitor['codigo_interno_monitor'],
                    marca_monitor = dataMonitor['marca_monitor'],
                    modelo_monitor = dataMonitor['modelo_monitor'],
                    serial_monitor = dataMonitor['serial_monitor'],
                    descripcion_monitor = dataMonitor['descripcion_monitor'],
                    fecha_adquisicion_monitor = dataMonitor['fecha_adquisicion_monitor'],
                    fecha_instalacion_monitor = dataMonitor['fecha_instalacion_monitor'],
                    fecha_garantia_monitor = dataMonitor['fecha_garantia_monitor'],
                    registro_fotografico_monitor = files_path + 'registro_fotografico_monitor.png',
                    foto_requisicion_monitor = files_path + 'foto_requisicion_monitor.png',
                    foto_acta_salida_monitor = files_path + 'foto_acta_salida_monitor.png',
                    foto_acta_recepcion_monitor = files_path + 'foto_acta_recepcion_monitor.png',
                    foto_factura_monitor = files_path + 'foto_factura_monitor.png'
                )
                monitor.save()
                dataTeclado = request.data
                files_path = 'teclados/' + dataTeclado['serial_teclado'] + '/'
                default_storage.save(files_path + f'{dataTeclado['serial_teclado']}_registro_fotografico_teclado.png', dataTeclado['registro_fotografico_teclado'])
                default_storage.save(files_path + f'{dataTeclado['serial_teclado']}_foto_requisicion_teclado.png', dataTeclado['foto_requisicion_teclado'])
                default_storage.save(files_path + f'{dataTeclado['serial_teclado']}_foto_acta_salida_teclado.png', dataTeclado['foto_acta_salida_teclado'])
                default_storage.save(files_path + f'{dataTeclado['serial_teclado']}_foto_acta_recepcion_teclado.png', dataTeclado['foto_acta_recepcion_teclado'])
                default_storage.save(files_path + f'{dataTeclado['serial_teclado']}_foto_factura_teclado.png', dataTeclado['foto_factura_teclado'])
                teclado = Teclado(
                    marca_teclado = dataTeclado['marca_teclado'],
                    modelo_teclado = dataTeclado['modelo_teclado'],
                    serial_teclado = dataTeclado['serial_teclado'],
                    fecha_adquisicion_teclado = dataTeclado['fecha_adquisicion_teclado'],
                    fecha_instalacion_teclado = dataTeclado['fecha_instalacion_teclado'],
                    fecha_garantia_teclado = dataTeclado['fecha_garantia_teclado'],
                    registro_fotografico_teclado = files_path + 'registro_fotografico_teclado.png',
                    foto_requisicion_teclado = files_path + 'foto_requisicion_teclado.png',
                    foto_acta_salida_teclado = files_path + 'foto_acta_salida_teclado.png',
                    foto_acta_recepcion_teclado = files_path + 'foto_acta_recepcion_teclado.png',
                    foto_factura_teclado = files_path + 'foto_factura_teclado.png'
                )
                teclado.save()
                dataMouse = request.data
                files_path = 'mouses/' + dataMouse['serial_mouse'] + '/'
                default_storage.save(files_path + f'{dataMouse['serial_mouse']}_registro_fotografico_mouse.png', dataMouse['registro_fotografico_mouse'])
                default_storage.save(files_path + f'{dataMouse['serial_mouse']}_foto_requisicion_mouse.png', dataMouse['foto_requisicion_mouse'])
                default_storage.save(files_path + f'{dataMouse['serial_mouse']}_foto_acta_salida.png', dataMouse['foto_acta_salida'])
                default_storage.save(files_path + f'{dataMouse['serial_mouse']}_foto_acta_recepcion.png', dataMouse['foto_acta_recepcion'])
                default_storage.save(files_path + f'{dataMouse['serial_mouse']}_foto_factura.png', dataMouse['foto_factura'])
                mouse = Mouse(
                    marca_mouse = dataMouse['marca_mouse'],
                    modelo_mouse = dataMouse['modelo_mouse'],
                    serial_mouse = dataMouse['serial_mouse'],
                    fecha_adquisicion_mouse =  dataMouse['fecha_adquisicion_mouse'],
                    fecha_instalacion_mouse = dataMouse['fecha_instalacion_mouse'],
                    fecha_garantia_mouse = dataMouse['fecha_garantia_mouse'],
                    registro_fotografico_mouse  = files_path + 'registro_fotografico_mouse.png',
                    foto_requisicion_mouse = files_path + 'foto_requisicion_mouse.png',
                    foto_acta_salida = files_path + 'foto_acta_salida.png',
                    foto_acta_recepcion = files_path + 'foto_acta_recepcion.png',
                    foto_factura = files_path + 'foto_factura.png'
                )
                mouse.save()
                dataTorre = request.data
                files_path = 'monitores/' + dataTorre['serial_torre'] + '/'
                default_storage.save(files_path + f'{dataTorre['serial_torre']}_registro_fotografico_torre.png', dataTorre['registro_fotografico_torre'])
                default_storage.save(files_path + f'{dataTorre['serial_torre']}_foto_requisicion_torre.png', dataTorre['foto_requisicion_torre'])
                default_storage.save(files_path + f'{dataTorre['serial_torre']}_foto_acta_salida_torre.png', dataTorre['foto_acta_salida_torre'])
                default_storage.save(files_path + f'{dataTorre['serial_torre']}_foto_acta_recepcion_torre.png', dataTorre['foto_acta_recepcion_torre'])
                default_storage.save(files_path + f'{dataTorre['serial_torre']}_foto_factura_torre.png', dataTorre['foto_factura_torre'])
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
                    registro_fotografico_torre = files_path + 'registro_fotografico_torre.png',
                    foto_requisicion_torre = files_path + 'foto_requisicion_torre.png',
                    foto_acta_salida_torre = files_path + 'foto_acta_salida_torre.png',
                    foto_acta_recepcion_torre = files_path + 'foto_acta_recepcion_torre.png',
                    foto_factura_torre = files_path + 'foto_factura_torre.png'
                )
                torre.save()
                computador = Computador(
                    area = dataComputador['area'],
                    workstation = dataComputador['workstation'],
                    monitor = monitor,
                    teclado = teclado,
                    mouse = mouse,
                    torre = torre,
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
                files_path = 'impresoras/' + dataImpresora['serial_impresora'] + '/'
                default_storage.save(files_path + f'{dataImpresora['serial_impresora']}_registro_fotografico_impresora.png', dataImpresora['registro_fotografico_impresora'])
                default_storage.save(files_path + f'{dataImpresora['serial_impresora']}_foto_requisicion_impresora.png', dataImpresora['foto_requisicion_impresora'])
                default_storage.save(files_path + f'{dataImpresora['serial_impresora']}_foto_acta_salida_impresora.png', dataImpresora['foto_acta_salida_impresora'])
                default_storage.save(files_path + f'{dataImpresora['serial_impresora']}_foto_acta_recepcion_impresora.png', dataImpresora['foto_acta_recepcion_impresora'])
                default_storage.save(files_path + f'{dataImpresora['serial_impresora']}_foto_factura_impresora.png', dataImpresora['foto_factura_impresora'])
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
                    registro_fotografico_impresora = files_path + 'registro_fotografico_impresora.png',
                    foto_requisicion_impresora = files_path + 'foto_requisicion_impresora.png',
                    foto_acta_salida_impresora = files_path + 'foto_acta_salida_impresora.png',
                    foto_acta_recepcion_impresora = files_path + 'foto_acta_recepcion_impresora.png',
                    foto_factura_impresora = files_path + 'foto_factura_impresora.png',
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
                files_path = 'accesorios/' + dataAccesorio['serial_accesorio'] + '/'
                default_storage.save(files_path + f'{dataAccesorio['serial_accesorio']}_registro_fotografico_accesorio.png', dataAccesorio['registro_fotografico_accesorio'])
                default_storage.save(files_path + f'{dataAccesorio['serial_accesorio']}_foto_requisicion_accesorio.png', dataAccesorio['foto_requisicion_accesorio'])
                default_storage.save(files_path + f'{dataAccesorio['serial_accesorio']}_foto_acta_salida_accesorio.png', dataAccesorio['foto_acta_salida_accesorio'])
                default_storage.save(files_path + f'{dataAccesorio['serial_accesorio']}_foto_acta_recepcion_accesorio.png', dataAccesorio['foto_acta_recepcion_accesorio'])
                default_storage.save(files_path + f'{dataAccesorio['serial_accesorio']}_foto_factura_accesorio.png', dataAccesorio['foto_factura_accesorio'])
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
                    registro_fotografico_accesorio = files_path + 'registro_fotografico_accesorio.png',
                    foto_requisicion_accesorio = files_path + 'foto_requisicion_accesorio.png',
                    foto_acta_salida_accesorio = files_path + 'foto_acta_salida_accesorio.png',
                    foto_acta_recepcion_accesorio = files_path + 'foto_acta_recepcion_accesorio.png',
                    foto_factura_accesorio = files_path + 'foto_factura_accesorio.png',
                )
                accesorio.save()
            return Response ({'mensaje': 'Se creo el accesorio'})
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        

                

    
