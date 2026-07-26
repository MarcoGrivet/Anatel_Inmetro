#==============================================================================
#  Projeto 31864 - ANATEL/INMETRO/DIMCI/MEDIÇÃO ANATEL
#  Meta II   - Estudo e Proposição de Ontologias e Formatos para Coleta e 
#              Armazenamento de Dados e Registros do SGM
#  Produto I - Coleta de Dados Digitais : Recuperação de Legado
#  Autor     - Marco Antonio Grivet Mattoso Maia
#============================================================================== 
#                             PROGRAMA PRINCIPAL

import os, time
import pandas as pd  
import importlib
from pathlib import Path

# Diretório Master dos certificados
PDF_CERTIFIC    = "D:/EMPRESAS/ANATEL_INMETRO/Certificados"
# Subdiretório que contem os certificados
PDF_BANK        = "Certificados_SEI_de_2018_a_nove2025"

PDF_DIRECTORY   = Path(PDF_CERTIFIC) / PDF_BANK
#print("DIRECTORY", PDF_DIRECTORY)

FIRST_CERTIFIC = 275    # no. do primeiro certificado a ser processado
LAST_CERTIFIC  = 275    # no. do último   certificado a ser processado

DEBUG = 0 # 0=no print   1=print text   2=print data
STORE = 0 # 0=dont save  1=save

# Para evitar erros em alguns certificados, certos laboratórios podem ser excluidos
EXCLUDED = ["flir", "Wavecontrol", "PUCRS"]

# Dicionário de identificadores dos laboratórios de certificação
search_dict = { "anritsu" : "Anritsu Company",
                "bird"    : "The RF Experts", 
                "celplan" : "celplan",
                "cpqd"    : "Fundação CPqD", 
                "cpqd"    : "CPqD Calibration Laboratory",
                "cpqd"    : "CPqD",
                "ctj"     : "ctj@grupoctj.com.br",
                "flir"    : "FLIR Systems Brasil",
                "inpe"    : "Homepage: www.lit.inpe.br",
                "ipt1"    : "Laboratório de Metrologia Mecânica",
                "ipt2"    : "Laboratório de Metrologia Elétrica",
                "keysight": "Keysight Technologies",
                "PUCRS"   : "Pontifícia Universidade Católica do Rio Grande do Sul",   
                "R&S"     : "rohde&schwarz",
                "Wavecontrol":"LabCal - Wavecontrol"               
            }

#------------------------------------------------------------------------------
# Rotina para impressão do conteúdo dos certificados para verificar o que de
# fato foi lido
 
def print_text(text, ALL):
    if ALL:
        npages = len(text)
    else:
        npages = 1
    for pages in range(npages):
        print(f"-------- PAGE {pages} --------\n")
        print(text[pages])
#------------------------------------------------------------------------------
# === MAIN ===
#------------------------------------------------------------------------------
# Importação da bliblioteca de rotinas
PDFLIB = importlib.import_module("my_pdf_library")

# Criação/leitura do dataframe onde parâmetros administrativos serão armazenados 
# Se for encontrado o arquivo "destination", resultados são a ele apensados.
# Caso contrário, o arquivo "destination" é criado vazio.
destination = os.path.join(PDF_DIRECTORY, "_extracted_attributes.xlsx")
KEEP = False
if KEEP:
    try:
        df_attribs = pd.read_excel(destination)
        start_row  = len(df_attribs)
        print("\n\tFile loaded successfully!")
    except FileNotFoundError:
        print(f"⚠️ File not found")
        start_row = 0
        colunas     = ["Arquivo", "Tipo", "Categoria", "Certificado Nº", "Equipamento", "Fabricante", "Modelo", "No. de Série", "Data da Calibração"]  
        df_attribs  = pd.DataFrame(columns=colunas) 
else:
    start_row = 0
    colunas     = ["Arquivo", "Tipo", "Categoria", "Certificado Nº", "Equipamento", "Fabricante", "Modelo", "No. de Série", "Data da Calibração"]  
    df_attribs  = pd.DataFrame(columns=colunas) 


