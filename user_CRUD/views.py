from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.db import IntegrityError


class Signup(View):

    def get(self, request):
        context = {'form': UserCreationForm}
        return render(request, 'user/signup.html', context)

    def post(self, request):
        if request.POST['password1'] == request.POST['password2']:
            try:
                # register user
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                return redirect('index')
            except IntegrityError:
                context = {'form': UserCreationForm,
                           'error': 'Username already exists'}
                return render(request, 'user/signup.html', context)
        context2 = {'form': UserCreationForm,
                    'error': 'Password Miss-Match'}
        return render(request, 'user/signup.html', context2)
