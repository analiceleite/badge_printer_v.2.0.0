from django import forms

class EDVForm(forms.Form):
    edv = forms.IntegerField()
    
    def clean_edv(self):
        edv = self.cleaned_data.get('edv')
        if len(str(edv)) != 8:
            raise forms.ValidationError("O EDV deve conter 8 dígitos")
        return edv
    
class TokenForm(forms.Form):
    token = forms.IntegerField()
    
    def clean_token(self):
        token = self.cleaned_data.get('token')
        if len(str(token)) != 5 :
            raise forms.ValidationError("Token inválido")
        return token

class ChangePasswordForm(forms.Form):
    new_password = forms.CharField()
    confirm_password = forms.CharField()
    