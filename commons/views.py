from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from core.models import Collaborator
from image_treatment.fix_image import fix_image
import os, shutil

    
CITY_SIGLAS = {
    "Joinville" : "JvL",
    "Curitiba" : "CtB",
    "Campinas" : "CaP",
}

def collaborator_exists(edv):
    try:
        get_object_or_404(Collaborator, edv=edv)
        print("Encontrou coll")
        return True
    except:
        return False

def create_path(path):
    try:
        if not os.path.exists(path):
            os.makedirs(path)
    except:
        # Houve um erro ao criar os caminhos de extração
        pass

def mount_error_response(css_class=".message--error" ,data=None, message=None, status="error", status_code=500, **kwargs):
    response = {
        "status": status,
        "message": message,
        "css_class": css_class,
        "data": data
    }
    # response.update(kwargs)
    return JsonResponse(response, status=status_code)

def mount_success_response(css_class=".message--success" ,data=None, message=None, status="success", status_code=200, **kwargs):
    response = {
        "status": status,
        "message": message,
        "css_class": css_class,
        "data": data
    }
    # response.update(kwargs)
    return JsonResponse(response, status=status_code)

def process_photo(collaborator_data):
    photo_path = collaborator_data["photo_path"]
    save_path_cropped_photo = os.path.join(settings.MEDIA_ROOT, "cropped_photos")
    final_path = os.path.join(settings.MEDIA_ROOT, "collaborator_photos")
    create_path(save_path_cropped_photo)
    create_path(final_path)
    fix_image(photo_path, save_path_cropped_photo, final_path)

def remove_especific_path(path):
    try:
        os.remove(path)
    except Exception as e:
        print(f"Erro ao excluir foto: {e}")
    
def remove_unnecessary_paths():
    temp_extract_path = os.path.join(settings.MEDIA_ROOT, "temp_extract")
    cropped_photos_path = os.path.join(settings.MEDIA_ROOT, "cropped_photos")
    media_path = os.path.join(settings.MEDIA_ROOT)
    shutil.rmtree(temp_extract_path)
    shutil.rmtree(cropped_photos_path)
    shutil.rmtree(media_path)

def translate_city(city):
    return CITY_SIGLAS.get(city)