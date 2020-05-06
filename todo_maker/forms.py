from django.forms import Form, ModelForm
from django import forms
from todo_maker.models import Task

class TaskCreateForm(ModelForm):
    id = forms.CharField(required=False)
    task_accomplished = forms.ChoiceField(
            widget = forms.Select(attrs={'class': "form-control"}),
            choices=[(0, "Task Pending"), (1, "Task Accomplished")],
        )
    class Meta:
        model = Task
        fields = ("id", "title", "description", "task_accomplished",)
        widgets = {
            "title" : forms.TextInput(attrs={'class' : 'form-control'}),
            "description" : forms.Textarea(attrs={'class' : 'form-control', 'rows' : 2}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
