from django.views.generic import ListView, CreateView
from .models import Task


class TaskListView(ListView):
    template_name = 'tasks/list.html'
    model = Task


class TaskCreateView(CreateView):
    template_name = 'tasks/create.html'
    model = Task
    fields = '__all__'
    success_url = '/tasks/'
