from django.urls import path
from .views import Home, BoatList, BoatDetail, CleaningListCreate, CleaningDetail

urlpatterns = [
  path('', Home.as_view(), name='home'),
  # new routes below 
  path('boats/', BoatList.as_view(), name='boat-list'),
  path('boat/<int:id>/', BoatDetail.as_view(), name='boat-detail'),
	path('boat/<int:boat_id>/cleaning/',CleaningListCreate.as_view(), name='cleaning-list-create'),
	path('boat/<int:boat_id>/cleaning/<int:id>/', CleaningDetail.as_view(),name='cleaning-detail')
]

#  boats and cleaning both use <int:id> in the path...unsure if that's an issue.

