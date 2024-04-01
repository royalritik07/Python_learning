from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

# Login
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.info(request, "Invalid Username")
            return redirect('/login/')
        
        user = authenticate(username = username, password = password)
        if user is None:
            messages.info(request, "Invalid Password")
            return redirect('/login/')
        else:
            login(request, user)
            return redirect('/')

    return render(request, 'login.html')


# Register
def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = User.objects.filter(username = username)
        if user.exists():
            messages.warning(request, "Username already exists!!")
            return redirect('/register/')

        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username
        )
        user.set_password(password)
        user.save()

        messages.info(request, "Account created successfully!!")
        return redirect('/register/')

    return render(request, 'register.html')

# Receipes
@login_required(login_url='/login/')
def receipes(request):
    if request.method == 'POST':
        receipe_name = request.POST.get('recepie_name')
        receipe_description = request.POST.get('recepie_description')
        receipe_image = request.FILES.get('recepie_image')

        Receipe.objects.create(
            receipe_name = receipe_name,
            receipe_description = receipe_description,
            receipe_image = receipe_image,
            )
        return redirect('/')
    
    querySet = Receipe.objects.all()

    # Search
    if request.GET.get('search'):
        querySet = querySet.filter(receipe_name__icontains = request.GET.get('search'))
    context = {'receipes': querySet}
        

    return render(request, 'receipes.html', context)


# Update
login_required(login_url='/login/')
def update_receipe(request, id):
    querySet = Receipe.objects.get(id = id)

    if request.method == 'POST':
        receipe_name = request.POST.get('recepie_name')
        receipe_description = request.POST.get('recepie_description')
        receipe_image = request.FILES.get('recepie_image')


        querySet.receipe_name = receipe_name
        querySet.receipe_description = receipe_description
        if receipe_image:
            querySet.receipe_image = receipe_image

        querySet.save()
        return redirect('/')

        


    context = {'receipe' : querySet}
    return render(request, 'update.html', context)  

@login_required(login_url='/login/')
def delete_receipe(request, id):
    querySet = Receipe.objects.get(id = id)
    querySet.delete()

    return redirect('/')

def logout_page(request):
    logout(request)
    return redirect('/login/')