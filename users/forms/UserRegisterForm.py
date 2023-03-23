from django import forms


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
        max_length=150
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
