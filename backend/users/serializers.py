from rest_framework import serializers
from .models import User, Room, Bookings

class UserSerializer(serializers.ModelSerializer):
    class Meta:

        """
        Class for reading and writing to the User table
        """
        model = User
        fields = ['id','name','email','password']
        extra_kwargs = {
            'password': {'write_only' : True}
        }

    def create(self,validated_data):
        
        """
        Function for validating data and hashing the password
        """
        password = validated_data.pop('password',None)
        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)

        instance.save()
        return instance
    
class RoomSerializer(serializers.ModelSerializer):

    """
    Class for reading from and writing on the Room table
    """
    class Meta:
        model = Room
        fields = ['id', 'title', 'description', 'user', 'image']

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance
    
class BookingSerializer(serializers.ModelSerializer):

    """
    Class for writing and reading from the Bookings table
    """
    class Meta:
        model = Bookings
        fields = ['id', 'booking_start', 'booking_end', 'user', 'room_id']

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance
        