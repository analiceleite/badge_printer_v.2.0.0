from core.models import Collaborator
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
import os, tempfile

def absolute_photo_path(collaborator):
    absolute_photo_path = os.path.join(settings.BASE_DIR, settings.MEDIA_ROOT, "collaborator_photos", collaborator.photo.path)
    return absolute_photo_path

def generate_temp_photo(photo):
            with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_photo_file:
                temp_photo_file.write(photo)
                return temp_photo_file.name        

def get_collaborator_data(request, collaborator_id):
    if request.method == "GET":
        collaborator = get_object_or_404(Collaborator, id=collaborator_id)
        data = {
            "id": collaborator.pk,
            "edv": collaborator.edv,
            "name": collaborator.name,
            "treatment_name": collaborator.treatment_name,
            "city": collaborator.city,
        }
        return JsonResponse(data)

def get_collaborator_photo(request, edv):
    collaborator = get_object_or_404(Collaborator, edv=edv)
    return HttpResponse(collaborator.photo, content_type='image/png')

def get_priority_name(collaborator):
    first_name = collaborator.name.split()[0]
    treatment_name = collaborator.treatment_name
    if treatment_name == first_name:
        name_info = mount_display_name(complete_name=collaborator.name)
    else:
        name_info = mount_display_name(complete_name=collaborator.treatment_name)
    return name_info
    
def mount_display_name(complete_name):
    name_length = len(complete_name)
    display_complete_name = complete_name
    display_first_name = complete_name.split()[0]
    return{"name_length": name_length,
            "display_complete_name": display_complete_name,
            "display_first_name": display_first_name}