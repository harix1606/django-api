from django.shortcuts import render
from rest_framework import viewsets
from .serializers import SongSerializer
from .models import Songs
from django.views.decorators.csrf import csrf_exempt
import datetime


class SongViewSet(viewsets.ModelViewSet):
    queryset = Songs.objects.all().order_by('name')
    serializer_class = SongSerializer

@csrf_exempt
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        check_user = User.objects.filter(email=email)
        valid_user = (len(list(check_user)) == 1)

        if (valid_user):
            current_user = email
            user_name = check_user.first().username
            request.session['current_user'] = current_user
            request.session['user_name'] = user_name
            return render(request, 'index.html', {'msg': 'Login successful'})
        else:
            return render(request, 'login.html', {'msg': 'Failed. Please try again'})
    else:
        return render(request, 'login.html')


@csrf_exempt
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        existing_email = User.objects.filter(email=email)
        is_new_user = (len(list(existing_email)) == 0)
        if (is_new_user):
            new_user = User.objects.create(username=username, email=email, password=password)
            new_user.save()
            return render(request, 'login.html', {'msg': 'Sign up successful'})
        else:
            return render(request, 'signup.html', {'msg': 'Error. Email already exists'})
    else:
        return render(request, 'signup.html')
