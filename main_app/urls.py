from django.urls import path
from .views import Home, BoatList, BoatDetail

urlpatterns = [
  path('', Home.as_view(), name='home'),
  # new routes below 
  path('boats/', BoatList.as_view(), name='boat-list'),
  path('boat/<int:id>/', BoatDetail.as_view(), name='boat-detail'),
]
