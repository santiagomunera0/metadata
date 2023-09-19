import fitz
import os

from src.common.common_tools import parameters

def get_propierties(pdf, file):
    file_size_mb = os.path.getsize(file) / (1024 * 1024)
    try:
        metadata = {
            'Titulo': pdf.metadata.get('title', ''),
            'Autor': pdf.metadata.get('author', ''),
            'Asunto': pdf.metadata.get('subject', ''),
            'Palabras_Clave': pdf.metadata.get('keywords', ''),
            "File_Size": round(file_size_mb, 2),
            'Fecha_Creacion': pdf.metadata.get('creationDate', ''),
            'Fecha_Modificacion': pdf.metadata.get('modDate', '')
        }

        return metadata

    except Exception as e:
        print("Error:", e)
        return None
    
def extract_metadata(file):
    pdf_document = fitz.open(file)
    metadata = get_propierties(pdf_document, file)    

    print(metadata)     