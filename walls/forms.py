from django import forms
from .models import Following


class FollowingForm(forms.ModelForm):
    class Meta:
        model = Following
        fields = ['target', 'follower']