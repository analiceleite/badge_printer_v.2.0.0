from image_treatment.fix_image import convert_to_png
from commons.views import collaborator_exists, create_path, translate_city
from core.models import Collaborator
from .tasks import process_photos_async
from django.conf import settings
from django.http import JsonResponse
import concurrent.futures, os, pandas as pd, zipfile



def collect_photo_path():
    temp_photos_path = os.path.abspath(os.path.join("media", "temp_extract"))
    file_names = []
    for file_name in os.listdir(temp_photos_path):
        full_path = os.path.join(temp_photos_path, file_name)
        file_names.append(full_path)
    return file_names

def create_collaborators_to_create_list(collaborators_data, processed_photos):
        collaborators_to_create = [
            Collaborator(
                name=collaborator["name"],
                edv=collaborator["edv"],
                treatment_name=collaborator["treatment_name"],
                city=collaborator["city"],
                photo=processed_photos[i]
            )
            for i, collaborator in enumerate(collaborators_data)
        ]
        return collaborators_to_create
    
def create_binary_photo_list(collaborators_data):
    processed_photos = []
    for collaborator in collaborators_data:
        photo_path = f"media/collaborator_photos/{collaborator["edv"]}.png"
        with open(photo_path, "rb") as file:
            processed_photos.append(file.read())
    return processed_photos

def data_frame_iterate(data_frame, temp_photos_path):
    photos_to_fix = []
    collaborators_data = []
    for index, row in data_frame.iterrows():
        edv = row["edv"]
        if not collaborator_exists(edv):
            complete_name = row["complete_name"]
            city = row["city"]
            treatment_name = complete_name.split()[0]
            collaborator_data = search_collaborator_photo(edv, complete_name, city, treatment_name, temp_photos_path)
            photos_to_fix.append(collaborator_data)
            collaborators_data.append({
                "name": complete_name,
                "edv": edv,
                "treatment_name": treatment_name,
                "city": collaborator_data["city"],
            })
    process_photos_async(photos_to_fix)
    processed_photos = create_binary_photo_list(collaborators_data)
    collaborators_to_create = create_collaborators_to_create_list(collaborators_data, processed_photos)
    if collaborators_to_create:
        Collaborator.objects.bulk_create(collaborators_to_create)

def extract_zip_file(archive, destiny_path):
    try:
        with zipfile.ZipFile(archive, "r") as zip_ref:
            zip_ref.extractall(destiny_path)
    except:
        return JsonResponse(
            {
                "status": "error",
                "message": "Houve um error ao extrair a pasta de fotos",
            },
            status=500,
        )


def move_image(image_path, destiny):
    destiny_path = os.path.join(destiny, os.path.basename(image_path))
    if not os.path.exists(destiny_path):
        os.rename(image_path, destiny_path)
        
def process_path(temp_extract_path):
    file_paths = []
    for root, dirs, files in os.walk(temp_extract_path):
        for file in files:
            full_path_archive = os.path.join(root, file)
            if file.lower().endswith(".zip"):
                extract_zip_file(full_path_archive, root)
                os.remove(full_path_archive)
            elif not file.lower().endswith((".png")):
                file_paths.append(full_path_archive) 
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(convert_to_png, file_paths)

def process_spreadsheet(xlsx_file):
    try:
        specific_columns = ["Nº pess.", "Nome completo", "Área de recursos humanos"]
        data_frame = pd.read_excel(xlsx_file, usecols=specific_columns)
        data_frame.columns = ["edv", "complete_name", "city"]
    except Exception as e:
        return JsonResponse(
            {"status": "error", "message": "Houve um erro ao processar a planilha"},
            status=500,
        )
    return data_frame


def process_zip_file(zip_file):
    temp_extract_path = os.path.join(settings.MEDIA_ROOT, "temp_extract")
    create_path(temp_extract_path)
    extract_zip_file(zip_file, temp_extract_path)
    process_path(temp_extract_path)


def relate_collaborators(data_frame, temp_photos_path):
    data_frame_iterate(data_frame, temp_photos_path)
    
def search_collaborator_photo(edv, complete_name, city, treatment_name, temp_photos_path):
    for photo_path in temp_photos_path:
        basename = os.path.basename(photo_path)
        photo_name = f"collaborator_photos/{basename}"
        edv_str = str(edv)
        if edv_str in photo_name:
            city = translate_city(city)
            return {
                "photo_path": photo_path,
                "photo_name": photo_name,
                "complete_name": complete_name,
                "treatment_name": treatment_name,
                "edv": edv,
                "city": city,
            }