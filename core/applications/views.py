from django.shortcuts import render
from .forms import UploadFileForm
from .utils import process_excel_file  # создадим позже

def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            process_excel_file(file)
            return render(request, "applications/success.html")
    else:
        form = UploadFileForm()
    return render(request, "applications/upload.html", {'form': form})
