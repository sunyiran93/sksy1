from django.urls import path
from .import views

urlpatterns = [
    path('', views.overview, name='overview'),
    path('imprint', views.imprint, name='imprint'),
    path('update-imprint/<str:pk>/', views.updateImprint, name='update-imprint'),
    path('create-task', views.createTask, name='create-task'),
    path('update-task/<int:id>', views.updateTask, name='update-task'),
    path('delete-task/<str:pk>/', views.deleteTask, name='delete-task'),
]