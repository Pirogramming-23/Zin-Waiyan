# apps.posts.forms.py
from django import forms
from .models import Idea

class IdeaForm(forms.ModelForm):
    class Meta:
        model = Idea
        exclude = ['created_at', 'updated_at']