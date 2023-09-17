from openpyxl import load_workbook
import os
import time


from src.common.common_tools import parameters

def get_propierties(excel, file):
    file_size_mb = os.path.getsize(file) / (1024 * 1024)
    try:
        metadata = {
            "Título": excel.properties.title,
            "Autor": excel.properties.creator,
            "Asunto": excel.properties.subject,
            "Palabras Clave": excel.properties.keywords,
            "File Size (MB)": round(file_size_mb, 2),
            "Fecha de Creación" : excel.strftime('%Y-%m-%d %H:%M:%S'),
            "Fecha de Modificación" : excel.strftime('%Y-%m-%d %H:%M:%S')
        }

        return metadata

    except Exception as e:
        print("Error:", e)
        return None
    
def extract_metadata(file):
    excel = load_workbook(file, read_only=True)
    metadata = get_propierties(excel, file)    

    print(metadata)    
