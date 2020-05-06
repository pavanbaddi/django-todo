from django.urls import path
from todo_maker import views
app_name = "todo_maker"

urlpatterns = [
    path('', views.List.as_view(),name="list-todo"),
    path('create', views.Create.as_view(),name="create-todo"),
    path('save', views.Create.as_view(),name="save-todo"),
    path('edit/<int:pk>', views.Create.as_view(),name="edit-todo"),
    # path('task-completed', views.TaskCompleted.as_view(),name="todo-task-completed"),
    # path('remove', views.Remove.as_view(),name="remove-todo"),
    # path('', ,name=""),
]