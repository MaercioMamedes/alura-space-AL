from django import forms
from users.helpers import Validation


class UserRegisterForm(forms.Form):

    first_name = forms.CharField(
        label='Primeiro nome',
        max_length=50,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )

    )

    last_name = forms.CharField(
        label='Último nome',
        max_length=50,
        required=50,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    username = forms.CharField(
        label='username',
        max_length=20,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    email = forms.EmailField(
        label='Email',
        max_length=150,
        widget=forms.EmailInput(
            attrs={'class':'form-control'}
        )
    )

    password = forms.CharField(
        label='Crie uma senha',
        widget=forms.PasswordInput(
            attrs={'class':'form-control'}
        ),
        required=True
    )

    password_confirm = forms.CharField(
        label='Corfirme sua uma senha',
        widget=forms.PasswordInput(
            attrs={'class':'form-control'}
        ),
        required=True
    )

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        errors_list = {}

        Validation.field_is_alphanumeric(self, first_name, field_name='first_name')
        Validation.field_is_alphanumeric(self, last_name, field_name='last_name')
        Validation.username_exist(self, username)
        Validation.password_validate(self, password, password_confirm)

    
    
