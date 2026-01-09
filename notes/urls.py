from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'notes'

urlpatterns = [
    # The root path (homepage) now points to the dashboard view
    path('', views.home, name='dashboard'),

    path('notes/', views.note, name='note'),
    path('files/', views.files, name='files'),
    path('search/', views.search_notes, name='search_notes'),

    # Auth routes
    path('login/', auth_views.LoginView.as_view(template_name='notes/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('about/', views.about, name='about'),

    # Notes CRUD
    path('note/create/', views.note_create, name='create'),
    path('note/<int:pk>/', views.note_detail, name='detail'),
    path('note/<int:pk>/edit/', views.note_update, name='edit'),
    path('note/<int:pk>/delete/', views.note_delete, name='delete'),
    
    path('note/<int:pk>/attachment/', views.serve_attachment, name='serve_attachment'),

    # Task CRUD
    path('calendar/', views.calendar_view, name='calendar'),
    path('calendar/<int:year>/<int:month>/', views.calendar_view, name='calendar_month'),
    path('calendar/<int:year>/<int:month>/<int:day>/', views.calendar_day_view, name='calendar_day'),
    path('task/', views.task, name='task'),
    path('task/create/', views.task_create, name='task_create'),
    
    # --- REMOVED the subtask_create URL ---
    
    path('task/<int:pk>/edit/', views.task_update, name='task_edit'),
    path('task/<int:pk>/delete/', views.task_delete, name='task_delete'),
    path('task-notifications/', views.check_task_notifications, name='task_notifications'),
]