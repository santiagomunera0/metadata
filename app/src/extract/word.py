from docx import Document
import os
from datetime import datetime

from src.common.common_tools import parameters

def get_propierties(document, file):
    file_size_mb = os.path.getsize(file) / (1024 * 1024)
    try:
        metadata = { 
            "Titulo": document.core_properties.title,
            "Autor": document.core_properties.author,
            "Asunto": document.core_properties.subject,
            "Palabras_Clave": document.core_properties.keywords,
            "File_Size": round(file_size_mb, 2),
            "Fecha_Creacion": document.core_properties.created,
            "Fecha_Modificación": document.core_properties.modified,
            "Categoria" : document.core_properties.category
        }

        return metadata

    except Exception as e:
        print("Error:", e)
        return None
    
def extract_metadata(file): 
    document = Document(file)
    metadata = get_propierties(document, file)    

    print(metadata)
