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
  files, list_xls, list_doc, list_ppt, list_pdf = [], [], [], [], []

  for file in os.listdir(path):
    file_path = os.path.join(path, file)
    if os.path.isfile(file_path):
      files.append(file)
      extension = pathlib.Path(file_path)
      match extension.suffix:
        case ".xlsx":
          list_xls.append(extract_xls(file_path))
        case ".docx":
          list_doc.append(extract_doc(file_path))
        case ".pptx":
          list_ppt.append(extract_ppt(file_path))
        case ".pdf":
          list_pdf.append(extract_pdf(file_path))  

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

if __name__=="__main__":
  check_directories(parameters)
  read_files(parameters['docs'])