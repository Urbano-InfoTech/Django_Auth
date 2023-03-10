from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers

class ExtendSerializer(RegisterSerializer):
    extend_field = serializers.CharField(write_only=True)