from django import forms
from django.utils import timezone

from .models import Title, Entry


class TopicForm(forms.ModelForm):
    date_added = forms.DateTimeField(widget=forms.widgets.DateInput(attrs={'type': 'date'}),
                                     required=False, initial=timezone.now)

    class Meta:
        model = Title
        fields = ['title', "preacher", "verses", "date_added"]
        labels = {'text': ''}
        widgets = {'verses': forms.Textarea(attrs={'cols': 80})}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text', 'verse']
        labels = {'text': 'Entry:'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}