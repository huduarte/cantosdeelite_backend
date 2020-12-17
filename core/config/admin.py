from django.contrib import admin
from core.config.models import Config

class ConfigAdmin(admin.ModelAdmin):
    list_display = ('name','endpoint','is_active')
    
    def save_model(self, request, obj, form, change):
        for config in Config.objects.all():
            config.is_active = False;
            config.save()
        super(ConfigAdmin, self).save_model(request, obj, form, change)

admin.site.register(Config, ConfigAdmin)