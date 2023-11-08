from django.db import models
from AppResponsables.models import Responsable
# Create your models here.

class Mouse(models.Model):
    marca_mouse = models.CharField(max_length=100)
    modelo_mouse = models.CharField(max_length=100)
    serial_mouse = models.CharField(max_length=100)
    fecha_adquisicion_mouse = models.DateField()
    fecha_instalacion_mouse = models.DateField()
    fecha_garantia_mouse = models.DateField()
    registro_fotografico_mouse = models.BinaryField(blank=True, null=True)
    foto_requisicion_mouse = models.BinaryField(blank=True, null=True)
    foto_acta_salida = models.BinaryField(blank=True, null=True)
    foto_acta_recepcion = models.BinaryField(blank=True, null=True)
    foto_factura = models.BinaryField(blank=True, null=True)
    fecha_creacion_mouse = models.DateTimeField(auto_now=True)
    fecha_modificacion_mouse = models.DateTimeField(auto_now=True) 


    class Meta:
        verbose_name = 'Mouse'
        verbose_name_plural = 'Mouses'

    def __str__(self):
          return str(self.serial_mouse)
          

class Teclado(models.Model):
    marca_teclado = models.CharField(max_length=100)
    modelo_teclado = models.CharField(max_length=100)
    serial_teclado = models.CharField(max_length=100)
    fecha_adquisicion_teclado = models.DateField()
    fecha_instalacion_teclado = models.DateField()
    fecha_garantia_teclado = models.DateField()
    registro_fotografico_teclado = models.BinaryField(blank=True, null=True)
    foto_requisicion_teclado = models.BinaryField(blank=True, null=True)
    foto_acta_salida_teclado = models.BinaryField(blank=True, null=True)
    foto_acta_recepcion_teclado = models.BinaryField(blank=True, null=True)
    foto_factura_teclado = models.BinaryField(blank=True, null=True)
    fecha_creacion_teclado = models.DateTimeField(auto_now=True)
    fecha_modificacion_teclado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Teclado'
        verbose_name_plural = 'Teclados'

    def __str__(self):
          return str(self.serial_teclado)
    
class Monitor(models.Model):
    codigo_interno_monitor = models.CharField(max_length=50)
    marca_monitor = models.CharField(max_length=100)
    modelo_monitor = models.CharField(max_length=100)
    serial_monitor = models.CharField(max_length=100)
    descripcion_monitor = models.TextField()
    fecha_adquisicion_monitor = models.DateField()
    fecha_instalacion_monitor = models.DateField()
    fecha_garantia_monitor = models.DateField()
    registro_fotografico_monitor = models.BinaryField(blank=True, null=True)
    foto_requisicion_monitor = models.BinaryField(blank=True, null=True)
    foto_acta_salida_monitor = models.BinaryField(blank=True, null=True)
    foto_acta_recepcion_monitor = models.BinaryField(blank=True, null=True)
    foto_factura_monitor = models.BinaryField(blank=True, null=True)
    fecha_creacion_monitor = models.DateTimeField(auto_now=True)
    fecha_modificacion_monitor = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Monitor'
        verbose_name_plural = 'Monitores'

    def __str__(self):
          return str(self.serial_monitor)

class Torre(models.Model):
    codigo_interno_torre = models.CharField(max_length=50)
    dominio_torre = models.CharField(max_length=200)
    nombre_equipo = models.CharField(max_length=250)
    marca_torre = models.CharField(max_length=50)
    modelo_torre = models.CharField(max_length=50)
    serial_torre = models.CharField(max_length=250)
    direccion_ip_torre = models.CharField(max_length=15)
    direccion_mac_torre = models.CharField(max_length=30)
    descripcion_torre = models.TextField()
    fecha_adquisicion_torre = models.DateField()
    fecha_instalacion_torre = models.DateField()
    fecha_garantia_torre = models.DateField()
    registro_fotografico_torre = models.BinaryField(blank=True, null=True)
    foto_requisicion_torre = models.BinaryField(blank=True, null=True)
    foto_acta_salida_torre = models.BinaryField(blank=True, null=True)
    foto_acta_recepcion_torre = models.BinaryField(blank=True, null=True)
    foto_factura_torre = models.BinaryField(blank=True, null=True)
    fecha_creacion_torre = models.DateTimeField(auto_now=True)
    fecha_modificacion_torre = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Mouse'
        verbose_name_plural = 'Torres'

    def __str__(self):
          return str(self.serial_torre)
   
