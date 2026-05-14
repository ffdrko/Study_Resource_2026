from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'preferred_language', 'is_nrb', 'country_of_residence', 'currency_preference')
        read_only_fields = ('id',)

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'preferred_language', 'is_nrb', 'country_of_residence', 'currency_preference')

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password'],
            preferred_language=validated_data.get('preferred_language', 'en'),
            is_nrb=validated_data.get('is_nrb', False),
            country_of_residence=validated_data.get('country_of_residence', ''),
            currency_preference=validated_data.get('currency_preference', 'BDT')
        )
        return user
