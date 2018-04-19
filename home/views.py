from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

from .models import MenuService
from .models import MenuApplication
from .models import MenuMessage

# Create your views here.

def menu_process(request):
    SERVICE_SHOW = 6
    APPLICATION_SHOW = 6
    MESSAGE_SHOW = 13
    
    USER = "shen1994"
    
    service_count = 0
    services = MenuService.objects.all()
    for service in services:
        service_count += 1
    if(service_count <= SERVICE_SHOW):
        user_name = "shen1995"
        user = User.objects.filter(username=user_name)
        if not user:
            user = User()
            user.username = user_name
            user.set_password("123456")
            user.email = "XXX@XXX.com"
            user.save()
        user = User.objects.get(username=user_name)
        for i in range(SERVICE_SHOW - service_count):
            new_service = MenuService()
            new_service.author = user
            new_service.title = "空"
            new_service.body = "空"
            new_service.save()
        services = MenuService.objects.all()[0:SERVICE_SHOW]
    else:
        services = services[0:SERVICE_SHOW]

    application_count = 0
    applications = MenuApplication.objects.all()
    for application in applications:
        application_count += 1
    if(application_count <= APPLICATION_SHOW):
        user_name = "shen1995"
        user = User.objects.filter(username=user_name)
        if not user:
            user = User()
            user.username = user_name
            user.set_password("123456")
            user.email = "XXX@XXX.com"
            user.save()
        user = User.objects.get(username=user_name)
        for i in range(APPLICATION_SHOW - application_count):
            new_application = MenuApplication()
            new_application.author = user
            new_application.title = "空"
            new_application.body = "空"
            new_application.save()
        applications = MenuApplication.objects.all()[0:APPLICATION_SHOW]
    else:
        applications = applications[0:APPLICATION_SHOW]

    message_count = 0
    messages = MenuMessage.objects.all()
    for message in messages:
        message_count += 1
    if(message_count <= MESSAGE_SHOW):
        user_name = "shen1995"
        user = User.objects.filter(username=user_name)
        if not user:
            user = User()
            user.username = user_name
            user.set_password("123456")
            user.email = "XXX@XXX.com"
            user.save()
        user = User.objects.get(username=user_name)
        for i in range(MESSAGE_SHOW - message_count):
            new_message = MenuMessage()
            new_message.author = user
            new_message.title = "空"
            new_message.body = "空"
            new_message.save()
        messages = MenuMessage.objects.all()[0:MESSAGE_SHOW]
    else:
        messages = messages[0:MESSAGE_SHOW]

    return render(request, "home/menu.html", \
                  {"services":services, "applications":applications, "messages":messages})

def menu_service_title(request):
    services = MenuService.objects.all()
    paginator = Paginator(services, 8)
    page = request.GET.get('page')
    try:
        current_page = paginator.page(page)
        service_titles = current_page.object_list
    except PageNotAnInteger:
        current_page = paginator.page(1)
        service_titles = current_page.object_list
    except EmptyPage:
        current_page = paginator.page(paginator.num_pages)
        service_titles = current_page.object_list
    return render(request, "home/service_title_list.html", \
                  {"service_titles":service_titles, "page":current_page})
    
def service_title_detail(request, service_id):
    service_content = get_object_or_404(MenuService, id=service_id)
    return render(request, "home/service_title_content.html", \
                  {"service_content":service_content})
        
def menu_application_title(request):
    applications = MenuApplication.objects.all()
    paginator = Paginator(applications, 8)
    page = request.GET.get('page')
    try:
        current_page = paginator.page(page)
        application_titles = current_page.object_list
    except PageNotAnInteger:
        current_page = paginator.page(1)
        application_titles = current_page.object_list
    except EmptyPage:
        current_page = paginator.page(paginator.num_pages)
        application_titles = current_page.object_list
    return render(request, "home/application_title_list.html", \
                  {"application_titles":application_titles, "page":current_page})
    
def application_title_detail(request, application_id):
    application_content = get_object_or_404(MenuApplication, id=application_id)
    return render(request, "home/application_title_content.html", \
                  {"application_content":application_content})

def menu_message_title(request):
    messages = MenuMessage.objects.all()
    paginator = Paginator(messages, 8)
    page = request.GET.get('page')
    try:
        current_page = paginator.page(page)
        message_titles = current_page.object_list
    except PageNotAnInteger:
        current_page = paginator.page(1)
        message_titles = current_page.object_list
    except EmptyPage:
        current_page = paginator.page(paginator.num_pages)
        message_titles = current_page.object_list
    return render(request, "home/message_title_list.html", \
                  {"message_titles":message_titles, "page":current_page})

def message_title_detail(request, message_id):
    message_content = get_object_or_404(MenuMessage, id=message_id)
    return render(request, "home/message_title_content.html", \
                  {"message_content":message_content})

def menu_service_content(request, service_id):
    service_content = get_object_or_404(MenuService, id=service_id)
    return render(request, "home/service_content.html", \
                  {"service_content":service_content})

def menu_application_content(request, application_id):
    application_content = get_object_or_404(MenuApplication, id=application_id)
    return render(request, "home/application_content.html", \
                  {"application_content":application_content})
    
def menu_message_content(request, message_id):
    message_content = get_object_or_404(MenuMessage, id=message_id)
    return render(request, "home/message_content.html", \
                  {"message_content":message_content})
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    