# https://stackoverflow.com/questions/1453488/how-to-markup-form-fields-with-div-class-field-type-in-django/1504903#1504903

from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254,
                            required=True,
                            widget=forms.EmailInput(
                            attrs={'class': 'form-control'}
                           ))


    class Meta(UserCreationForm.Meta) :
        model = User
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }
        fields =  fields = UserCreationForm.Meta.fields + ('email',)
