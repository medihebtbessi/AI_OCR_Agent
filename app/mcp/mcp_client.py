import requests
from app.utils.logger import logger
from app.config import MCP_SERVER_URL


def send_invoice_to_backend(invoice_data: dict):
    """
    Client MCP simplifié :
    - envoie un tool-call au serveur Spring Boot
    """

    payload = {
        "tool": "save_invoice",
        "args": invoice_data
    }

    try:
        response = requests.post(
            MCP_SERVER_URL,
            json=payload,
            timeout=10
        )
        response.raise_for_status()

        logger.info("Facture envoyée au backend via MCP")
        return response.json()

    except requests.RequestException as e:
        logger.error(f"Erreur MCP : {e}")
        raise
