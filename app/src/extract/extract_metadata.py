import os

from src.common.common_tools import parameters
import src.extract.power_point as ppt
import src.extract.excel as xls
import src.extract.word as doc
import src.extract.pdf as pdf

def extract_metadata():
    ppt_file = os.path.join(parameters['docs'], 'test.pptx')
    xls_file = os.path.join(parameters['docs'], 'test.xlsx')
    doc_file = os.path.join(parameters['docs'], 'test.docx') 
    pdf_file = os.path.join(parameters['docs'], 'test.pdf')

    ppt.extract_metadata(ppt_file)
    xls.extract_metadata(xls_file)
    doc.extract_metadata(doc_file)  
    pdf.extract_metadata(pdf_file)