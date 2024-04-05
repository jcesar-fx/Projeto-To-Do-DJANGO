from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def helloWorld(request):
    return HttpResponse('hello world!')
def tasklist(request):
    return render(request, 'tasks/list.html')
def yourname(request, name):
    return render(request, 'tasks/yourname.html', {'name': name})