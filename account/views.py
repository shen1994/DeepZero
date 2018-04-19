from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.http import HttpResponse
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import LoginForm
from home.forms import MenuServiceForm
from home.forms import MenuApplicationForm
from home.forms import MenuMessageForm

# Create your views here.
@csrf_exempt
def user_login(request):
    if request.method == "GET":
        login_form = LoginForm()
        return render(request, "account/login.html", \
                      {"form":login_form})
    
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_info = login_form.cleaned_data
            user = authenticate(username = user_info["username"], \
                                password = user_info["password"])
        if user:
            login(request, user)
            # return HttpResponseRedirect(reverse("account:service_post"))
            return HttpResponseRedirect("/account/service-post")
        else:
            return HttpResponseRedirect("/account/login/login-error")
            
def login_error(request):
    return render(request, "account/wrong_login.html")
 
@csrf_exempt
@login_required(login_url="/account/login/")
def service_post(request):
    if request.method == "GET":
        menu_services = MenuServiceForm()
        
        return render(request, "account/submit_service_article.html", \
               {"menu_services":menu_services})
    
    if request.method == "POST":     
        menu_services = MenuServiceForm(data=request.POST)
        if menu_services.is_valid():
            _ = menu_services.cleaned_data
            try:
                new_service = menu_services.save(commit=False)
                new_service.author = request.user
                new_service.save()
                return HttpResponse("0")
            except:
                return HttpResponse("1")
        else:
            return HttpResponse("2")

@csrf_exempt 
@login_required(login_url="/account/login/")      
def application_post(request):
    if request.method == "GET":
        menu_applications = MenuApplicationForm()
        
        return render(request, "account/submit_application_article.html", \
               {"menu_applications":menu_applications})
    
    if request.method == "POST":
        menu_applications = MenuApplicationForm(data=request.POST)
        if menu_applications.is_valid():
            _ = menu_applications.cleaned_data
            try:
                new_application = menu_applications.save(commit=False)
                new_application.author = request.user
                new_application.save()
                return HttpResponse("0")
            except:
                return HttpResponse("1")
        else:
            return HttpResponse("2")

@csrf_exempt
@login_required(login_url="/account/login/")         
def message_post(request):
    if request.method == "GET":
        menu_messages = MenuMessageForm()
        
        return render(request, "account/submit_message_article.html", \
               {"menu_messages":menu_messages})
    
    if request.method == "POST":
        menu_messages = MenuMessageForm(data=request.POST)
        if menu_messages.is_valid():
            _ = menu_messages.cleaned_data
            try:
                new_message = menu_messages.save(commit=False)
                new_message.author = request.user
                new_message.save()
                return HttpResponse("0")
            except:
                return HttpResponse("1")
        else:
            return HttpResponse("2")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    