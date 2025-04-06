from django.urls import path
from .views import TodoListCreate, TodoDetail

urlpatterns = [
    path('todos/', TodoListCreate.as_view(), name='todo-list'),
    path('todos/<int:pk>/', TodoDetail.as_view(), name='todo-detail'),
]
