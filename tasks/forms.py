from django import forms # type: ignore
from .models import Task

class taskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('tittle', 'done')