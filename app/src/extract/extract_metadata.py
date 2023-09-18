""" import os
import pandas as pd """

""" from src.common.common_tools import parameters, multiple_files
import src.extract.power_point as ppt
import src.extract.excel as xls
import src.extract.word as doc

def extract_metadata():
    ppt_file = os.path.join(parameters['docs'], 'test.pptx')
    xls_file = os.path.join(parameters['docs'], 'test.xlsx')
    doc_file = file = os.path.join(parameters['docs'], 'test.docx') 

    ppt.extract_metadata(ppt_file)
    xls.extract_metadata(xls_file)
    doc.extract_metadata(doc_file)  

metadata_list = multiple_files(extract_metadata())

df = pd.DataFrame(metadata_list)
print(df) """

import os
import pandas as pd

from src.common.common_tools import parameters
import src.extract.power_point as ppt
import src.extract.excel as xls
import src.extract.word as doc

def extract_metadata(files):
    all_metadata = []  # Lista para almacenar metadatos de todos los archivos
    for file in files:
        metadata = extract_metadata_from_file(file)
        if metadata:
            all_metadata.append(metadata)  # Agrega los metadatos a la lista
    return all_metadata

def extract_metadata_from_file(file):
    # Aquí debes llamar a la función correspondiente según el tipo de archivo
    if file.endswith('.pptx'):
        return ppt.extract_metadata(file)
    elif file.endswith('.xlsx'):
        return xls.extract_metadata(file)
    elif file.endswith('.docx'):
        return doc.extract_metadata(file)
    else:
        return None

# Definir la lista de archivos a procesar
file_list = [
    os.path.join(parameters['docs'], 'test.pptx'),
    os.path.join(parameters['docs'], 'test.xlsx'),
    os.path.join(parameters['docs'], 'test.docx')
]

# Llamar a la función extract_metadata para extraer metadatos de los archivos
metadata_list = extract_metadata(file_list)

# metadata_list ahora contiene los metadatos de los archivos procesados

# Convierte metadata_list en un DataFrame
df = pd.DataFrame(metadata_list)

# Imprimir el DataFrame
print(df)