from django import forms

class UserForm(forms.Form):
    name = forms.CharField(label='Name of client')
    age = forms.IntegerField(label='Age of client')
