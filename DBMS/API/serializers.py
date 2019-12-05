from rest_framework import serializers

from .models import Songs

class SongSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Songs
        fields = ('name', 'writer', 'genre')