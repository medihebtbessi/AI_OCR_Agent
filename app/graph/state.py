from typing import TypedDict, Any

class InvoiceState(TypedDict):
    image_path: str
    image: Any
    processed_image: Any
    ocr_text: str
    invoice_data: dict
    confidence: float
