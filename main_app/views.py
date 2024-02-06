from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

from .models import Boat, Cleaning, Captain
from .serializers import BoatSerializer, CleaningSerializer, CaptainSerializer


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
  def retrieve(self, request, *args, **kwargs):
    instance=self.get_object()
    serializer=self.get_serializer(instance)

    captains_not_associated=Captain.objects.exclude(id__in=instance.toys.all())
    captains_serializer=CaptainSerializer(captains_not_associated, 
    many=True)
    
    return Response({
      'Boat': serializer.data,
      'captains_not_associated': captains_serializer.data,
    })

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

class CaptainList(generics.ListCreateAPIView):
  queryset = Captain.objects.all()
  serializer_class = CaptainSerializer

class CaptainDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Captain.objects.all()
  serializer_class = CaptainSerializer
  lookup_field = 'id'


class AddCaptainToBoat(APIView):
  def post(self, request, boat_id, captain_id):
    boat = Boat.objects.get(id=boat_id)
    captain = Captain.objects.get(id=captain_id)
    boat.captains.add(captain)
    return Response ({'message': f'Captain {captain.name} is added to {boat.make}-{boat.model} '})
  
class RemoveCaptainFromBoat(APIView):
  def post(self, request, boat_id, captain_id):
    boat = Boat.objects.get(id=boat_id)
    captain = Captain.objects.get(id=captain_id)
    boat.captains.remove(captain)
    return Response ({'message': f'Captain {captain.name} is removed from {boat.make}-{boat.model} '})
