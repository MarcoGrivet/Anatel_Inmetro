general_patterns = {
        "Certificado Nº": r"Certificate/SO Number:\s+([\w\-]+)",
        "Equipamento": r"Description:\s+((?:(?!\s{5}).)+)",
        "Fabricante": r"Manufacturer:\s+((?:(?!\s{5}).)+)", 
        "Modelo": r"Model Number:\s+((?:(?!\s{5}).)+)",   
        "No. de Série": r"Serial Number:\s+((?:(?!\s{5}).)+)",
        "Data da Calibração": r"Calibration Date:\s+([0-9]{2}.[0-9]{2}.[0-9]{4})"      
    }