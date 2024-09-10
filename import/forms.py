from django import forms

class UploadFileForm(forms.Form):
    spreadsheet = forms.FileField()
    picture = forms.FileField()
    
    def clean_xlsx_file(self):
        xlsx_file = self.cleaned_data['spreadsheet']
        if not xlsx_file.name.endswith('.xlsx'):
            raise forms.ValidationError("O arquivo deve estar no formato XLSX.")
        return xlsx_file

    def clean_zip_file(self):
        zip_file = self.cleaned_data['pictures']
        if not zip_file.name.endswith('.zip'):
            raise forms.ValidationError("O arquivo deve ser uma pasta ZIP.")
        return zip_file
