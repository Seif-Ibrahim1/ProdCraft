from django.db import models
import uuid

# User model representing a user in the system
class User(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
    )
    username = models.CharField(unique=True, max_length=20, null=False, blank=False)
    password = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField()

    def __str__(self) -> str:
        return self.username

# Task model representing a task associated with a user
class Task(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='tasks')
    name = models.CharField(max_length=100, null=False, blank=False)
    done = models.BooleanField(default=False)
    remind_at = models.DateTimeField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name

# Note model representing a note associated with a user
class Note(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='notes')
    title = models.CharField(max_length=100, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    remind_at = models.DateTimeField(null=True, blank=True)

    def __str__(self) -> str:
        return self.title
