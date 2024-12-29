from rest_framework.views import APIView  # Importing APIView for handling API requests
from rest_framework.response import Response  # Importing Response for sending API responses
from rest_framework import status  # Importing status for HTTP status codes
from .serializers import RegisterSerializer, LoginSerializer  # Importing the serializers
from rest_framework.permissions import IsAuthenticated  # Importing permissions

# View for user registration
class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)  # Deserialize the request data
        if serializer.is_valid():  # Check if the data is valid
            serializer.save()  # Save the new user
            return Response(
                {
                    "message": "User registered successfully",
                    "username": serializer.data['username'],
                }, 
                status=status.HTTP_201_CREATED
            )  # Return success response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return error response if data is invalid


# # View for user login
class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)  # Deserialize the request data
        if serializer.is_valid():  # Check if the data is valid
            user = serializer.validated_data["user"]  # Get the user object from validated data
            return Response(
                {
                    "message": "Login successful",
                    "username": user.username,  # Access username from the user object
                    "firstname": user.firstname,
                    "lastname": user.lastname,
                    "email": user.email,
                    "phonenumber": user.phonenumber,
                },
                status=status.HTTP_200_OK
            )  # Return success response with user details
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return error response if data is invalid




class ProfileView(APIView):
    permission_classes = [IsAuthenticated]  # Ensure the user is authenticated

    def get(self, request):
        user = request.user  # Get the logged-in user
        return Response(
            {
                "username": user.username,
                "firstname": user.firstname,
                "lastname": user.lastname,
                "email": user.email,
                "phonenumber": user.phonenumber,
            },
            status=status.HTTP_200_OK
        )
