from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import User, Task, Note

# Serializer for the Note model
class Note_serializer(ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'

# Serializer for the Task model
class Task_serializer(ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

# Serializer for the User model
class User_serializer(ModelSerializer):
    # Nested serializers for related Task and Note objects
    tasks = Task_serializer(many=True)
    notes = Note_serializer(many=True)

    class Meta:
        model = User
        fields = '__all__'
