from rest_framework import serializers 
from .models import Pessoa 

  
class PessoaSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Pessoa 
        fields = ('uuid', 'email','name')
        depth = 1

    # def get_serializer_context(self):
    #     return {
    #         'answerable': 1
    #         'installation_location': installation_location
    #         }   
     