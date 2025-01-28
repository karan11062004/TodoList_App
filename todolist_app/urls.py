from django.urls import path
from todolist_app import views
urlpatterns = [
    path('todolist/',views.todolist,name='todolist'),
    path('delete/<task_id>',views.delete_task,name='delete'),
    path('edit/<task_id>',views.edit_task,name='edit'),
    path('done/<task_id>',views.done_task,name='done'),
    path('undone/<task_id>',views.undone_task,name='undone'),

]
