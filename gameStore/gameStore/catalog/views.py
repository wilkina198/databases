from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from catalog.models import Brothers, Absences, Events, Motions

def index(request):
    """View function for home page of site."""

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html')

from django.views import generic


class BrotherListView(LoginRequiredMixin, generic.ListView):
    model = Brothers
    paginate_by = 10

class BrotherDetailView(LoginRequiredMixin, generic.DetailView):
    model = Brothers

class EventsListView(LoginRequiredMixin, generic.ListView):
    model = Events
    paginate_by = 10

class EventsDetailView(LoginRequiredMixin, generic.DetailView):
    model = Events

class AbsencesListView(LoginRequiredMixin, generic.ListView):
    model = Absences
    paginate_by = 10

class MotionsListView(LoginRequiredMixin, generic.ListView):
    model = Motions
    paginate_by = 10

from .forms import EventsForm
def EventsCreate(request):
    form = EventsForm(request.POST or None)
        #if form.is_valid():
    form.save

def MotionsCreate(request):
    form = MotionsForm(request.POST or None)
        #if form.is_valid():
    form.save

def AbsencesCreate(request):
    form = AbsencesForm(request.POST or None)
        #if form.is_valid():
    form.save
