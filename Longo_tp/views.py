from django.http import HttpResponse

def mi_vista(request):
    return HttpResponse("hola soy la vista")