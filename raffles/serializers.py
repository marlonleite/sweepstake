import random

from rest_framework import serializers


class RaffleSerializer(serializers.Serializer):
    items = serializers.ListField(
        child=serializers.CharField(max_length=100), write_only=True)

    class Meta:
        fields = '__all__'

    def create(self, validated_data):
        return validated_data

    def to_representation(self, instance):
        obj = super().to_representation(instance)

        obj['item'] = random.choice(instance['items'])

        return obj
