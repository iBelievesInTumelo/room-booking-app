from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializers import UserSerializer, BookingSerializer, RoomSerializer
from rest_framework.response import Response
from .models import User, Room, Bookings
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist, EmptyResultSet


class RegisterView(APIView):

    """
    Class for registering new users
    """
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class LoginView(APIView):

    """
    class to handle user login endpoint, token generation and cookie setting
    """

    def post(self,request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email = email).first()

        if user is None:
            raise AuthenticationFailed('Incorrect username or password')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect username or password')

        payload = {             # create a payload for creating a token using jwt
            'id': user.id,
            'exp' : datetime.datetime.now() + datetime.timedelta(minutes = 60),
            'iat' : datetime.datetime.now()
        }

        token = jwt.encode(payload, 'secret', algorithm = 'HS256')  # create a token for login

        response = Response()

        response.set_cookie(key = 'jwt', value = token, httponly = True)

        response.data = {
            'jwt': token
            }
        
        return response
    
class UserView(APIView):

    """ 
    End point for user information request
    """

    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')
        
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])

        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Authentication expired')
        
        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)

        return Response(serializer.data)

class RegisterRoomView(APIView):
    def post(self, request):
        serializer = RoomSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class LogoutView(APIView):

    """
    The purpose of the class is to delete the cookie
    """
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message' : 'Successfully logged out'
        }
        
        return response
    
class RoomView(APIView):

    """
    This class returns all registered rooms available
    """

    def get(self, request):
        queryset = Room.objects.all()
        serializer = RoomSerializer(queryset, many=True)

        return Response(serializer.data)



class BookingsView(APIView):

    """
    Class for creating and deleting bookings
    """

    def post(self, request):
        serializer = BookingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

    def delete(self, request, pk):
        try:
            booking = Bookings.objects.get(pk=pk)
            booking.delete()
            return Response(status=status.HTTP_200_OK)
        
        except ObjectDoesNotExist:
            return Response({'message':'Booking not found'},status=status.HTTP_400_BAD_REQUEST)
        
class UserBookings(APIView):

    def post(self, request):
            try:
                user_id = request.data
                queryset = Bookings.objects.filter(user=user_id['user'])
                serializer = BookingSerializer(queryset, many=True)
                return Response( serializer.data, status=status.HTTP_200_OK)

            except EmptyResultSet:
                return Response(status=status.HTTP_400_BAD_REQUEST)