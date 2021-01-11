from django.views.generic import ListView, DetailView, CreateView, UpdateView

from notes.forms import NoteForm
from notes.models import Note


class HomeView(ListView):
    model = Note
    template_name = 'notes/home.html'


class NoteView(DetailView):
    model = Note
    template_name = 'notes/note_view.html'


class AddNote(CreateView):
    model = Note
    form_class = NoteForm
    template_name = 'notes/add_note.html'


class UpdateNote(UpdateView):
    model = Note
    form_class = NoteForm
    template_name = 'notes/update_note.html'
