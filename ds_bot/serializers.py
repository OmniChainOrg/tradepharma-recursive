from rest_framework import serializers
from .models import Match, Offer, Demand

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ['id', 'offer', 'demand', 'matched_at', 'status']
