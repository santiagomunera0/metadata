from docx import Document
import os
from datetime import datetime

from src.common.common_tools import parameters

def get_propierties(document, file):
    file_size_mb = os.path.getsize(file) / (1024 * 1024)
    try:
        metadata = { 
            "Título": document.core_properties.title,
            "Autor": document.core_properties.author,
            "Asunto": document.core_properties.subject,
            "Palabras Clave": document.core_properties.keywords,
            "File Size (MB)": round(file_size_mb, 2),
            "Fecha de Creación": datetime.fromtimestamp(os.path.getctime(archivo_path)).strftime('%Y-%m-%d %H:%M:%S'),
            "Fecha de Modificación": datetime.fromtimestamp(os.path.getmtime(archivo_path)).strftime('%Y-%m-%d %H:%M:%S')
        }

        return metadata

    except Exception as e:
        print("Error:", e)
        return None
    
def extract_metadata(file): 
    document = Document(file)
    metadata = get_propierties(document, file)    

    print(metadata)
