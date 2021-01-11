from django.views.generic import ListView, DetailView

from notes.models import Note


class HomeView(ListView):
    model = Note
    template_name = 'notes/home.html'


class NoteView(DetailView):
    model = Note
    template_name = 'notes/note.html'
