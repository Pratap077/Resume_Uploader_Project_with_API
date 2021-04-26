from django.contrib import admin
from django.urls import path
from blog import views
from rest_framework import routers
from django.urls import include

router=routers.DefaultRouter()
router.register('student',views.Student_blockViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.project_api.as_view(),name='home'),
    path('detail/<int:pk>', views.detail_view, name='detail'),
    path('list/', views.list_view, name='list'),
    path('api/',include(router.urls))

]
