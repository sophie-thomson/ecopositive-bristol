from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Endorsement
from .serializers import EndorsementSerializer
from rest_framework.exceptions import ValidationError


class EndorsementList(generics.ListCreateAPIView):
    """
    List all endorsers, i.e. all instances of a user
    endorsing a company.
    Create an endorsement, i.e. endorse a company if logged in.
    Perform_create associates the current logged in user with an
    endorsement and checks if the endorser is the company owner.
    """
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
    ]
    queryset = Endorsement.objects.all()
    serializer_class = EndorsementSerializer

    def perform_create(self, serializer):
        owner = self.request.user
        endorsed_company = serializer.validated_data.get(
            'endorsed_company'
        )

        if owner == endorsed_company.owner:
            raise ValidationError({
                'detail': 'You cannot endorse your own company'
            })

        serializer.save(owner=self.request.user)


class EndorsementDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve an endorsement.
    No Update view, as we either endorse or unendorse a company.
    Destroy an endorsement to unendorse a company if endorsement owner.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Endorsement.objects.all()
    serializer_class = EndorsementSerializer
