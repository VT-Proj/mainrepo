from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import get_user_model

# Create your views here.
def home(request):
    return render(request, "authenticate/index.html")
# def signup(request):
#     if request.method =="POST":
#         # username= request.POST.get('username')
#         username= request.POST['username']
#         name=request.POST['name']
#         # empid=request.POST['empid']
#         email=request.POST['email']
#         password=request.POST['password']
#         password1=request.POST['password1']
        
#         if password == password1:
#             User = get_user_model()
#             myuser = User.objects.create_superuser(username=username,email=email, password=password)
#             myuser.name = name
#             myuser.save()
#             messages.success(request, "Your account is registered")
#             return redirect('signin')
#         else:
#             messages.error(request, "Passwords do not match")

#     return render(request, "authenticate/signup.html")
# def signin(request):
#     return render(request, "authenticate/signin.html")
# def signout(request):
#     pass