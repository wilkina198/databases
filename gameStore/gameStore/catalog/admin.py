from django.contrib import admin

# Register your models here.
from catalog.models import Events, Absences, Brothers, Motions

admin.site.register(Events)
admin.site.register(Absences)
admin.site.register(Brothers)
admin.site.register(Motions)

'''@admin.register(BoardGame)
class BoardGameAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'price')
    fields = [('name', 'company'), ('genre', 'date_released'), 'summary', ('price', 'players')]

@admin.register(VideoGame)
class VideoGameAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'price')
    fields = [('name', 'console'), ('company', 'genre', 'date_released'), 'summary', 'price', ('singleplayer', 'multiplayer')]
'''
