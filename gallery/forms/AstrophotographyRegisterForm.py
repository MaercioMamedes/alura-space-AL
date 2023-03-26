from django import forms
from gallery.models import Astrophotography


class AstrophotographyRegisterForm(forms.ModelForm):
    class Meta:
        model = Astrophotography
        exclude = ['published', 'registered_by']

        widgets = {
            'image': forms.FileInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'image_source': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'title': forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),

            'date_image': forms.DateInput(
                attrs={
                    'type':'date',
                    'class':'form-control'
                }
            ),

            'description': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),

            'category': forms.Select(
                attrs={
                    'class':'form-control'
                }
            ),
        
        }

    def clean(self):
        return super().clean()