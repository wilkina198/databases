from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('brothers/', views.BrotherListView.as_view(), name='brothers'),
    path('brothers/<str:pk>', views.BrotherDetailView.as_view(), name='brother detail'),

    path('events/', views.EventsListView.as_view(), name='events'),
    #path('events/<int:pk>', views.EventsDetailView.as_view(), name='events detail'),
    path('create_events/', views.EventsCreate, name='create events'),

    path('motions/', views.MotionsListView.as_view(), name='motions'),
    #path('motions/<int:pk>', views.MotionsDetailView.as_view(), name='events detail'),
    path('create_motions/', views.MotionsCreate, name='create motions'),

    path('absences/', views.AbsencesListView.as_view(), name='absences'),
    #path('absences/<int:pk>', views.AbsencesDetailView.as_view(), name='events detail'),
    path('create_absences/', views.AbsencesCreate, name='create absences'),
]
