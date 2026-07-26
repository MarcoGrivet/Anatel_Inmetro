general_patterns = {
        "Certificado Nº": r"Certificado de Calibração N\s+([\w\-]+)",
        "Equipamento": r"Item:\s+(.+)",
        "Fabricante": r"marca\s+([\w]+)", 
        "Modelo": r"modelo\s+([\w]+)",   
        "No. de Série": r"série n\s+([\w]+)",
        "Data da Calibração": r"Data da execução da calibração:\s+([0-9]{2}.[0-9]{2}.[0-9]{4})"      
    }
