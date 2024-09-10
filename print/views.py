from .generate_pdf import generate_pdf
from commons.views import translate_city
from core.models import Collaborator
from django.http import FileResponse
from django.shortcuts import get_object_or_404, render
from commons.views import mount_error_response, mount_success_response, process_photo
from image_treatment.fix_image import convert_to_png
from register.forms import RegisterCollaboratorForm
from register.utils import create_binary_photo, mount_collaborator_data, save_temp_file


def render_print(request):
    collaborators = Collaborator.objects.filter(active=True)
    return render(request, "print.html", {"collaborators": collaborators})

def print_selected_collaborators(request):
    if request.method == "POST":
        collaborators_id = request.POST.getlist("selected_badges")
        selected_collaborators = Collaborator.objects.filter(id__in=collaborators_id)
        try:
            pdf = generate_pdf(selected_collaborators)
            response = FileResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename="crachas.pdf"'
            return response
        except Exception as e:
            print(e)
            return mount_error_response(message="An error occurred while generating the badge")
               
def edit_collaborator(request):    
    if request.method == "POST":
        collaborator_id = request.POST.get('collaborator_id')
        collaborator = get_object_or_404(Collaborator, id=collaborator_id)
        form = RegisterCollaboratorForm(request.POST, request.FILES, instance=collaborator)
        if form.is_valid():
            if 'photo' in request.FILES:
                try:
                    temp_photo_path = save_temp_file(form.cleaned_data["photo"], form.cleaned_data["edv"])
                    png_path = convert_to_png(temp_photo_path)
                    collaborator_data = mount_collaborator_data(png_path)
                    process_photo(collaborator_data)
                    processed_photo_path = f"media/collaborator_photos/{form.cleaned_data["edv"]}.png"
                    binary_photo = create_binary_photo(processed_photo_path)
                except:
                    return mount_error_response(message="An error occurred while editing the collaborator")
                form.instance.photo = binary_photo
            form.cleaned_data["city"] = translate_city(form.cleaned_data["city"])
            form.save()
            return mount_success_response(message="Employee successfully edited")

def delete_collaborator(request):
    if request.method == 'POST':
        collaborator_id = request.POST.get('collaborator_id')
        try:
            collaborator = get_object_or_404(Collaborator, id=collaborator_id)
            collaborator.active = False
            collaborator.save()
            return mount_success_response(message="Employee successfully deleted.")
        except:
            return mount_error_response(message="Collaborator was not found", status_code=404)