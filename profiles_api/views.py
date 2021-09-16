from rest_framework.viewsets import ModelViewSet

from profiles_api import models
from rest_framework import filters
from profiles_api import serializers
from rest_framework.authentication import TokenAuthentication

from profiles_api import permissions


class UserProfileViewSet(ModelViewSet):
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)

