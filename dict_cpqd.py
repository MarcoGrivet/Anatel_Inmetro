general_patterns = {
        "Certificado Nº": r"Número:\s+(DOT-[0-9]{1,5}.CC.[0-9]{1,2}-[A-Z]{1})",
        "Equipamento": r"Equipamento:\s+(\w+(?: \w+){0,2})",
        "Fabricante": r"Fabricante:\s+(.+)",
        "Modelo": r"Modelo:\s+(\w+)",  
        "No. de Série": r"Número de Série:\s+(\w+)",
        "Data da Calibração": r"Data da calibração:\s+([0-9]{1,2}\/[a-z]{3}\/[0-9]{4})"
}
