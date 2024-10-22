from django import forms

class PesaFormularioBase(forms.Form):
    marca = forms.CharField(max_length=20)
    material = forms.CharField(max_length=20)
    peso = forms.IntegerField()

class CrearPesaFormulario(PesaFormularioBase):...
   
class EditarPesaFormulario(PesaFormularioBase):...
    

class BuscarPesaFormulario(forms.Form):
    marca = forms.CharField(max_length=20, required=False)
