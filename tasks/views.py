from django.shortcuts import render, get_object_or_404, redirect # type: ignore
from django.http import HttpResponse # type: ignore

from .forms import taskForm
from django.contrib.auth.decorators import login_required # type: ignore
from .models import Task
from django.core.paginator import Paginator # type: ignore
from django.contrib import messages #type: ignore
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model # type: ignore
import datetime
from django.utils.decorators import method_decorator
from rest_framework import generics
from .serializers import Taskserializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
@method_decorator(login_required, name='dispatch')
class TaskListCreate(generics.ListCreateAPIView):
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    def get_queryset(self):
     return Task.objects.filter(user=self.request.user)
    queryset = get_queryset
    serializer_class = Taskserializer
@method_decorator(login_required, name='dispatch')
class TaskListRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
     return Task.objects.filter(user=self.request.user)
    queryset = Task.objects.all()
    serializer_class = Taskserializer
    lookup_field = 'pk'

@login_required
def tasklist(request):
    search = request.GET.get('search')
    filter = request.GET.get('filter')
    taskDoneRecently = Task.objects.filter(done='done', updated_at__gt=datetime.datetime.now()-datetime.timedelta(days=30),user=request.user).count()
    tasksDone =Task.objects.filter(done='done',user=request.user).count()
    tasksDoing = Task.objects.filter(done='doing',user=request.user).count()
    if search:
        tasks = Task.objects.filter(tittle__icontains = search, user=request.user)
    elif filter:
        tasks = Task.objects.filter(done = filter, user=request.user)
    else:
        tasks_list = Task.objects.all().order_by('-created_at').filter(user=request.user )
        paginator = Paginator(tasks_list, 5)
        page = request.GET.get('page')
        tasks = paginator.get_page(page)
    return render(request, 'tasks/list.html', {'tasks': tasks,'taskrecently' : taskDoneRecently, 'tasksdone' : tasksDone, 'tasksdoing' : tasksDoing})
@login_required
def taskView(request, id):
    task = get_object_or_404(Task, pk=id, user=request.user)
    return render(request, 'tasks/task.html', {'task' : task })
@login_required
def newtask(request):
    if request.method == 'POST':
        form = taskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'doing'
            task.user = request.user
            task.save()
            return redirect('/')
    else:
        form = taskForm()
        return render(request, 'tasks/addtask.html', {'form' : form})

@login_required
def edittask(request, id):
    task = get_object_or_404(Task, pk=id, user=request.user)
    form = taskForm(instance=task)
    if(request.method == 'POST'):
        form = taskForm(request.POST, instance=task)
        if (form.is_valid()):
            task.save()
            return redirect('/')

        return render(request, 'tasks/edittask.html', {'form':form, 'task': task})  
    else:
        return render(request, 'tasks/edittask.html', {'form':form, 'task': task})
@login_required
def deletetask(request, id):
    task = get_object_or_404(Task, pk=id, user=request.user)
    task.delete()
    messages.info (request, 'Tarefa deletada com sucesso.')
    return redirect('/')
@login_required
def changestatus(request, id):
    task = get_object_or_404(Task, pk=id, user=request.user)
    if (task.done == 'doing'):
        task.done = 'done'
    else: 
        task.done = 'doing'
    task.save()
    return redirect('/')
def yourname(request, name):
    return render(request, 'tasks/yourname.html', {'name': name})
def helloWorld(request):
    return HttpResponse('hello world!')