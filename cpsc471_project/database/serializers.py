from rest_framework import serializers
from .models2 import DatabaseClub

class ClubSerializer(serializers.ModelSerializer):

    class Meta:
        model = DatabaseClub
        fields = ['name', 'city']