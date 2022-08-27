from .models import User
from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField


class UserCreationSerailizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'password',]

    def validate(self, attrs):
        username = User.objects.filter(username=attrs['username']).exists()
        email = User.objects.filter(email=attrs['email']).exists()
        phone_number = User.objects.filter(phone_number=attrs['phone_number']).exists()

        if username:
            raise serializers.ValidationError("User with username already exists.")
        
        if email:
            raise serializers.ValidationError("User with email already exists.")
        
        if phone_number:
            raise serializers.ValidationError("User with phonenumber already exists.")
        
        return super().validate(attrs)


        

