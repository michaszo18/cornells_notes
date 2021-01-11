from django.forms import TextInput, ModelForm, Textarea, Select

from notes.models import Note


class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'category', 'author', 'body')

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control'
            }),
            'category': TextInput(attrs={
                'class': 'form-control'
            }),
            'author': Select(attrs={
                'class': 'form-control'
            }),
            'body': Textarea(attrs={
                'class': 'form-control'
            }),
        }
