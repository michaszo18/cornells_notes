from django.contrib import admin

from notes.models import Note, Category

admin.site.register(Note)
admin.site.register(Category)
