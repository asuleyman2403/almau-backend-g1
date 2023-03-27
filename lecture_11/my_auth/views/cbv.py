from rest_framework.views import APIView, Response
from my_auth.serializers import UserSerializer, ChangePasswordSerializer, ForgotPasswordSerializer, ResetPasswordSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from my_auth.models import User, ResetPassword
from django.core.mail import send_mail
from django import template
from datetime import datetime, timezone

import uuid

TOKEN_LIFETIME = 1 * 60 * 60

class UsersAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        data = request.data
        serializer = UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)


class ChangeAPIView(APIView):
    permission_classes = (IsAuthenticated, )

    def put(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        old_password = request.data['old_password']
        new_password = request.data['new_password']
        user = User.objects.get(username=request.user.username)
        if user.check_password(old_password):
            user.set_password(new_password)
            user.save()
            user_serializer = UserSerializer(user)
            return Response(user_serializer.data, status=200)
        else:
            return Response({'message': 'Incorrect old password'}, status=400)


class ForgotPasswordAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = request.data['email']
        try:
            token = uuid.uuid4()
            email_template = template.loader.get_template('my_auth/reset-password.html')
            email_content = email_template.render({'FRONTEND_RESET_PASSWORD_URL': 'http://localhost:5500/verify-email',
                                                   'TOKEN': token})
            send_mail(subject='Reset your password', message='', html_message=email_content,
                      from_email='settings.EMAIL_HOST_USER',
                      recipient_list=[email],
                      fail_silently=False)
            reset_password = ResetPassword(email=email, token=token)
            reset_password.save()
            return Response({'message': 'Please, check your email'}, status=200)
        except:
            return Response({'message': 'Internal Server Error'}, status=500)


class ResetPasswordAPIView(APIView):
    permission_classes = (AllowAny,)

    def put(self, request, token):
        data = request.data
        serializer = ResetPasswordSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        new_password = data['new_password']
        repeat_password = data['repeat_password']

        if new_password == repeat_password:
            try:
                print(token)
                reset_password = ResetPassword.objects.get(token=token)
                print(reset_password)
                email = reset_password.email
                created_at = reset_password.created_at
                if (datetime.now(timezone.utc) - created_at).total_seconds() < TOKEN_LIFETIME:
                    user = User.objects.get(email=email)
                    user.set_password(new_password)
                    user.save()
                    user_serializer = UserSerializer(user)
                    return Response(user_serializer.data, status=200)
                else:
                    reset_password.delete()
                    return Response({'message': 'Token is expired, please try again!'}, status=400)
            except:
                return Response({'message': 'Not found'}, status=404)
        else:
            return Response({'message': 'Passwords are not same'}, status=400)


