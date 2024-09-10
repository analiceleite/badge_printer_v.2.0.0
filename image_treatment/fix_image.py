from PIL import Image
from rembg import remove
import cv2, numpy as np, os

def convert_to_png(image_path):
    image = Image.open(image_path)
    png_path = os.path.splitext(image_path)[0] + ".png"
    image.save(png_path, "PNG")
    if not image_path.lower().endswith(".png"):
        os.remove(image_path)
    return png_path
    

def detect_and_crop_face(photo_path, save_path_cropped_photo):
    photo_name = os.path.basename(photo_path)
    save_path_cropped_photo = os.path.join(save_path_cropped_photo, photo_name)
    try:
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        image = cv2.imread(photo_path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5, minSize=(30, 30))
        #Verificar o que fazer caso não encontre rosto
        # if len(faces) == 0:
            # return Image.open(photo_path)
        # Assume que o primeiro rosto detectado é o principal
        x, y, w, h = faces[0]
        
        nova_altura = int(h * 1.7)
        nova_largura = int(w * 1.4)
        novo_y = max(y - ((nova_altura - h) // 2), 0)
        novo_x = max(x - ((nova_largura - w) // 2), 0)
        
        nova_altura = min(nova_altura, image.shape[0] - novo_y)
        nova_largura = min(nova_largura, image.shape[1] - novo_x)
        
        roi = image[novo_y:novo_y + nova_altura, novo_x:novo_x + nova_largura]
        # Recortar a região do rosto
        # cropped_face = image[y:y + h, x:x + w]
        # cropped_face_image = Image.fromarray(cv2.cvtColor(cropped_face, cv2.COLOR_BGR2RGB))
        cropped_face_image = Image.fromarray(cv2.cvtColor(roi, cv2.COLOR_BGR2RGB))
        cropped_face_image.save(save_path_cropped_photo)
        return save_path_cropped_photo
    except Exception as e:
        print(f"Erro em detect_and_crop_face: {e}")

def fix_image(photo_path, save_path_cropped_photo, final_path):
    cropped_image_path = detect_and_crop_face(photo_path, save_path_cropped_photo)
    photo_name = os.path.basename(cropped_image_path)
    final_path = os.path.join(final_path, photo_name)
    remove_background_and_resize(cropped_image_path, final_path)


def remove_background_and_resize(photo_path, save_path):
    try:
        with Image.open(photo_path) as image:
            image_no_background = remove(image)
            resized_image = image_no_background.resize((354,500), Image.LANCZOS)
            resized_image.save(save_path)
            
    except Exception as e:
        print(f"Houve um erro ao remover o fundo da foto: {e}")
        pass