from commons.views import process_photo
import concurrent.futures

def process_photos_async(photos_to_fix):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(process_photo, photos_to_fix)