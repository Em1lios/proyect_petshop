from django.db import models
from tkinter import Widget
from django import forms

# modelos productos
class CategoriaProducto(models.Model):
    categoria = models.CharField(max_length=30)

    def __str__(self):
        return self.categoria
    
    class Meta:
        db_table = 'db_categoria_producto'

class Producto(models.Model):
    codigo = models.AutoField(null=False,primary_key=True)
    nombre = models.CharField(max_length=50)
    marca =  models.CharField(max_length=50)
    stock = models.IntegerField()
    precio = models.IntegerField()
    descripcion = models.CharField(max_length=200)
    stock = models.IntegerField()
    categoria = models.ManyToManyField(CategoriaProducto, related_name='categorias')
    imagen = models.ImageField(upload_to="productos", null=True) 
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.nombre
    
    def get_categorias(self):
        return "\n".join([c.categoria for c in self.categoria.all()])
    
    class Meta:
        db_table = 'db_producto'



#usuario

class TipoUsuario(models.Model):
    tipo_usuario = models.CharField(max_length=20)

    def __str__(self):
        return self.tipo_usuario

    class Meta:
        db_table = "db_tipo_usuario"

class Usuario(models.Model):
    id_usuario = models.IntegerField(null=False, primary_key=True)
    nombre_usuario = models.CharField(max_length=20)
    pass_usuario = models.CharField(max_length=20)
    tipo_usuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE)
    fecha_nac_usuario = models.DateField(editable=True)
    telefono_usuario = models.IntegerField(editable=True)
    correo_usuario = models.EmailField(max_length=30)
    direccion_usuario = models.CharField(max_length=40)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

#class items_carrito(models.Model):
   # nombre_producto = models.CharField(max max_length=40)
    #precio_producto = models.IntegerField()
    #imagen = models.ImageField(ulpoad_to="items_carrito",null=true)
    
    ##def __str__(self):
      #  return self.nombre_producto
    
    #class Meta

#<form action="" method="POST">
    #{% csrf_token  %}
    #<input type="hidden" name="nombre_producto" id="nombre_producto" value="{{ aux.nombre }}">
    #<input type="hidden" name="precio_producto" id="precio_producto" value="{{ aux.precio }}">
    #<input type="hidden" name="imagen_producto" id="imagen_producto" value="{{ aux.imagen }}">
    #<input type="submit" value="Carrito" style="cursor: pointer" class="btn btn-success btn-sm ml-auto">
#</form>

#python manage.py makemigrations
#python manage.py migrate
#python manage.py createsuperuser
#python manage.py runserver