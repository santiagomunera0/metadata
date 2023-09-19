import os
import pathlib

import pandas as pd
from src.common.common_tools import parameters
import src.extract.power_point as ppt
import src.extract.excel as xls
import src.extract.word as doc
import src.extract.pdf as pdf

df_excel = pd.DataFrame(columns=["Titulo", "Autor", "Asunto", "Palabras_Clave", "File_Size", "Fecha_Creacion", "Fecha_Modificacion", "Categoria"])

def extract_metadata(ruta_archivo):
    path = pathlib.Path(ruta_archivo)
    print(path.suffix)
    match path.suffix:
        case ".pdf":
            pdf.extract_metadata(ruta_archivo)
        case ".pptx":
           df_ppt = df_ppt.append(ppt.extract_metadata(ruta_archivo), ignore_index = True)
        case ".xlsx":
            global df_excel
            xls.extract_metadata(ruta_archivo)
            metadata_excel = xls.extract_metadata(ruta_archivo)
            df_excel = pd.concat([df_excel, metadata_excel], ignore_index=True)
        case ".docx":
            doc.extract_metadata(ruta_archivo)
    print(df_excel)