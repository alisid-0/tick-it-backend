from rest_framework import serializers
from .models import Venue, Event


class EventSerializer(serializers.HyperlinkedModelSerializer):
    venue = serializers.HyperlinkedRelatedField(
        view_name='venue-detail',
        read_only=True
    )
    venue_info = serializers.StringRelatedField(
        source = 'venue'
    )
    event_url = serializers.ModelSerializer.serializer_url_field(
        view_name='event-detail'
    )

    class Meta:
        model = Event
        fields = [
            'id', 'event_url', 'description', 'date', 'start_time', 'end_time', 'picture_link', 'venue', 'venue_info'
        ]


class VenueSerializer(serializers.HyperlinkedModelSerializer):
    events = EventSerializer(
        many=True,
        read_only=True
    )
    venue_url = serializers.ModelSerializer.serializer_url_field(
        view_name='venue-detail'
    )

    class Meta:
        model = Venue
        fields = [
            'id', 'venue_url', 'name', 'address', 'city', 'state', 'country', 'capacity', 'website', 'picture_link', 'events'
        ]
