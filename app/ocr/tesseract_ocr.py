import pytesseract
from PIL import Image
import os

# Chemin vers l'exécutable Tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Comme TESSDATA_PREFIX est déjà défini dans Windows, pas besoin de le redéfinir ici
# os.environ['TESSDATA_PREFIX'] = r"C:\Program Files\Tesseract-OCR\tessdata"

def extract_text(image: Image.Image, lang="fra") -> str:
    """
    Extrait le texte d'une image en utilisant Tesseract OCR.

    :param image: Image PIL
    :param lang: Code langue Tesseract (par défaut "fra")
    :return: Texte extrait
    """
    try:
        text = pytesseract.image_to_string(image, lang=lang)
        return text.strip()
    except pytesseract.TesseractError as e:
        print("Erreur Tesseract:", e)
        return ""
