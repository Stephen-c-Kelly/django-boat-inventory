from rest_framework import serializers
from .models import Boat, Cleaning, Captain
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Add a password field, make it write-only

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
    
    def create(self, validated_data):
      user = User.objects.create_user(
          username=validated_data['username'],
          email=validated_data['email'],
          password=validated_data['password']  # Ensures the password is hashed correctly
      )
      
      return user


class CaptainSerializer(serializers.ModelSerializer):
   class Meta:
      model=Captain
      fields='__all__'
      
class BoatSerializer(serializers.ModelSerializer):
    clean_for_today=serializers.SerializerMethodField()
    captains=CaptainSerializer(many=True, read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)
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


