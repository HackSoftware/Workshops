from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from rest_framework import status

from .authentication import CurlAuthenticator

class UniversalTruth(APIView):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JSONWebTokenAuthentication, CurlAuthenticator)

    def get(self, request):
        import ipdb; ipdb.set_trace()
        return Response(data={'answer': 42}, status=status.HTTP_200_OK)
