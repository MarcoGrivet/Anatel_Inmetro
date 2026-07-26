#==============================================================================
#  Projeto 31864 - ANATEL/INMETRO/DIMCI/MEDICAO ANATEL
#  Meta II   - Estudo e Proposição de Ontologias e Formatos para Coleta e 
#              Armazenamento de Dados e Registros do SGM
#  Produto I - Coleta de Dados Digitais : Recuperação de Legado
#  Autor     - Marco Antonio Grivet Mattoso Maia
#============================================================================== 
#                             BIBLIOTECA DE SUPORTE


import pymupdf                 # install PyMuPDF
import re, os
import pandas as pd
import pdfplumber
import pytesseract
from dataclasses import dataclass
from typing import List, Tuple, Dict, Any

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

RESOLUTION = 300
#------------------------------------------------------------------------------
def check_if_pdf_is_image(fname):
    doc = pymupdf.open(fname)
    if doc[0].get_text():
        return False       # if PDF textual
    else:
        return True        # if PDF flattened  
#------------------------------------------------------------------------------
def search_category(text, dict):
    for k in range(len(dict)):
        key  = list(dict.keys())[k]
        name = dict[key]
        if name.lower() in text.lower():
            return key
    return('not found') 
#------------------------------------------------------------------------------
def extract_pdf_text(fname, type, condition):
    pdf_dict_text= {}
    pdf_dict_data= {}
    if type:    # PDF is flattened            
        with pdfplumber.open(fname) as pdf:
            for i, page in enumerate(pdf.pages):
                # Convert page to high-res image
                pil_image = page.to_image(resolution=RESOLUTION).original
                # OCR full text
                text = pytesseract.image_to_string(pil_image, lang="eng")
                # OCR structured data (word-level with positions)
                data = pytesseract.image_to_data(pil_image, output_type=pytesseract.Output.DICT) 
                pdf_dict_text[i] = text
                pdf_dict_data[i] = data
    else:       # PDF is textual
        with pymupdf.open(fname) as doc:
            toc = doc.get_toc()
            for i, page in enumerate(doc):
                # sort the extracted text in reading order.
                texto = page.get_text(sort=condition)   
                # remove blank lines
                clean1 = "\n".join(line for line in texto.splitlines() if line.strip())
                # remove leading blanks
                clean2 = "\n".join(line.lstrip() for line in clean1.splitlines())
                pdf_dict_text[i] = clean2
                pdf_dict_data[i] = []
 
    return pdf_dict_text, pdf_dict_data
#------------------------------------------------------------------------------
def extract_key_value_pairs(pdf_dict_text, dictionary):
    pairs = []
    
    for label, pattern in dictionary.items():
        found= False
        for page_num in range(len(pdf_dict_text)):
            match = re.search(pattern, pdf_dict_text[page_num])
            if match:
                pairs.append((label, match.group(1).strip()))
                #print(f'\t{label} : {match.group(1).strip()}')
                found = True
                break
        if not found:
            pairs.append((label, 'NOT FOUND'))
            #print(f'\t{label} : NOT FOUND')

    return pairs
#------------------------------------------------------------------------------
import re

# Portuguese month names and abbreviations
MESES = {
    "janeiro":   1, "jan": 1, "Jan": 1,
    "fevereiro": 2, "feb": 2, "Feb": 2, "fev": 2,
    "março":     3, "mar": 3, "Mar": 3,
    "abril":     4, "apr": 4, "Apr": 4, "abr": 4,
    "maio":      5, "mai": 5, "Mai": 5, "may": 5,
    "junho":     6, "jun": 6, "Jun": 6,
    "julho":     7, "jul": 7, "Jul": 7,
    "agosto":    8, "aug": 8, "Aug": 8, "ago": 8,
    "setembro":  9, "sep": 9, "Sep": 9, "set": 9,
    "outubro":  10, "oct": 10,"Oct": 10,"out": 10,
    "novembro": 11, "nov": 11,"Nov": 11,
    "dezembro": 12, "dec": 12,"Dec": 12,"dez": 12
}
#------------------------------------------------------------------------------
def convert_date(date_str):
    s = date_str.lower().strip()
    # -----------------------------------------------
    # 1. Format: "24 de junho de 2025"
    # -----------------------------------------------
    m = re.match(r"(\d{1,2})\s+de\s+([a-zç]+)\s+de\s+(\d{4})", s)
    if m:
        d, month_name, y = m.groups()
        m_num = MESES[month_name]
        return f"{int(d):02d}/{m_num:02d}/{y}"
    # -----------------------------------------------
    # 2. Numeric formats: "24/06/2025", "24.06.2025", "24-06-2025"
    # -----------------------------------------------
    m = re.match(r"(\d{1,2})[./-](\d{1,2})[./-](\d{4})", s)
    if m:
        d, m_num, y = m.groups()
        return f"{int(d):02d}/{int(m_num):02d}/{y}"
    # -----------------------------------------------
    # 3. Mixed abbrev: "24/jun/2025" or "24 jun 2025"
    # -----------------------------------------------
    m = re.match(r"(\d{1,2})[ ./-]([a-zç]+)[ ./-](\d{4})", s)
    if m:
        d, month_name, y = m.groups()
        #print("MONTH",month_name)
        m_num = MESES[month_name]
        return f"{int(d):02d}/{m_num:02d}/{y}"
    raise ValueError(f"Formato de data desconhecido: {date_str}")
