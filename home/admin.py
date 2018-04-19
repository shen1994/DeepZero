from django.contrib import admin

from .models import MenuService
from .models import MenuApplication
from .models import MenuMessage

# Register your models here.

class MenuServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created")
    list_filter = ("author", "created")
    search_field = ("title",)
    ordering = ["created",]

admin.site.register(MenuService, MenuServiceAdmin)

class MenuApplicationAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created")
    list_filter = ("author", "created")
    search_field = ("title",)
    ordering = ["created",]

admin.site.register(MenuApplication, MenuApplicationAdmin)

class MenuMessageAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created")
    list_filter = ("author", "created")
    search_field = ("title",)
    ordering = ["created",]

admin.site.register(MenuMessage, MenuMessageAdmin)
