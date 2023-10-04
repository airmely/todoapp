from django.urls import path

from . import views

urlpatterns = [
    path('', views.view_all_tasks, name='tasks'),
    path('create/', views.create_new_task, name='create_task'),
    path('update/<int:task_id>/', views.update_task, name='update_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.sign_up, name='register'),
]
