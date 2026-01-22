from app.graph.invoice_graph import build_invoice_graph

def run_invoice_agent(image_path: str):
    graph = build_invoice_graph()

    state = {
        "image_path": image_path
    }

    result = graph.invoke(state)
    return result
