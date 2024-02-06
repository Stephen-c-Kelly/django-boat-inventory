from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

from .models import Boat, Cleaning
from .serializers import BoatSerializer, CleaningSerializer


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

class CleaningListCreate(generics.ListCreateAPIView):
  serializer_class=CleaningSerializer
  
  def get_queryset(self):
    boat_id = self.kwargs['boat_id']
    return Cleaning.objects.filter(boat_id=boat_id)
  
  def perform_create(self, serializer):
    boat_id = self.kwargs['boat_id']
    boat = Boat.objects.get(id=boat_id)
    serializer.save(boat=boat)

class CleaningDetail(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = CleaningSerializer
  lookup_field = 'id'

  def get_queryset(self):
    boat_id = self.kwargs['boat_id']
    return Cleaning.objects.filter(boat_id=boat_id)
