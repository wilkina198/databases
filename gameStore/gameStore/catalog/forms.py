from django import forms
from .models import Motions, Events, Absences, Brothers

class MotionsForm(forms.ModelForm):
    class Meta:
        model = Motions
        fields = ['brother', 'type', 'summary']

class EventsForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ['name', 'date', 'location']

class AbsencesForm(forms.ModelForm):
    class Meta:
        model = Absences
        fields = ['brother', 'event', 'late']
