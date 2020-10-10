from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User ,auth 
# Create your views here.


def register(request) :

    if request.method == 'POST':
        first_name = request.POST['first_name']

        last_name = request.POST.get('last_name',False)

        username = request.POST['user_name']

        email = request.POST['email']

        password = request.POST['password']

        confirmpassword = request.POST['confirmpassword']


        user = User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)

        user.save()
        
        messages.info(request,'User Created')
        
        return redirect('register')
    else: 
        return render(request,'register.html')