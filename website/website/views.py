from django.http import HttpResponse, Http404

def index(request):
    return HttpResponse("<h1>This is the first page, guys</h1>")

