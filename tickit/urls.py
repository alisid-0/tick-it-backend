from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.VenueList.as_view(), name='venue-list'),
    path('venues/<int:pk>', views.VenueDetail.as_view(), name='venue-detail'),
    path('events/', views.EventList.as_view(), name='event-list'),
    path('events/<int:pk>', views.EventDetail.as_view(), name='event-detail'),
]