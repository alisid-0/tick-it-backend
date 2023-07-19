from rest_framework import serializers
from .models import Venue, Event

class VenueSerializer(serializers.HyperlinkedModelSerializer):
    events = serializers.HyperlinkedRelatedField(
        view_name='event-detail',
        many = True,
        read_only = True
    )
    venue_url = serializers.ModelSerializer.serializer_url_field(
        view_name='venue-detail'
    )
    class Meta:
        model = Venue
        fields = [
            'id', 'venue_url', 'name', 'address', 'city', 'state', 'country', 'capacity', 'website', 'events'
        ]

class EventSerializer(serializers.HyperlinkedModelSerializer):
    venue = serializers.HyperlinkedRelatedField(
        view_name='venue-detail',
        read_only = True
    )
    class Meta:
        model = Event
        fields = ['id', 'description', 'date', 'start_time', 'end_time', 'venue']
