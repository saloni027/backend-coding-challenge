from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response

from userapp import models
from userapp.serializers import RegistrationSerializer

@api_view(['POST',])
def logout_view(request):
    """ 
    View for logout of Users 
    """
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status= status.HTTP_200_OK)
        
@api_view(['POST',])
def registration_view(request):
    """ 
    View for Registering Users 
    """
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "Registration Successful!"
            data['username'] = account.username
            token = Token.objects.get(user=account).key
            data['token'] = token           
        else:
            data = serializer.errors
        return Response(data, status=status.HTTP_201_CREATED)
            
        
        

