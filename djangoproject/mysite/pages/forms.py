from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
   email = forms.CharField(max_length = 100,)
   password = forms.CharField()

class Registrationform(UserCreationForm):
    email=forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )

    def save(self, commit=True):
        user = super(Registrationform, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.first_name=self.cleaned_data['first_name']
        user.last_name=self.cleaned_data['last_name']
        user.email=self.cleaned_data['email']
        
        if commit:
            user.save()

        return user