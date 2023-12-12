from django.contrib import admin
from .models import User, Task, Note

# Registering models for the Django admin interface
admin.site.register(User)  # Registering the User model
admin.site.register(Task)  # Registering the Task model
admin.site.register(Note)  # Registering the Note model
