from django.http import HttpResponse

def inicio(request):
    return HttpResponse('Bienvenidos a mi INICIO!!')