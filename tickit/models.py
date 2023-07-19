from django.db import models

# Create your models here.


class Venue(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    capacity = models.IntegerField()
    website = models.CharField(max_length=255)
    picture_link = models.URLField(blank=True, null=True)

    def __str__(self) -> str:
        return str({
            "id":self.id, 
            "name":self.name, 
            "address": self.address,
            "city": self.city,
            "state": self.state,
            "country": self.country,
            "capacity": self.capacity,
            "website": self.website,
            "picture_link": self.picture_link
            })


class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, related_name='events')
    picture_link = models.URLField(blank=True, null=True)
    def __str__(self) -> str:
        return self.name
