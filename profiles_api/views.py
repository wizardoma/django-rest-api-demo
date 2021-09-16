from rest_framework.views import APIView
from rest_framework.views import Response

from profiles_api.response import JsonResponse


class HelloApiView(APIView):
    def get(self, request, format=None):
        an_apiview = [
            'Uses a Http methods as functions',
            'Is similar to a traditional Django view',
            'Gives you the most control'
        ]

        return Response(data=JsonResponse(is_error=False, status=200, data=an_apiview, error_message=None))
