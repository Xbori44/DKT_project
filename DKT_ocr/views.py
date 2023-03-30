from django.shortcuts import render
from .forms import UploadImageForm
from .ocr_processing import extract_text_from_image
import pytesseract

def ocr_view(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = request.FILES['image']
            extracted_text = extract_text_from_image(image)
            return render(request, 'DKT_ocr/ocr.html', {'form': form, 'extracted_text': extracted_text})
    else:
        form = UploadImageForm()
    return render(request, 'DKT_ocr/ocr.html', {'form': form})
