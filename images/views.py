from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse

from .images import convert_image

def home_page(request):
    if request.method == "POST":
        # We are get uploaded file from request
        uploaded_file = request.FILES['file']
        # Then we make an object of file handling class
        f = FileSystemStorage()
        # And saving file with 1st - name of file, 2nd - file instance itself
        name = f.save(uploaded_file.name, uploaded_file)
        edited_file_name = convert_image(name)
        if edited_file_name:
            url = f.url(uploaded_file.name)
            edited_url = f.url(edited_file_name)
        else:
            HttpResponse('Something goes wrong')
        return render(request, 'images/home.html', {'url': url,
    'edited_url': edited_url})
    else :
       return render(request, 'images/home.html', {}) 
