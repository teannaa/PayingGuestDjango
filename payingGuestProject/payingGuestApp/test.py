class SignupForm(forms.Form):
    firstName=forms.CharField(widget=forms.TextInput(
        attrs={
            'id':'firstname',
            'class': 'form-control',
            'name': 'text',
            'placeholder': '',
            'required':''}
    ))
    lastName = forms.CharField(widget=forms.TextInput(
        attrs={
            'id': 'secondname',
            'class': 'form-control',
            'name': 'text',
            'placeholder': '',
            'required': ''
         }
    ))
    email=forms.CharField(widget=forms.TextInput(
        attrs={
            'id': 'email',
            'class': 'form-control',
            'name': 'text',
            'placeholder': '',
            'required': ''
        }
    ))
    password1=forms.CharField(widget=forms.PasswordInput(
        attrs={
            'id': 'password1',
            'class': 'form-control',
            'name': 'text',
            'placeholder': '',
            'required': ''
        }
    ))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'id': 'password2',
            'class': 'form-control',
            'name': 'text',
            'placeholder': '',
            'required': ''
        }
    ))

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(
        attrs={
            'id': 'myCustomId',
            'class': 'myCustomClass',
            'name': 'myCustomName',
            'placeholder': 'myCustomPlaceholder'}
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'id': 'myCustomId',
            'class': 'myCustomClass',
            'name': 'myCustomName',
            'placeholder': 'myCustomPlaceholder'}
    ))
