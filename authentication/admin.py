from django.contrib import admin
from .models import User
# Register your models here.

# class UserAdmin(admin.ModelAdmin):
#     model = User
#     list_display = ('username', 'email', 'phone_number') 
   
# admin.site.register(UserAdmin, User)   
admin.site.register(User) 