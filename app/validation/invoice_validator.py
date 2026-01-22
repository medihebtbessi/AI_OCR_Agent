def validate_invoice(data: dict) -> tuple[bool, float]:
    required_fields = [
        "invoiceNumber", "supplierName", "invoiceDate",
        "totalHT", "totalTVA", "totalTTC"
    ]

    score = 0
    for field in required_fields:
        if field in data and data[field]:
            score += 1

    confidence = score / len(required_fields)
    return confidence >= 0.7, confidence
