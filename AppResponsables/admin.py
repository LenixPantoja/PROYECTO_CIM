from django.contrib import admin
from AppResponsables.models import Responsable
from django.utils.safestring import mark_safe
import base64

# Register your models here.
@admin.register(Responsable)
class ResponsableAdmin(admin.ModelAdmin):
    list_display = ('nombres_completos', 'numero_documento',)
    list_filter = ('nombres_completos', 'numero_documento',)
    search_fields = ('nombres_completos', 'numero_documento',)
    list_display = ('nombres_completos', 'numero_documento')
    
    def view_firma(self, obj):
        if obj.firma_responsable:
            return mark_safe('<img src="data:image/png;base64,{}" width="100" height="100" />'.format(base64.b64encode(obj.firma_responsable).decode('utf-8')))
        else:
            return "No disponible"
    
    view_firma.short_description = 'Firma'
    
    readonly_fields = ('view_firma', )
