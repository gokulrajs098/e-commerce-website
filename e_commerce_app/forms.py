from django import forms

class SignupForm(forms.Form):
    firstname = forms.CharField(max_length=100, required=True)
    lastname = forms.CharField(max_length=100, required=True)
    username = forms.CharField(max_length=100, required=True)
    email = forms.EmailField( widget=forms.EmailInput)
    password = forms.CharField(required=True)

    def clean_username(self):
        name = self.cleaned_data.get('username')
        if len(name) < 5:
            raise forms.ValidationError('Username must be more than 5 characters long')
        return name
    
class LoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)
