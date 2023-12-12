from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, Task, Note
from .serializer import User_serializer, Task_serializer, Note_serializer
from django.contrib.auth.hashers import make_password, check_password

# View to provide a list of available API endpoints
def endpoints(request):
    data = ['api/v1/users/', 'api/v1/users/:username', 'api/v1/:username/tasks',
            'api/v1/:username/tasks/:id', 'api/v1/users/:username/check_password',
            'api/v1/:username/notes', 'api/v1/:username/notes/:id'
            ]
    return Response(data)

# View for handling user-related operations
@api_view(['GET', 'POST'])
def users_view(request):
    # Handling GET requests for user retrieval
    if request.method == 'GET':
        users = User.objects.filter()
        serializer = User_serializer(users, many=True)
        return Response(serializer.data)
    
    # Handling POST requests for user creation
    if request.method == 'POST':
        data = request.data
        username = data['username']
        password = data['password']
        email = data['email']
        user = User.objects.create(username=username, password=make_password(password), email=email)
        serializer = User_serializer(instance=user, many=False)
        return Response(serializer.data, status=201)

# View for handling individual user operations
@api_view(['GET', 'PUT', 'DELETE'])
def user_by_username(request, username):
    user = User.objects.get(username=username)
    if request.method == 'GET':
        serializer = User_serializer(user, many=False)
        return Response(serializer.data)

    if request.method == 'PUT':
        # Handling PUT requests for user updates
        data = request.data
        if data.get('password') is not None:
            password = data['password']
            user.password = make_password(password)
        if data.get('email') is not None:
            user.email  = data['email']
    
        user.save()

        serializer = User_serializer(instance=user, many=False)
        return Response(serializer.data)

    if request.method == 'DELETE':
        # Handling DELETE requests for user deletion
        user.delete()
        return Response()

    return Response()

# View for checking if a given password matches a user's password
@api_view(['GET', 'POST'])
def check_matching_password(request, username):
    user = User.objects.get(username=username)
    if request.method == 'GET':
        return Response()

    if request.method == 'POST':
        # Handling POST requests for password matching
        oldPass = user.password
        if(check_password(request.data['password'], oldPass)):
            return Response({"matching": True})
        else:
            return Response({"matching": False})

# View for handling tasks related to a specific user
@api_view(['GET', 'POST'])
def tasks_by_username(request, username):
    user = User.objects.get(username=username)
    if request.method == 'GET':
        # Handling GET requests for tasks retrieval
        tasks = Task.objects.filter(user=user)
        serializer = Task_serializer(tasks, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        # Handling POST requests for task creation
        data = request.data
        task = Task.objects.create(user=user, name=data['name'])
        if data.get('remind_at') is not None:
            task.remind_at = data['remind_at']
        
        serializer = Task_serializer(task, many=False)
        task.save()
        return Response(serializer.data)

    return Response()

# View for handling individual task operations
@api_view(['GET', 'PUT', 'DELETE'])
def task_by_id(request, username, id):
    task = Task.objects.get(id=id)
    if request.method == 'GET':
        # Handling GET requests for individual task retrieval
        serializer = Task_serializer(task, many=False)
        return Response(serializer.data)

    if request.method == 'PUT':
        # Handling PUT requests for task updates
        data = request.data
        if data.get('name') is not None:
            task.name = data['name']
        if data.get('done') is not None:
            task.done  = data['done']
        if data.get('remind_at') is not None:
            task.remind_at = data['remind_at']
    
        task.save()

        serializer = Task_serializer(instance=task, many=False)
        return Response(serializer.data)

    if request.method == 'DELETE':
        # Handling DELETE requests for task deletion
        task.delete()
        return Response()

    return Response()

# View for handling notes related to a specific user
@api_view(['GET', 'POST'])
def notes_by_username(request, username):
    user = User.objects.get(username=username)
    if request.method == 'GET':
        # Handling GET requests for notes retrieval
        notes = Task.objects.filter(user=user)
        serializer = Note_serializer(notes, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        # Handling POST requests for note creation
        data = request.data
        note = Note.objects.create(user=user, title=data['title'], content=data['content'])
        if data.get('remind_at') is not None:
            note.remind_at = data['remind_at']
        
        serializer = Note_serializer(note, many=False)
        note.save()
        return Response(serializer.data)

    return Response()

# View for handling individual note operations
@api_view(['GET', 'PUT', 'DELETE'])
def note_by_id(request, username, id):
    note = Note.objects.get(id=id)
    if request.method == 'GET':
        # Handling GET requests for individual note retrieval
        serializer = Note_serializer(note, many=False)
        return Response(serializer.data)

    if request.method == 'PUT':
        # Handling PUT requests for note updates
        data = request.data
        if data.get('title') is not None:
            note.title = data['title']
        if data.get('content') is not None:
            note.content  = data['content']
        if data.get('remind_at') is not None:
            note.remind_at = data['remind_at']
    
        note.save()

        serializer = Note_serializer(instance=note, many=False)
        return Response(serializer.data)

    if request.method == 'DELETE':
        # Handling DELETE requests for note deletion
        note.delete()
        return Response()

    return Response()