# Seleção dos certificados a serem processados
folder    = Path(PDF_DIRECTORY)
files     = sorted(folder.glob("*.pdf"))
files_str = [str(p) for p in files]
n_files   = len(files_str)
print('\tNO. DE CERTIFICADOS = ',n_files)

GENLIST = False
if GENLIST:
    df_pdf = pd.DataFrame(files_str, columns=["Arquivo"])
    df_pdf.head()
    df_pdf.to_excel("global_pdf_list.xlsx", index=False)
#
#--------- LOOP PRINCIPAL --------------------------------------------------------------
#
for k in range(FIRST_CERTIFIC-1,LAST_CERTIFIC):
    start = time.time()
    pdf_file   = files_str[k]
    short_name = os.path.basename(pdf_file)
    print("\n-------------------------------------------------------------------")
    print(f"\n{k+1:3d} File : {short_name}")

# Detecção do tipo dearquivo PDF
    pdf_type = PDFLIB.check_if_pdf_is_image(pdf_file)
    if pdf_type:
        print("\tPDF is flattened")
    else:
        print("\tPDF is textual")

# Extração do conteúdo do certificado       
    full_text, full_data = PDFLIB.extract_pdf_text(pdf_file, pdf_type, True)
    if DEBUG==1:
        print("\n-------- TEXT --------\n")
        print_text(full_text, True)
    if DEBUG==2:
        print("\n-------- DATA --------\n")
        print_text(full_data, True)

# Detecção do laboratório de certificação
    result   = ''.join(full_text.values())
    category = PDFLIB.search_category(result, search_dict)
    if category == 'not found':
        print ("\tCategory not found....\n")
        row = len(df_attribs)
        df_attribs.loc[row, "Arquivo"]   = short_name
        df_attribs.loc[row, "Tipo"]      = pdf_type 
        df_attribs.loc[row, "Categoria"] = "UNKNOWN" 
        continue 
    print(f"\tCategory = {category.upper():s}\n")

# Para evitar erros em alguns certificados, certos laboratórios podem ser excluidos
    if category in EXCLUDED:
        row = len(df_attribs)
        df_attribs.loc[row, "Arquivo"]   = short_name
        df_attribs.loc[row, "Tipo"]      = pdf_type 
        df_attribs.loc[row, "Categoria"] = category 
        continue

# Seleção do dicionário de expressões regulares para o laboratório específico     
    dict_name = "dict_"+ category
    module = importlib.import_module(dict_name)
    general_patterns = module.general_patterns

# Extração dos pares (atributo, valor)
    kv_pairs = PDFLIB.extract_key_value_pairs(full_text, general_patterns)
    for m in range(len(kv_pairs)):       
        print(f"\t{kv_pairs[m][0]:20s} = {kv_pairs[m][1]:s}")
        if kv_pairs[m][1] == "NOT FOUND":
            continue
        if kv_pairs[m][0]=="Data da Calibração":
            key, value  = kv_pairs[m]
            kv_pairs[m] = (key, PDFLIB.convert_date(value))   # new tuple
        #print(f"\t{kv_pairs[m][0]:20s} = {kv_pairs[m][1]:s}")

    row = len(df_attribs)
    df_attribs.loc[row, "Arquivo"]   = short_name
    df_attribs.loc[row, "Tipo"]      = pdf_type 
    df_attribs.loc[row, "Categoria"] = category 
    cols = df_attribs.columns[3:9]
    df_attribs.loc[row, cols] = [kv_pairs[p][1] for p in range(6)] 

# Gravação dos parâmetros coletados em uma planilha EXCEL
if STORE:
    print(df_attribs)
    destination = os.path.join(PDF_DIRECTORY, "_extracted_attributes.xlsx")
    df_attribs.to_excel(destination, index=False) 
    
print(f"\n\tDuration {time.time()-start:.3f} sec.")
print("\n-------------------------------------------------------------------")
