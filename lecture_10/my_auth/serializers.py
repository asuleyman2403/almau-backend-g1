from rest_framework import serializers
from my_auth.models import User


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = '__all__'


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(allow_null=False, allow_blank=False)
    new_password = serializers.CharField(allow_null=False, allow_blank=False)


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(allow_null=False, allow_blank=False)


class ResetPasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(min_length=8, max_length=16, allow_null=False, allow_blank=False)
    repeat_password = serializers.CharField(min_length=8, max_length=16, allow_null=False, allow_blank=False)
