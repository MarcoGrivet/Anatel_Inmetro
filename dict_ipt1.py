general_patterns = {
        "Certificado Nº": r"CERTIFICADO DE CALIBRAÇÃO N°\s+([\w\-\ ]+)",
        "Equipamento": r"Item:\s+(.+)",
        "Fabricante": r"Fabricante:\s+([\w]+)", 
        "Modelo": r"Modelo:\s+([\w\ ]+)",   
        "No. de Série": r"Nº de série:\s+([\w]+)",
        "Data da Calibração": r"São Paulo,\s+([0-9]{2} de [a-z]{1,} de [0-9]{4})"      
    }
