from openpyxl import load_workbook
import os
from datetime import datetime
import pandas as pd

from src.common.common_tools import parameters

def get_propierties(excel, file):
    file_size_mb = os.path.getsize(file) / (1024 * 1024)
    try:
        metadata = {
            "Titulo": excel.properties.title,
            "Autor": excel.properties.creator,
            "Asunto": excel.properties.subject,
            "Palabras_Clave": excel.properties.keywords,
            "File_Size": round(file_size_mb, 2),
            "Fecha_Creacion": excel.properties.created,
            "Fecha_Modificacion": excel.properties.modified,
            "Categoria": excel.properties.category
        }
        


        return metadata

    except Exception as e:
        print("Error:", e)
        return None
    
def extract_metadata(file):
    excel = load_workbook(file, read_only=True)
    metadata = get_propierties(excel, file)    

    print(metadata)  
    result = pd.DataFrame([metadata])
    return result
  
