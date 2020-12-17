from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings 

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

admin.autodiscover()

admin.site.site_header = settings.PROJECT_NAME if settings.PROJECT_NAME else u'Core Admin'
admin.site.site_title =  settings.PROJECT_NAME if settings.PROJECT_NAME else u'Core Admin'

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/pessoa/', include('pessoa.urls')),

]
