from django.forms import TextInput, ModelForm, Textarea, Select

from notes.models import Note, Category

choices = Category.objects.all().values_list('name', 'name')


class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'category', 'questions', 'body', 'cues', 'summary')

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control'
            }),
            'category': Select(
                choices=choices,
                attrs={
                    'class': 'form-control',
                }),
            'questions': Textarea(attrs={
                'class': 'form-control',
                'style': "height: 180px"
            }),
            'body': Textarea(attrs={
                'class': 'form-control',
                'style': "height: 500px"
            }),
            'cues': Textarea(attrs={
                'class': 'form-control',
                'style': "height: 500px"
            }),
            'summary': Textarea(attrs={
                'class': 'form-control',
                'style': "height: 250px"
            }),
        }
