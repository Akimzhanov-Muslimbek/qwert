from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.todo_list, name='todo_list'),
    path('<int:id>/', views.todo_detail, name='todo_detail'),
    path('create/', views.todo_create, name='todo_create'),
    path('<int:id>/delete/', views.todo_delete, name='todo_delete'),
]
