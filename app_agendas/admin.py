from django.contrib import admin
from .models import Agenda_Publica

	
@admin.register(Agenda_Publica)
class Agenda_PublicaAdmin(admin.ModelAdmin):
	pass

