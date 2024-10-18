from django import forms

class CrearPesaFormulario(forms.Form):
    marca = forms.CharField(max_length=20)
    material = forms.CharField(max_length=20)
    peso = forms.IntegerField()


class BuscarPesaFormulario(forms.Form):
    marca = forms.CharField(max_length=20, required=False)
