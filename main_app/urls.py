from django.urls import path
from .views import Home, BoatList, BoatDetail, CleaningListCreate, CleaningDetail, CaptainList, CaptainDetail, AddCaptainToBoat, RemoveCaptainFromBoat, CreateUserView, LoginView, VerifyUserView  

urlpatterns = [
  path('', Home.as_view(), name='home'),
  # new routes below 
  path('boats/', BoatList.as_view(), name='boat-list'),
  path('boat/<int:id>/', BoatDetail.as_view(), name='boat-detail'),

  path('boats/<int:boat_id>/add_captain/<int:captain_id>/', AddCaptainToBoat.as_view(),name='add-captain-to-boat'),
  path('boats/<int:boat_id>/remove_captain/<int:captain_id>/', RemoveCaptainFromBoat.as_view(),name='remove-captain-from-boat'),
  path('captains/', CaptainList.as_view(), name='captain-list'),
  path('captain/<int:id>/', CaptainDetail.as_view(), name='captain-detail'),
	path('boat/<int:boat_id>/cleaning/',CleaningListCreate.as_view(), name='cleaning-list-create'),
	path('boat/<int:boat_id>/cleaning/<int:id>/', CleaningDetail.as_view(),name='cleaning-detail'),
  
  path('users/register/', CreateUserView.as_view(), name='register'),
  path('users/login/', LoginView.as_view(), name='login'),
  path('users/token/refresh/', VerifyUserView.as_view(), name='token_refresh'),
]

#  boats and cleaning both use <int:id> in the path...unsure if that's an issue.

