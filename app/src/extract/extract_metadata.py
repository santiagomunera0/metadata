import os

from src.common.common_tools import parameters
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