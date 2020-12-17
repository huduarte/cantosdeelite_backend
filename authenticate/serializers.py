from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, get_user_model
User = get_user_model()

from porter.models import Porter
from person.models import Person

class GroupSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Group
        fields = ('name',)

class CustomUserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True, required=False)
    email = serializers.EmailField(
        required=True
    )
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'password', 'groups',)  
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)  # as long as the fields are the same, we can just use this
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        # token['email'] = user.email
        token['name'] = user.first_name
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['token'] = str(refresh.access_token)
        data['user'] = CustomUserSerializer(self.user).data

        porter = Porter.objects.filter(user = self.user).first()
        if porter:
            data['installation_location'] = porter.installation_location.name
        else:
            data['installation_location'] = 'None'

        person = Person.objects.filter(user=self.user).first()
        if person and not person.has_app:
            person.has_app = True
            person.save()

        return data

from django.contrib.auth.password_validation import validate_password

class ChangePasswordSerializer(serializers.Serializer):
    """
    Serializer for password change endpoint.
    """
    email = serializers.EmailField(required=True)
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    password_confirmation = serializers.CharField(required=True)

    def validate_new_password(self, value):
        validate_password(value)
        return value