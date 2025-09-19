from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Standards)
class standardadmin(admin.ModelAdmin):
    list_display = ['id', 'names']

@admin.register(Section)
class sectionadmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'standard']

@admin.register(Student)
class studentadmin(admin.ModelAdmin):
    list_display = ['user', 'standard', 'section', 'created_at']
