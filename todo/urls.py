from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('add/', views.task_create, name='task_create'),
    path('delete/<int:task_id>/', views.task_delete, name='task_delete'),
    path('update-status/<int:task_id>/', views.task_update_status, name='task_update_status'),
    path('task/<int:task_id>/', views.task_detail, name='detalhe_task'),
]
