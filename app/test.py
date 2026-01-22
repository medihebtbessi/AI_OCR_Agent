from PIL import Image
from app.ocr.tesseract_ocr import extract_text

img = Image.open("data/samples/invoice_sample.jpg")  # remplace par une image test
print(extract_text(img, lang="fra"))
