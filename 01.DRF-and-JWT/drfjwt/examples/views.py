from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_framework import status


class UniversalTruth(APIView):
    def get(self, request):
        return Response(data={'answer': 42}, status=status.HTTP_200_OK)
