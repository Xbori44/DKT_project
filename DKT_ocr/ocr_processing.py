import pytesseract
from PIL import Image

# set path to Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_image(image):
    img = Image.open(image)
    text = pytesseract.image_to_string(img, lang="eng+kor")
    return text
