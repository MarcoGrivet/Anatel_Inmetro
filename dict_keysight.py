general_patterns = {
        "Certificado Nº": r"Certificado Nº\s+([\w\-]+)",
        "Equipamento": r"Descrição\s+(.+?)(?=\s{2,})",
        "Fabricante": r"Fabricante\s+(.+?)(?=\s{5,})", 
        "Modelo": r"Modelo Nº\s+(\w+)",   
        "No. de Série": r"Série Nº\s+(\w+)",
        "Data da Calibração": r"Data da Calibração\s+([0-9]{1,2} \w{3} [0-9]{1,4})"      
    }
