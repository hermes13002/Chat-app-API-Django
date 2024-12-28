from rest_framework import serializers  # Importing Django REST framework serializers
from django.contrib.auth import authenticate  # Importing Django's authentication method
from .models import User  # Importing the User model

# Serializer for user registration
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Password field, write-only

    class Meta:
        model = User  # Specifying the model to be serialized
        fields = ['username', 'firstname', 'lastname', 'email', 'phonenumber', 'password']  # Fields to be included in the serialization

    # Method to create a new user
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            firstname = validated_data['firstname'],
            lastname = validated_data['lastname'],
            email=validated_data['email'],
            phonenumber = validated_data['phonenumber'],
            password=validated_data['password']
        )
        return user

# # Serializer for user login
# class LoginSerializer(serializers.Serializer):
#     email = serializers.EmailField()  # Email field
#     password = serializers.CharField(write_only=True)  # Password field, write-only

#     # Method to validate user credentials
#     def validate(self, data):
#         user = authenticate(username=data['email'], password=data['password'])
#         if not user:
#             raise serializers.ValidationError("Invalid credentials")  # Raise error if credentials are invalid
#         return {"user": user, "email": data['email']}


# Serializer for user login
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()  # Username field
    password = serializers.CharField(write_only=True)  # Password field, write-only

    # Method to validate user credentials
    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if not user:
            raise serializers.ValidationError("Invalid credentials")  # Raise error if credentials are invalid
        # return {"user": user}
        return {"user": user, "email": data['email']}
