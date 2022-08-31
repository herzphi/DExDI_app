from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
# Imaginary function to handle an uploaded file.
#from somewhere import handle_uploaded_file


def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def index(request):
    return render(request, 'pm_graphs/index.html')


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'pm_graphs/upload_file.html', {'form': form})

