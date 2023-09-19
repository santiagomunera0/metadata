from pptx import Presentation
import os

from src.common.common_tools import parameters

def get_propierties(presentation, file):
    file_size_mb = os.path.getsize(file) / (1024 * 1024)
    try:
        metadata = {
            "Titulo": presentation.core_properties.title,
            "Autor": presentation.core_properties.author,
            "Asunto": presentation.core_properties.subject,
            "Palabras_Clave": presentation.core_properties.keywords,
            "File_Size": round(file_size_mb, 2),
            "Fecha_Creacion": presentation.core_properties.created,
            "Fecha_Modificacion": presentation.core_properties.modified,
            "Categorias": presentation.core_properties.category,
            "Comentarios": presentation.core_properties.comments,
            "Numero_Paginas": len(presentation.slides),
        }

        return metadata

    except Exception as e:
        print("Error:", e)
        return None
    
def extract_metadata(file):
    presentation = Presentation(file)
    metadata = get_propierties(presentation, file)
    return metadata    