from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from datetime import datetime

from .models import *
from .forms import *

# Create your views here.

def index(request):
	f_tasks = Task.objects.filter(complete=False).order_by('due')
	c_tasks = Task.objects.filter(complete=True).order_by('created')

	if request.method =='POST':
		for x in request.POST:
			if x.startswith('task_'):
				d = int(x.replace('task_', ''))
				d = Task.objects.get(pk=d)
				d.complete = not d.complete
				d.save()
				break
		return redirect('/')


	context = {'tasks': f_tasks, 'completed': c_tasks,'time': datetime.now().timestamp()}
	return render(request, 'tasks/list.html', context)

def updateTask(request, pk):
	task = Task.objects.get(id=pk)

	form = TaskForm(instance=task)

	if request.method == 'POST':
		form = TaskForm(request.POST, instance=task)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}

	return render(request, 'tasks/update_task.html', context)

def deleteTask(request, pk):
	item = Task.objects.get_object_or_404(id=pk)

	if request.method == 'POST':
		item.delete()

	return redirect('/')

def addTask( request ):
	form = TaskForm()

	if request.method == 'POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form': form}
	return render(request, 'tasks/add_task.html', context);



