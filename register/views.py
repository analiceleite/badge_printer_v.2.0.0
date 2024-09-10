from .forms import RegisterCollaboratorForm
from .utils import create_binary_photo, mount_collaborator_data, save_temp_file
from commons.views import (collaborator_exists,
                           mount_error_response,mount_success_response,
                           process_photo,
                           remove_especific_path, remove_unnecessary_paths,
                           translate_city)
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from image_treatment.fix_image import convert_to_png

@require_http_methods(["GET","POST"])
def render_register(request):
    if request.method == "POST":
        form = RegisterCollaboratorForm(request.POST, request.FILES)
        if form.is_valid():
            if collaborator_exists(form.cleaned_data["edv"]):
                return mount_error_response(message="The collaborator is already registered", status_code=409)
            try:
                temp_photo_path = save_temp_file(form.cleaned_data["photo"], form.cleaned_data["edv"])
                png_path = convert_to_png(temp_photo_path)
                collaborator_data = mount_collaborator_data(png_path)
                process_photo(collaborator_data)
                processed_photo_path = f"media/collaborator_photos/{form.cleaned_data["edv"]}.png"
                binary_photo = create_binary_photo(processed_photo_path)
                form.cleaned_data["city"] = translate_city(form.cleaned_data["city"])
                form.instance.photo = binary_photo
                form.save()
                return mount_success_response(message="The collaborator was registered successfully", status_code=201)
            except Exception as e:
                print(e)
                media_path = png_path.replace("temp_extract", "collaborator_photos")
                remove_especific_path(media_path)
                return mount_error_response(message="An error occurred while registering the collaborator")
            finally:
                remove_unnecessary_paths()
                pass
    return render(request, 'register.html')
