from upload.models import *
from upload.api.serializer import UserSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class UserViewSet(viewsets.ModelViewSet):
 queryset = Resume.objects.all()
 serializer_class = UserSerializer