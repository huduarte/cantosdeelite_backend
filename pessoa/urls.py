from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .api_views import PessoaUpdateView, PessoaListView

urlpatterns = [
    path('<uuid:uuid>/', PessoaUpdateView.as_view(), name="pessoa_update"),    
    path('', PessoaListView.as_view(), name="pessoa_list"),       
]