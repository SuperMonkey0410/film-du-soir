from django.forms import forms
from django.forms import ModelForm
from django.forms.models import ModelForm
from .models import Feedback


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ('text', 'name', 'email',)
