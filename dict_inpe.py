general_patterns = {
        "Certificado Nº": r"NUMBER:\s+([\w\.-]+)",
        "Equipamento": r"OBJETO:\s+(\w+(?: \w+){0,2})",
        "Fabricante": r"FABRICANTE:\s+(\w+(?: \w+){0,2})",
        "Modelo": r"MODELO:\s+(\w+)",  
        "No. de Série": r"DE SÉRIE:\s+(\w+)",
        "Data da Calibração": r"DATA DA CALIBRAÇÃO:\s+([0-9]{2}/[0-9]{2}/[0-9]{4})"
}
