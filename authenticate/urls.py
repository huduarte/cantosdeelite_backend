from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .api_views import ObtainTokenPairWithColorView, CustomUserCreate, ChangePasswordView

urlpatterns = [
    path('user/create/', CustomUserCreate.as_view(), name="create_user"),
    path('token/obtain/', ObtainTokenPairWithColorView.as_view(), name='token_create'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('user/update/', ChangePasswordView.as_view(), name='update_user'),
]