from .utils import generate_temp_photo, get_priority_name
from django.conf import settings
from django.contrib.staticfiles.finders import find
from django.template.loader import render_to_string
from io import BytesIO
from PyPDF2 import PdfMerger
import os, pdfkit

def generate_pdf(selected_collaborators):
    merger = PdfMerger()

    for collaborator in selected_collaborators:
        logo_bp = find("assets/badge_images/logo_bp.svg")
        css  = find("style/badge_css/cracha.css")
        temp_photo_path = generate_temp_photo(collaborator.photo)
        
        name_info = get_priority_name(collaborator)
        
        context = {
            "css": css,
            "collaborator": collaborator,
            "photo_path": temp_photo_path,
            "logo_bp": logo_bp,
            **name_info
        }
        
        html_content = render_to_string("cracha.html", context)
        options = {
            "page-width": "54mm",
            "page-height": "86mm",
            "margin-top": "0",
            "margin-right": "0",
            "margin-bottom": "0",
            "margin-left": "0",
            "enable-local-file-access": "",
            "disable-smart-shrinking": "",
        }

        wkhtmltopdf_path = os.path.join(settings.BASE_DIR, "venv", "bin", "wkhtmltopdf.exe")
        config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path)

        try:
            pdf_bytes = pdfkit.from_string(html_content, False, options=options, configuration=config)
        except Exception as e:
            print(f"Erro ao gerar PDF: {e}")
        pdf_file = BytesIO(pdf_bytes)
        pdf_file.seek(0)
        merger.append(pdf_file)
    output = BytesIO()
    merger.write(output)
    merger.close()
    output.seek(0)
    return output            