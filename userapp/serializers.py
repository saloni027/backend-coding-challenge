from django.contrib.auth.models import User
from rest_framework import serializers

class RegistrationSerializer(serializers.ModelSerializer):
    """ 
    Serializer for registration of Users
    """
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def save(self):
        """ 
        Override save method for validating data before save
        """
        password = self.validated_data['password']
        password2 = self.validated_data['password']
        
        if password != password2:
            raise serializers.ValidationError({'error': 'Password and Password2 should be same'})
        
        account = User(username=self.validated_data['username'])
        account.set_password(password)
        account.save()
        return account