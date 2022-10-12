import datetime
from django.shortcuts import render
from todolist.models import Task
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    user = request.user
    context = {
        "username" : user.username,
        "todolist" : Task.objects.filter(user=user),
    }
    return render(request, "todolist.html", context)


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully registered!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Invalid username/password!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

def create_task(request):
    if request.method == "POST":
        task = request.POST

        Task.objects.create(
            user = request.user,
            date = datetime.datetime.now(),
            title = task.get("title"),
            description = task.get("description"),
            is_finished = False,
        )
        return HttpResponseRedirect(reverse('todolist:show_todolist'))
    return render(request, 'create_task.html')

def change_status(request, id):
    task = Task.objects.get(id = id)
    task.is_finished = not task.is_finished
    task.save()
    return HttpResponseRedirect(reverse('todolist:show_todolist'))

def delete_task(request, id):
    Task.objects.get(id = id).delete()
    return HttpResponseRedirect(reverse('todolist:show_todolist'))

def show_json(request):
    data = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@csrf_exempt
def create_json(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        task = Task.objects.create(
            title = title, 
            description = description,
            date = datetime.date.today(), 
            is_finished = False, 
            user=request.user
            )

        result = {
            'fields':{
                'title':task.title,
                'description':task.description,
                'is_finished':task.is_finished,
                'date':task.date,
            },
            'id':task.id
        }

        return JsonResponse(result)