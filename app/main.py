from app.agents.invoice_agent import run_invoice_agent
from app.utils.logger import logger

if __name__ == "__main__":
    image_path = "data/samples/invoice_sample.jpg"

    logger.info("Démarrage agent OCR facture")
    result = run_invoice_agent(image_path)

    logger.info("Facture envoyée au backend avec succès")
