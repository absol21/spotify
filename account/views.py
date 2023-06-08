from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterSerializer,ChangePasswordSerializer,ForgotPasswordSerializer,ForgotPasswordCompleteSerializer
from .models import User
from .permissions import IsActivePermissions
from drf_yasg.utils import swagger_auto_schema

class RegisterView(APIView):
    @swagger_auto_schema(request_body=RegisterSerializer())
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response("Successfully registered", 201)

class ActivationView(APIView):
    def get(self, request, email, activation_code):
        user = User.objects.filter(email=email, activation_code=activation_code).first()
        if not user:
            return Response("User doesn't exist", 400)
        user.activation_code = ''
        user.is_active = True
        user.save()
        return Response('Activated', 200)


class ChangePasswordView(APIView):
    permission_classes = [IsActivePermissions]
    
    @swagger_auto_schema(request_body=ChangePasswordSerializer())
    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception = True):
            serializer.set_new_password()
            return Response('Status: 200. Пароль успешно обнавлен')
         

class ForgotPasswordView(APIView):
    @swagger_auto_schema(request_body=ForgotPasswordSerializer())
    def post(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.send_verification_email()
            return Response('Вы выслали сообщение для восстановления')
        

class ForgotPasswordCompleteView(APIView):
    @swagger_auto_schema(request_body=ForgotPasswordCompleteSerializer())
    def post(self, request):
        serializer = ForgotPasswordCompleteSerializer(data=request.data) 
        if serializer.is_valid(raise_exception=True):
            serializer.set_new_password()
            return Response('Пароль успешно изменен')