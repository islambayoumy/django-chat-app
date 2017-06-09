from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
        
        self.fields['first_name'].label = "Display_name"

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'password1', 
            'password2'
        )

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']

        if commit:
            user.save()
            
        return user
