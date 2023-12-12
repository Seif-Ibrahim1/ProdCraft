from django.urls import path
from . import views

# URL patterns for ProdCraft API
urlpatterns = [
    # Endpoint to retrieve a list of available API endpoints
    path('api/v1/endpoints/', views.endpoints),

    # User-related endpoints
    path('api/v1/users/', views.users_view),
    path('api/v1/users/<str:username>/', views.user_by_username),
    path('api/v1/users/<str:username>/check_password/', views.check_matching_password),

    # Task-related endpoints
    path('api/v1/users/<str:username>/tasks/', views.tasks_by_username),
    path('api/v1/users/<str:username>/tasks/<str:id>/', views.task_by_id),

    # Note-related endpoints
    path('api/v1/users/<str:username>/notes/', views.notes_by_username),
    path('api/v1/users/<str:username>/notes/<str:id>/', views.note_by_id),
]
