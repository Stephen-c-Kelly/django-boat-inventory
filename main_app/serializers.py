from rest_framework import serializers
from .models import Boat, Cleaning, Captain

class CaptainSerializer(serializers.ModelSerializer):
   class Meta:
      model=Captain
      fields='__all__'
      
class BoatSerializer(serializers.ModelSerializer):
    clean_for_today=serializers.SerializerMethodField()
    captains=CaptainSerializer(many=True, read_only=True)
    class Meta:
        model = Boat
        fields = '__all__'
    def get_clean_for_today(self, obj):
       return obj.clean_for_today()

class CleaningSerializer(serializers.ModelSerializer):
  class Meta:
    model = Cleaning
    fields = '__all__'
    read_only_fields = ('boat',)



