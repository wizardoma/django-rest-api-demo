from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.views import Response
from rest_framework import status
from profiles_api import serializers


class HelloApiView(APIView):
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        an_apiview = [
            'Uses a Http methods as functions',
            'Is similar to a traditional Django view',
            'Gives you the most control'
        ]

        return Response({'data': an_apiview})

    def post(self, request):
        serializers = self.serializer_class(data=request.data)
        if serializers.is_valid():
            name = serializers.validated_data.get('name')
            message = f'Hello {name}'

            return Response({'message': message})
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST )


class HelloViewSet(ViewSet):

    def list(self, request):
        a_viewset = [
            'Hello'
        ]

        return Response({'message': a_viewset})

    def retrieve(self, request, pk=None):
        return Response({'done': 'YEs o'})

