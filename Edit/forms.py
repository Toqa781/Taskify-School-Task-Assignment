from django import forms
from tasks.models import (Task, x)


class TaskForm(forms.ModelForm):
    choose = forms.ChoiceField(choices=x, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Task
        fields = ['title', 'teacher', 'choose', 'Description', 'admin']