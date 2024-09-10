from .forms import UploadFileForm
from .utils import collect_photo_path, process_spreadsheet, process_zip_file, relate_collaborators
from commons.views import mount_error_response, mount_success_response, remove_unnecessary_paths
from django.shortcuts import render

def import_files(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                xlsx_file = form.cleaned_data["spreadsheet"]
                zip_file = form.cleaned_data["picture"]
                data_frame = process_spreadsheet(xlsx_file)
                process_zip_file(zip_file)
                temp_photos_path = collect_photo_path()
                relate_collaborators(data_frame, temp_photos_path)
                try:
                    remove_unnecessary_paths()
                except:
                    #Sem caminhos para remover
                    pass
                return mount_success_response(message="All employees were successfully registered.", status_code=201)
            except:
                return mount_error_response(message="An error occurred while registering the employees")
                
    else:
        form = UploadFileForm()
    return render(request, 'import.html', {"form":form})
