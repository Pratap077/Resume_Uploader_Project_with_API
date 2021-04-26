from django.urls import path, include
from upload.api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('resume', views.UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls))
]
