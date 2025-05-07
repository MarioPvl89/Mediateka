from django import forms
from .models import MediaItem

class MediaItemForm(forms.ModelForm):
    class Meta:
        model = MediaItem
        exclude = ['user', 'added_at']  # или укажи только нужные поля
