from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status, permissions
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from .models import Boat, Cleaning, Captain
from .serializers import BoatSerializer, CleaningSerializer, CaptainSerializer, UserSerializer


class Home(APIView):
  def get(self,request):
    content={'message': 'Welcome to the Boat Inventory api home route!'}
    return Response(content)

class BoatList(generics.ListCreateAPIView):
  # queryset = Boat.objects.all()
  serializer_class = BoatSerializer
  permission_classes=[permissions.IsAuthenticated]

  def get_queryset(self):
    user=self.request.user
    return Boat.objects.filter(user=user)

  def perform_create(self, serializer):
    serializer.save(user=self.request.user)

class BoatDetail(generics.RetrieveUpdateDestroyAPIView):
  # queryset = Boat.objects.all()
  serializer_class = BoatSerializer
  lookup_field = 'id'
  
  def get_queryset(self):
    user=self.request.user
    return Boat.objects.filter(user=user)

  def retrieve(self, request, *args, **kwargs):
    instance=self.get_object()
    serializer=self.get_serializer(instance)

    captains_not_associated=Captain.objects.exclude(id__in=instance.captains.all())
    captains_serializer=CaptainSerializer(captains_not_associated, 
    many=True)
    
    return Response({
      'Boat': serializer.data,
      'captains_not_associated': captains_serializer.data,
    })
  
  def perform_update(self, serializer):
    boat = self.get_object()
    if boat.user != self.request.user:
        raise PermissionDenied({"message": "You do not have permission to edit this boat."})
    serializer.save()

  def perform_destroy(self, instance):
    if instance.user != self.request.user:
        raise PermissionDenied({"message": "You do not have permission to delete this boat."})
    instance.delete()


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

class CreateUserView(generics.CreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer

  def create(self, request, *args, **kwargs):
    response = super().create(request, *args, **kwargs)
    user = User.objects.get(username=response.data['username'])
    refresh = RefreshToken.for_user(user)
    return Response({
      'refresh': str(refresh),
      'access': str(refresh.access_token),
      'user': response.data
    })
  
class LoginView(APIView):
  permission_classes = [permissions.AllowAny]

  def post(self, request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
      refresh = RefreshToken.for_user(user)
      return Response({
        'refresh': str(refresh),
        'access': str(refresh.access_token),
        'user': UserSerializer(user).data
      })
    return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
  
class VerifyUserView(APIView):
  permission_classes = [permissions.IsAuthenticated]

  def get(self, request):
    user = User.objects.get(username=request.user)  # Fetch user profile
    refresh = RefreshToken.for_user(request.user)  # Generate new refresh token
    return Response({
      'refresh': str(refresh),
      'access': str(refresh.access_token),
      'user': UserSerializer(user).data
    })