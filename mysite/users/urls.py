# users/urls.py
from django.urls import path, include
from .views import RegisterView, LoginView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register(r'', BlogView, basename='blog')
# router.register(r'register', RegisterView, basename='register')
# router.register(r'login', LoginView, basename='login')
# router.register(r'token', TokenObtainPairView, basename='token')
# router.register(r'token/refresh', TokenRefreshView, basename='refresh-token')


urlpatterns = [
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('login/', LoginView.as_view(), name='auth_login'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("", include(router.urls) ),
]