from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenRefreshSerializer, TokenBlacklistSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenRefreshView, TokenBlacklistView
from .serializers import *



class SignUpView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]


class MyTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = response.data["refresh"]
        response.set_cookie("refresh", token, httponly=True)
        response.data.pop('refresh', None)
        return response

class MyTokenRefreshView(TokenRefreshView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        # Retrieve the refresh token from the cookie
        refresh_token = request.COOKIES.get('refresh')


        # Validate the refresh token and generate a new access token
        data = {'refresh': refresh_token}
        serializer = TokenRefreshSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        # Return the new access token
        return Response(serializer.validated_data, status=status.HTTP_200_OK)

class MyTokenBlacklistView(TokenBlacklistView):
    permission_classes = [AllowAny]
    def get(self, request, *args, **kwargs):
        refresh_token = request.COOKIES.get('refresh')

        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            response = Response({"message": "Token successfully blacklisted"}, status=200)
            response.delete_cookie('refresh')
            return response
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


