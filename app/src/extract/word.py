from docx import Document
import os

from src.common.common_tools import parameters

def get_propierties(document, file):
    file_size_mb = os.path.getsize(file) / (1024 * 1024)
    try:
        metadata = { 
            "Título": document.core_properties.title,
            "Autor": document.core_properties.author,
            "Asunto": document.core_properties.subject,
            "Palabras Clave": document.core_properties.keywords,
            "File Size (MB)": round(file_size_mb, 2)
        }

        return metadata

    except Exception as e:
        print("Error:", e)
        return None
    
def extract_metadata(file): 
    document = Document(file)
    metadata = get_propierties(document, file)    

    print(metadata)