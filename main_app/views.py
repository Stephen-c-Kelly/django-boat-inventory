from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

from .models import Boat
from .serializers import BoatSerializer


class Home(APIView):
  def get(self,request):
    content={'message': 'Welcome to the Boat Inventory api home route!'}
    return Response(content)


class BoatList(generics.ListCreateAPIView):
  queryset = Boat.objects.all()
  serializer_class = BoatSerializer

class BoatDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Boat.objects.all()
  serializer_class = BoatSerializer
  lookup_field = 'id'

