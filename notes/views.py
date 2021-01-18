from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from notes.forms import NoteForm
from notes.models import Note, Category


class HomeView(ListView):
    model = Note
    template_name = 'notes/home.html'
    ordering = ['-created_at']


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


class DeleteNote(DeleteView):
    model = Note
    template_name = 'notes/delete_note.html'
    success_url = reverse_lazy('home')


class AddCategoryView(CreateView):
    model = Category
    template_name = 'categories/add_category.html'
    fields = '__all__'
