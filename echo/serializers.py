
from rest_framework import serializers
from .models import *


class OsTyperSerializer(serializers.ModelSerializer):
  class Meta:
      model=OsTyper
      fields='__all__'


class OsCommandSerializer(serializers.ModelSerializer):
  class Meta:
      model=OsCommand
      fields='__all__'


class ParameterSerializer(serializers.ModelSerializer):
  class Meta:
      model=Parameter
      fields='__all__'


class MathCommandSerializer(serializers.ModelSerializer):
  class Meta:
      model=MathCommand
      fields='__all__'


# serializer worked sucessfully 