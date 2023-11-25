from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import NewUser
class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text = 'Required. Enter a valid email address.')
    class Meta:
        model = NewUser
        fields = ('username', 'email', 'password1', 'password2', )

