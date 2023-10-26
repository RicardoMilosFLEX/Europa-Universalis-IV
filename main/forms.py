from .models import Notes
from django.forms import ModelForm, TextInput, Textarea
class Notesform(ModelForm):
    class Meta:
        model = Notes
        fields = ["title", "notes"]
        widgets = {"title": TextInput(attrs={'class': 'form-control','placeholder':'Введите название'}),
                   "notes": Textarea(attrs={'class':'form-control', 'placeholder':'Введите текст вашей статьи'})}