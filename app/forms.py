from django import forms
from django.forms import ModelForm
from .models import *

#form producto
class ProductoForm(ModelForm):
    nombre = forms.CharField(min_length=10,max_length=20)
    precio = forms.IntegerField(min_value=400)
    class Meta:
        model = Producto
        fields = ['codigo','nombre','marca','precio','descripcion','stock','categoria','imagen']

    # widgets = {
    #       'fecha_ing' : forms.SelectDateWidget(years=range(2020,2023))
    #    }


#  FORM USUARIO
class  UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        pass_usuario = forms.CharField(widget=forms.PasswordInput)
        fields = ['id_usuario','nombre_usuario','pass_usuario','tipo_usuario','fecha_nac_usuario','telefono_usuario', 'correo_usuario','direccion_usuario']
        widgets = {
            'password': forms.PasswordInput(),
        }   
        widgets = {
            'fecha_nac_usuario' : forms.SelectDateWidget(years=range(1900,2022))
        }