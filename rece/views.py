from django.shortcuts import render,redirect
from django.http import HttpResponse
from rece.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.error(request, "Invalid Username")
            return redirect('/login/')
        
        user = authenticate(request, username = username, password = password)
        if user is None:
            messages.error(request, "Invalid password")
            return redirect('/login')
        else:
            login(request, user=user)
            return redirect('/recepe/')
            
    return render(request, 'login.html')

@login_required(login_url='/login')
def recepe_page(request):
    if request.method == "POST":
        data = request.POST
        reciepe_img = request.FILES.get('recipe_image')

        reciepe_name = data.get('name')
        reciepe_desc = data.get('description')
        
        receipe = Reciepe.objects.create(
            name = reciepe_name,
            description = reciepe_desc,
            reciepe_image = reciepe_img, )
        
        receipe.save()
        return redirect('/recepe/')
    
    queryset = Reciepe.objects.all()
    if request.GET.get('searchr'):
        queryset = queryset.filter(name__icontains = request.GET.get('searchr'))

    context = {'records':queryset}
    return render(request, 'recepe.html', context = context)

def logout_page(request):
    logout(request)
    return redirect('/login')


def about_page(request):
    return render(request, 'about.html')

def register_page(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username = username).exists():
            messages.error(request, "Username Already Taken")
        else:
            user = User.objects.create(first_name = first_name, last_name = last_name, username = username)

            user.set_password(password)

            user.save()
            messages.success(request, "Account Created Successfully")
            return redirect('/login')

            
    return render(request, 'register.html')

@login_required(login_url='/login')
def delete_recepe(request, id):
    record = Reciepe.objects.get(id = id)
    record.delete()

    return redirect('/recepe/')

@login_required(login_url='/login')
def update_recepe(request, id):
    queryset = Reciepe.objects.get(id = id)

    context = {"Recipe" : queryset}

    if request.method == "POST":
        data = request.POST
        reciepe_name = data.get('name')
        reciepe_desc = data.get('description')

        queryset.name = reciepe_name
        queryset.description = reciepe_desc

        if request.FILES.get('recipe_image'):
            reciepe_img = request.FILES.get('recipe_image')
            queryset.reciepe_image = reciepe_img
        
        queryset.save()
        
        return redirect('/recepe/')


    return render(request,'update.html', context = context)

