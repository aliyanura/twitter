from django import forms
from .models import *
from django.core.exceptions import ValidationError


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message',]
        widgets = {
            'message': forms.TextInput(attrs={'class': 'form-control',
                                                'id':"floatingTextarea2",
                                                'placeholder': "Leave a comment here",
                                                'style': "height: 100px"}),
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['message', 'image']
        widgets = {'message': forms.TextInput(attrs={'class': 'form-control',
                                                    'id':"floatingTextarea2",
                                                    'placeholder': "Leave a comment here",
                                                    'style': "height: 100px"}),}

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image',]