from django import forms
from core.models import Collaborator

class RegisterCollaboratorForm(forms.ModelForm):
    photo = forms.FileField(required=True)
    class Meta:
        model = Collaborator
        fields = [
            'name',
            'edv',
            'city',
            'treatment_name',
            'photo',
        ]

