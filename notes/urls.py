from django.urls import path

from .views import HomeView, NoteView, AddNote

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('note/<int:pk>', NoteView.as_view(), name="note_view"),
    path('add_note', AddNote.as_view(), name="add_note"),
]
