from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
class List(View):
    template = "todo_maker/list.html"
    def get(self, request, *args, **kwargs):
        
        context = {}

        return render(request, self.template, context)

class Create(View):
    template = "todo_marker/create.html"
    def get(self, request, *args, **kwargs):
        
        context = {}

        return render(request, self.template, context)


