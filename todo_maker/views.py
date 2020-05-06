from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from todo_maker.models import Task
from todo_maker.forms import TaskCreateForm
from django.contrib import messages

# Create your views here.
class List(View):
    template = "todo_maker/list.html"
    def get(self, request, *args, **kwargs):
        instance = None
        if kwargs.get('pk', None):
            try:
                instance = Task.objects.filter(pk=kwargs.get('pk', None))[0]
            except Exception:
                instance = None

        form = TaskCreateForm(instance=instance)
        context = {
            "tasks" : Task.objects.filter(),
            "form" : form,
        }

        return render(request, self.template, context)
    
    def post(self, request, *args, **kwargs):
        instance = None
        post  = request.POST.copy()
        pk = kwargs.get('pk', None)
        if pk:
            try:
                instance = Task.objects.filter(pk=pk)[0]
            except Exception:
                instance = None

        form = TaskCreateForm(post, instance=instance)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.add_message(request, messages.SUCCESS, "Reviews successfully submitted.")
        else:
            messages.add_message(request, messages.ERROR, "Please fill * marked fields")
            
        
        return redirect(reverse('list-todo'))


class Create(View):
    template = "todo_marker/create.html"
    def get(self, request, *args, **kwargs):
        
        context = {}

        return render(request, self.template, context)


