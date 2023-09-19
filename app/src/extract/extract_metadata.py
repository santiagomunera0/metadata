import os
import pathlib

import pandas as pd
from src.common.common_tools import parameters
import src.extract.power_point as ppt
import src.extract.excel as xls
import src.extract.word as doc
import src.extract.pdf as pdf

def extract_metadata(ruta_archivo):
    df_excel= pd.DataFrame({})
    path = pathlib.Path(ruta_archivo)
    print(path.suffix)
    match path.suffix:
        case ".pdf":
            pdf.extract_metadata(ruta_archivo)
        case ".pptx":
           df_ppt = df_ppt.append(ppt.extract_metadata(ruta_archivo), ignore_index = True)
        case ".xlsx":
            xls.extract_metadata(ruta_archivo)
            df_excel = df_excel.append(xls.extract_metadata(ruta_archivo), ignore_index = True)
        case ".docx":
            doc.extract_metadata(ruta_archivo)
    print(df_excel)