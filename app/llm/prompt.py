INVOICE_PROMPT = """
Tu es un expert comptable tunisien.

À partir du texte OCR suivant d'une facture,
extrais STRICTEMENT les champs suivants en JSON valide :

- invoiceNumber
- supplierName
- supplierMatricule
- invoiceDate (YYYY-MM-DD)
- totalHT
- totalTVA
- totalTTC
- currency

Texte facture :
{text}

Retourne uniquement le JSON, sans explication.
"""
