general_patterns = {
        "Certificado Nº": r"Calibration Certificate:\s+([A-Z]{1}-[0-9]{1,4}/[0-9]{2})",
        "Equipamento": r"Instrumento:\s+(\w+(?: \w+){0,2})",
        "Fabricante": r"Modelo / Tipo:\s+(\w+(?: \w+){0,2})",
        "Modelo": r"Modelo / Tipo:\s.{40}(.*)", #r"([A-Za-z\s]+)(?=Manufacturer:)",  
        "No. de Série": r"Cód. de Identificação:\s+(\w+)",
        "Data da Calibração": r"Calibration Date :\s+([0-9]{2}/[0-9]{2}/[0-9]{4})"
}