from rest_framework import generics, permissions, status, views
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserRegistrationSerializer
from django.contrib.auth import get_user_model
User = get_user_model()

class RegisterView(views.APIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserRegistrationSerializer

class LoginView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny)

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == status.HTTP_200_OK:
            user = User.objects.get(email=request.data['email'])
            response.data['email'] = user.email
            response.data['first_name'] = user.first_name
            response.data['last_name'] = user.last_name
        return response

