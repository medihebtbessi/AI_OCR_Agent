from langgraph.graph import StateGraph
from app.graph.state import InvoiceState
from app.utils.image_utils import load_image
from app.ocr.preprocessing import preprocess_image
from app.ocr.tesseract_ocr import extract_text
from app.llm.extractor import extract_invoice_data
from app.validation.invoice_validator import validate_invoice
from app.mcp.mcp_client import send_invoice_to_backend
from app.config import OCR_LANG

def build_invoice_graph():

    graph = StateGraph(InvoiceState)

    graph.add_node("load_image", lambda s: {
        **s, "image": load_image(s["image_path"])
    })

    graph.add_node("preprocess", lambda s: {
        **s, "processed_image": preprocess_image(s["image"])
    })

    graph.add_node("ocr", lambda s: {
        **s, "ocr_text": extract_text(s["processed_image"], OCR_LANG)
    })

    graph.add_node("llm", lambda s: {
        **s, "invoice_data": extract_invoice_data(s["ocr_text"])
    })

    graph.add_node("validate", lambda s: {
        **s,
        "confidence": validate_invoice(s["invoice_data"])[1]
    })

    graph.add_node("send", lambda s: send_invoice_to_backend(s["invoice_data"]))

    graph.set_entry_point("load_image")

    graph.add_edge("load_image", "preprocess")
    graph.add_edge("preprocess", "ocr")
    graph.add_edge("ocr", "llm")
    graph.add_edge("llm", "validate")
    graph.add_edge("validate", "send")

    graph.set_finish_point("send")

    return graph.compile()
