from django import forms
from .models import TextNotes


class NewNoteForm(forms.ModelForm):
    # model is associated with textNote models
    # title in fields list inside the meta class is refering to the title in
    # TextNote model
    note = forms.CharField(widget=forms.Textarea(
        attrs={'row': 9, 'placeholder': 'enter your notes here',
               'class': 'form-control'}),
        max_length=10000,
        help_text='Maximum length for this note is 10000'
           )
    title = forms.CharField(widget=forms.TextInput(
         attrs={'class': 'form-control',
                'placeholder': 'title',
                }))

    class Meta:
        model = TextNotes
        fields = ['title', 'note']
