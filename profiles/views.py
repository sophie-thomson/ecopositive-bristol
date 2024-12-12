from django.db.models import Count
from rest_framework import generics, filters
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(generics.ListAPIView):
    """
    List all profiles.
    No create view as profile creation is handled by django signals.
    """
    queryset = Profile.objects.annotate(
        endorsements_count=Count('owner__endorsing_user', distinct=True),
    ).order_by('-created_on')
    serializer_class = ProfileSerializer
    filter_backends = [
        filters.OrderingFilter
    ]
    ordering_fields = [
        'endorsements_count',
        'owner__endorsing_user__created_on',
    ]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update a profile if you're the owner.
    """
    # Sets the permission classes attribute
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        endorsements_count=Count('owner__endorsing_user', distinct=True),
    ).order_by('-created_on')
    serializer_class = ProfileSerializer
