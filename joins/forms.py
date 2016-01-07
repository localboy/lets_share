from django import forms
from django.forms import ModelForm
from .models import Join

#Django regular form
class EmailForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()

#Model form
class JoinForm(ModelForm):
    class Meta:
        model = Join
        fields = ['email']
