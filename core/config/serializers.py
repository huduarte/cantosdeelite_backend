from rest_framework import serializers 
from core.config.models import Config


class ConfigSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Config
        fields = '__all__'
        depth = 1