from rest_framework import serializers
from django.contrib.auth import get_user_model,authenticate
from django.core.validators import RegexValidator

User=get_user_model()
password_rules = RegexValidator(
    regex=r'^(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*])',
    message="Password must contain at least one uppercase letter, one number, and one special character."
)
class RegistrationSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True,validators=[password_rules])
    class Meta:
        model=User
        fields=['id','username','first_name','last_name','username','email','password']

    def create(self, validated_data):
        user=super(RegistrationSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class LoginSerializer(serializers.Serializer):
    username=serializers.CharField(write_only=True)
    password=serializers.CharField(validators=[password_rules])

    def validate(self, data):
        user=authenticate(username=data['username'],password=data['password'])
        if not user:
            raise serializers.ValidationError("Invalid Credential")
        data['user']=user
        return data