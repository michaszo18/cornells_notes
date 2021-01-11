from django.urls import path

from .views import HomeView, NoteView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('note/<int:pk>', NoteView.as_view(), name="note"),
]
