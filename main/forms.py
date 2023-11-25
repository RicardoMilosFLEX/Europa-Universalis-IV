from .models import Notes, User
from django.forms import ModelForm, TextInput, Textarea
from django import forms

class Notesform(ModelForm):
    class Meta:
        model = Notes
        fields = ["title", "notes"]
        widgets = {"title": TextInput(attrs={'class': 'form-control','placeholder':'Введите название'}),
                   "notes": Textarea(attrs={'class':'form-control', 'placeholder':'Введите текст вашей статьи'})}

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['login', 'email', 'password']
        widgets = {'login': Textarea(attrs={'placeholder': 'Введите логин'}),
                   'email': Textarea(attrs={'placeholder': 'Введите email'}),
                   'password': forms.PasswordInput()}