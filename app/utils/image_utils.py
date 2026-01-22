import cv2
import numpy as np

def load_image(path: str) -> np.ndarray:
    image = cv2.imread(path)
    if image is None:
        raise ValueError("Image non trouvée")
    return image
