from django.http import HttpResponse


def saludo(request): # primera vista

	return HttpResponse("<h1>Curso de pildoras informaticas</h1>")


def noticias(request):

	return HttpResponse("<h1>Seccion Noticias</h1>")