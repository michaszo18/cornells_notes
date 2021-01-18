from django.urls import path

from .views import HomeView, NoteView, AddNote, UpdateNote, DeleteNote, AddCategoryView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('note/<int:pk>', NoteView.as_view(), name="note_view"),
    path('add_note', AddNote.as_view(), name="add_note"),
    path('note/update/<int:pk>', UpdateNote.as_view(), name="update_note"),
    path('note/delete/<int:pk>', DeleteNote.as_view(), name="delete_note"),
    path('add_category', AddCategoryView.as_view(), name="add_category"),
]
