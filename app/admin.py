from django.contrib import admin
from .models import *
# Register your models here.

#producto
class ProductosAdmin(admin.ModelAdmin):
    list_display = ['codigo','nombre','marca','precio','descripcion','stock','get_categorias','imagen','create_at','update_at']
    search_fields = ['codigo']
    list_per_pages = 5


#usuario
class UsuariosAdmin(admin.ModelAdmin):
    list_display = ['id_usuario','nombre_usuario','pass_usuario','tipo_usuario','fecha_nac_usuario','telefono_usuario', 'correo_usuario','direccion_usuario']
    search_fields = ['ID']
    list_per_page = 5

#producto
admin.site.register(CategoriaProducto)
admin.site.register(Producto, ProductosAdmin)
#usuario
admin.site.register(TipoUsuario)
admin.site.register(Usuario, UsuariosAdmin)