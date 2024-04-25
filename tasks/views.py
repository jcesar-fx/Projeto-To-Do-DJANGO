from django.shortcuts import render, get_object_or_404, redirect # type: ignore
from django.http import HttpResponse # type: ignore
from .forms import taskForm

from .models import Task

# Create your views here.
def tasklist(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'tasks/list.html', {'tasks': tasks})
def taskView(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'tasks/task.html', {'task' : task })
def newtask(request):
    if request.method == 'POST':
        form = taskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'doing'
            task.save()
            return redirect('/')
    else:
        form = taskForm()
        return render(request, 'tasks/addtask.html', {'form' : form})
def helloWorld(request):
    return HttpResponse('hello world!')
def edittask(request, id):
    task = get_object_or_404(Task, pk=id)
    form = taskForm(instance=)
def yourname(request, name):
    return render(request, 'tasks/yourname.html', {'name': name})