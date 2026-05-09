from django.contrib import admin
from .models import Grupo

# Register your models here.
@admin.register(Grupo)
class GrupoAdmin(admin.ModelAdmin):
    list_display = ('nombre','usuario')