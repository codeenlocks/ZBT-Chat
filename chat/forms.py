from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Room

class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'slug']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom du salon (ex: Projet Python)'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Identifiant unique (ex: projet-python)'}),
        }

def clean_slug(self):
    slug = self.cleaned_data['slug']
    if Room.objects.filter(slug=slug).exists():
        raise forms.ValidationError("Ce slug existe déjà. Choisissez un autre identifiant unique.")
    return slug