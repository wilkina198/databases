from django.db import models
import uuid
from django.urls import reverse
from django.contrib.auth.models import User

# Models
from django.urls import reverse
class Events(models.Model):
    """Model representing a Event"""
    name = models.CharField(max_length=50, help_text='Name of the event')
    date = models.DateTimeField(null=True, blank=True)
    location = models.TextField(null=True, blank=True, default='TBD')

    class Meta:
        ordering = ['date']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a detail record for this event."""
        return reverse('Event detail', args=[str(self.name)])

class Absences(models.Model):
    """Model representing an Absence"""
    brother = models.ForeignKey('Brothers', on_delete=models.SET_NULL, null=True)
    event = models.ForeignKey('Events', on_delete=models.SET_NULL, null=True)
    late = models.BooleanField(default=False)

    def __str__(self):
        return self.name

from django.urls import reverse
class Brothers(models.Model):
    """Model representing a brother"""
    name = models.CharField(max_length=200, help_text='Enter the name of a brother', primary_key=True)
    STATUS = (('C', 'Collegiate'),
              ('A', 'Alumni'),
              ('S', 'Suspended'),
              )
    status = models.CharField(max_length=1,choices=STATUS, blank=True, default='C')
    #absences = models.ManyToManyField('Absences')
    phone_number = models.CharField(max_length=11, blank=True)
    email = models.EmailField()
    """Position"""

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a detail record for this brother."""
        return reverse('brother detail', args=[str(self.name)])

from django.urls import reverse
class Motions(models.Model):
    """Model representing a Motion"""
    brother = models.ForeignKey('Brothers', on_delete=models.SET_NULL, null=True)
    TYPE = (('M', 'Motion'),
            ('D', 'Open Discussion'),
            ('A', 'Announcement'),
            )
    type = models.CharField(max_length=1,choices=TYPE, blank=True, default='M')
    summary = models.TextField(help_text='Your motion/open discussion/announcement')

    class Meta:
        ordering = ['type']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a detail record for this Motion."""
        return reverse('motion detail', args=[str(self.id)])
