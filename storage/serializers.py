from rest_framework import serializers
from .models import user, call

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = '__all__'

class CallSerializer(serializers.ModelSerializer):
    class Meta:
        model = call
        fields = '__all__'
