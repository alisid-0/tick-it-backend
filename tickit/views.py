from rest_framework import generics
from .models import Venue, Event
from .serializers import VenueSerializer, EventSerializer

class VenueList(generics.ListCreateAPIView):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer

class VenueDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer

class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
