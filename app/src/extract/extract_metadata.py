import os
import pathlib

import pandas as pd
from src.common.common_tools import parameters
import src.extract.power_point as ppt
import src.extract.excel as xls
import src.extract.word as doc
import src.extract.pdf as pdf

def extract_xls(file):
  dic_xls = xls.extract_metadata(file)
  return dic_xls

def extract_doc(file):
  df_doc = doc.extract_metadata(file)
  return df_doc

def extract_ppt(file):
  df_ppt = ppt.extract_metadata(file)
  return df_ppt

def extract_pdf(file):
  df_pdf = pdf.extract_metadata(file)
  return df_pdf