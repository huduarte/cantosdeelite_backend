from django.urls import path
from .api_views import ConfigListView

urlpatterns = [
    path('', ConfigListView.as_view(), name="config_list"),
]