import os
import pathlib
import pandas as pd
from src.common.common_tools import parameters, check_directories
from src.extract.extract_metadata import extract_xls, extract_doc, extract_pdf, extract_ppt

def list_metadata_to_dataframe(list, format):
  df = pd.DataFrame(list).reset_index(drop=True)
  export_path_file = os.path.join(parameters['raw'], f'{format}_metadata.csv')
  df.to_csv(export_path_file, index=False)
  return df

def read_files(path):
  list_data_unified = []
  files, list_xls, list_doc, list_ppt, list_pdf = [], [], [], [], []

  for file in os.listdir(path):
    file_path = os.path.join(path, file)
    if os.path.isfile(file_path):
      files.append(file)
      extension = pathlib.Path(file_path)
      match extension.suffix:
        case ".xlsx":
          dict_xls = extract_xls(file_path)
          list_data_unified.append(list(dict_xls.values()))
          list_xls.append(dict_xls)
        case ".docx":
          dict_doc = extract_doc(file_path)
          list_data_unified.append(list(dict_doc.values()))
          list_doc.append(dict_doc)
        case ".pptx":
          dict_ppt = extract_ppt(file_path)
          list_data_unified.append(list(dict_ppt.values()))
          list_ppt.append(dict_ppt)
        case ".pdf":
          dict_pdf = extract_pdf(file_path)
          list_data_unified.append(list(dict_pdf.values()))
          list_pdf.append(dict_pdf)

  print("***************")
  print("   exporting xls metadata...")
  list_metadata_to_dataframe(list_xls, 'xls')
  print("   xls metadata exported...")
  print("***************")
  print("   exporting doc metadata...")
  list_metadata_to_dataframe(list_doc, 'doc')
  print("   doc metadata exported...")
  print("***************")
  print("   exporting ppt metadata...")
  list_metadata_to_dataframe(list_ppt, 'ppt')
  print("   ppt metadata exported...")
  print("***************")
  print("   exporting pdf metadata...")
  list_metadata_to_dataframe(list_pdf, 'pdf')
  print("   pdf metadata exported...")
  print("***************")

  df_data_unified = pd.DataFrame(data=list_data_unified, columns=['Titulo', 'Autor', 'Asunto', 'Palabras_Clave', 'File_Size', 'Fecha_Creacion', 'Fecha_Modificacion', 'Categoria', 'Comentarios', 'Numero_Paginas'])
  export_path_file = os.path.join(parameters['raw'], f'data_unified_metadata.csv')
  df_data_unified.to_csv(export_path_file, index=False)

if __name__=="__main__":
  check_directories(parameters)
  read_files(parameters['docs'])