from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        label='Usuário',
        max_length=20,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: user01',
                }
        )
    )

    password = forms.CharField(
        label='Senha',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite a sua senha'
                }
        )
    )