class Ciudad(models.Model):
    nombre_ciudad = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'

    def __str__(self):
          return str(self.nombre_ciudad)

class Sede(models.Model):
    nombre_sede = models.CharField(max_length=100)
    ciudad = models.ManyToManyField(Ciudad, verbose_name="Ciudades")
    class Meta:
        verbose_name = 'Sede'
        verbose_name_plural = 'Sedes'

    def __str__(self):
          return str(self.nombre_sede)

class Area(models.Model):
    nombre_area = models.CharField(max_length=200)
    sedes = models.ManyToManyField(Sede, related_name='areas')
    fecha_creacion_area = models.DateTimeField(auto_now=True)
    fecha_modificacion_area = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Area'
        verbose_name_plural = 'Areas'

    def __str__(self):
          return str(self.nombre_area)

class Workstation(models.Model):
    puesto_trabajo = models.CharField(max_length=200)
    fecha_creacion_workstation = models.DateTimeField(auto_now=True)
    fecha_modificacion_workstation = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Puesto de Trabajo'
        verbose_name_plural = 'Puestos de Trabajo'

    def __str__(self):
          return str(self.puesto_trabajo)
    
class Computador(models.Model):
    area = models.ForeignKey(Area, verbose_name="Area", on_delete=models.CASCADE)
    workstation = models.ForeignKey(Workstation, verbose_name= "Workstation", on_delete=models.CASCADE)
    monitor = models.OneToOneField(Monitor, verbose_name= "Monitor",on_delete=models.CASCADE)
    teclado = models.OneToOneField(Teclado, verbose_name= "Teclado",on_delete=models.CASCADE)
    mouse = models.OneToOneField(Mouse, verbose_name="Mouse",  on_delete=models.CASCADE)
    torre = models.OneToOneField(Torre, verbose_name="Torre", on_delete=models.CASCADE)
    responsable = models.ManyToManyField(Responsable, verbose_name="Responsable")

    class Meta:
        verbose_name = 'Computador'
        verbose_name_plural = 'Computadores'

    def __str__(self):
          return str(self.torre
                     )
    
class Impresoras(models.Model):
    computador = models.ForeignKey(Computador, verbose_name="Computador", on_delete=models.CASCADE)
    codigo_interno_impresora = models.CharField(max_length=50)
    nombre_impresora = models.CharField(max_length=100)
    modelo_impresora = models.CharField(max_length=250)
    serial_impresora = models.CharField(max_length=200)
    descripcion_impresora = models.TextField()
    fecha_adquisicion_impresora = models.DateField()
    fecha_instalacion_impresora = models.DateField()
    fecha_garantia_impresora = models.DateField()
    registro_fotografico_impresora = models.BinaryField(blank=True, null=True)
    foto_requisicion_impresora = models.BinaryField(blank=True, null=True)
    foto_acta_salida_impresora = models.BinaryField(blank=True, null=True)
    foto_acta_recepcion_impresora = models.BinaryField(blank=True, null=True)
    foto_factura_impresora = models.BinaryField(blank=True, null=True)
    fecha_creacion_impresora = models.DateTimeField(auto_now=True)
    fecha_modificacion_impresora = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Impresora'
        verbose_name_plural = 'Impresoras'

    def __str__(self):
          return str(self.serial_impresora)

class Accesorios(models.Model):
    computador = models.ForeignKey(Computador, verbose_name="Computador", on_delete=models.CASCADE)
    codigo_interno_accesorio = models.CharField(max_length=50)
    nombre_accesorio = models.CharField(max_length=100)
    serial_accesorio = models.CharField(max_length=100)
    modelo_accessorio = models.CharField(max_length=50)
    marca_accesorio = models.CharField(max_length=50)
    descripcion_accesorio = models.TextField()
    fecha_adquisicion_accesorio = models.DateField()
    fecha_instalacion_accesorio = models.DateField()
    fecha_garantia_accesorio = models.DateField()
    registro_fotografico_accesorio = models.BinaryField(blank=True, null=True)
    foto_requisicion_accesorio = models.BinaryField(blank=True, null=True)
    foto_acta_salida_accesorio = models.BinaryField(blank=True, null=True)
    foto_acta_recepcion_accesorio = models.BinaryField(blank=True, null=True)
    foto_factura_accesorio = models.BinaryField(blank=True, null=True)
    fecha_creacion_accesorio = models.DateTimeField(auto_now=True)
    fecha_modificacion_accesorio = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Accesorio'
        verbose_name_plural = 'Accesorios'

    def __str__(self):
          return str(self.serial_accesorio)









