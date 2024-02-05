from rest_framework.views import APIView
from rest_framework.response import Response

class Home(APIView):
  def get(self,request):
    content={'message': 'Welcome to the Boat Inventory api home route!'}
    return Response(content)


