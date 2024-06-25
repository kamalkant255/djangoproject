from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HelloWorldViewSet

router = DefaultRouter()
router.register(r'hello', HelloWorldViewSet, basename='hello')

urlpatterns = [
    path('', include(router.urls)),
]
