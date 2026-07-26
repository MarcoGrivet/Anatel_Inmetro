general_patterns = {
        "Certificado Nº": r"CERTIFICADO DE CALIBRAÇÃO No\s+([\w\-]+)",
        "Equipamento": r"Item:\s+(.+)",
        "Fabricante": r"marca\s*([^,]*)", 
        "Modelo": r"modelo\s*([^,]*)",   
        "No. de Série": r"série no\s*([^,]*)",
        "Data da Calibração": r"Data da execução da calibração:\s+([0-9]{2}.[0-9]{2}.[0-9]{4})"      
    }
