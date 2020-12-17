from django.contrib import admin
from .models import Pessoa

class PessoaAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'uuid','email','name','update_at', 'created_at',)
    list_filter = ('email',)
    
    date_hierarchy = 'update_at'

admin.site.register(Pessoa, PessoaAdmin)