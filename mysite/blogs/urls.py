from django.urls import path
from .views import BlogView
from rest_framework.routers import DefaultRouter
from django.urls import path, include


router = DefaultRouter()

router.register(r'', BlogView, basename='blog')

urlpatterns = [
    path("", include(router.urls) ),
    # path("/comment", Comment.as_view(), name="comment")
]
