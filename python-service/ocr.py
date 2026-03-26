import pytesseract
from PIL import Image
import re

# Set path (Windows users)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text(documents):
    extracted = {}

    for doc in documents:
        try:
            img = Image.open(doc["path"])
            text = pytesseract.image_to_string(img)

            # Extract Aadhaar number (12 digit)
            aadhar = re.findall(r'\b\d{4}\s\d{4}\s\d{4}\b', text)
            if aadhar:
                extracted["aadhar"] = aadhar[0]

            # Extract PAN number
            pan = re.findall(r'[A-Z]{5}[0-9]{4}[A-Z]', text)
            if pan:
                extracted["pan"] = pan[0]

        except Exception as e:
            print("OCR Error:", e)

    return extracted
