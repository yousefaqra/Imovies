from django.contrib import admin
from .models import Genre, Movie


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class MovieAdmin(admin.ModelAdmin):
    exclude = ('date_created', )
    list_display = ('title', 'relase_year',
                    'number_in_stock', 'genre')


admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
