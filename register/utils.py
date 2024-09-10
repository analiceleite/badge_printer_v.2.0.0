from commons.views import create_path
from django.conf import settings
import os

def create_binary_photo(photo_path):
    with open(photo_path, "rb") as file:
        return file.read()
                    
def mount_collaborator_data(photo_path):
    basename = os.path.basename(photo_path)
    photo_name = f"collaborator_photos/{basename}"
    return {
                "photo_path": photo_path,
                "photo_name": photo_name
            }
    
def save_temp_file(file, edv):
    temp_path = os.path.join(settings.MEDIA_ROOT, "temp_extract")
    create_path(temp_path)
    base_name, ext = os.path.splitext(file.name)
    temp_file_name = f"{edv}{ext}"
    temp_path = os.path.join(temp_path, temp_file_name)
    with open(temp_path, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    return temp_path