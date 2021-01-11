from django.views.generic import ListView, DetailView, CreateView

from notes.models import Note


class HomeView(ListView):
    model = Note
    template_name = 'notes/home.html'


class NoteView(DetailView):
    model = Note
    template_name = 'notes/note_view.html'


class AddNote(CreateView):
    model = Note
    template_name = 'notes/add_note.html'
    fields = '__all__'
