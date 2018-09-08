from django import forms
from .models import Articles
from django.core.exceptions import ValidationError

class PostForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'post', 'author']
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'post' : forms.Textarea(attrs={'class':'form-control'}),
        }
